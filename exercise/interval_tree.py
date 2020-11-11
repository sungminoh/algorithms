#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from pprint import pprint
import pytest
import csv
from typing import Union
from typing import Any
from typing import Tuple
from typing import IO
from types import FunctionType
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Interval(object):
    l: Any
    r: Any

    def overlap(self, interval: 'Interval'):
        return interval.l <= self.l <= interval.r \
            or interval.l <= self.r <= interval.r \
            or self.l <= interval.l <= self.r \
            or self.l <= interval.r <= self.r

    def __eq__(self, interval: 'Interval'):
        return self.l == interval.l and self.r == interval.r


class IntervalTree(object):
    class Node(Interval):
        def __init__(self, interval: Interval):
            super().__init__(**interval.__dict__)
            self.max_r = interval.r
            self.parent = None
            self.left = None
            self.right = None

        def insert(self, node):
            if node.r > self.max_r:
                self.max_r = node.r
            if node.l < self.l:
                if self.left:
                    self.left.insert(node)
                else:
                    node.parent = self
                    self.left = node
            else:
                if self.right:
                    self.right.insert(node)
                else:
                    node.parent = self
                    self.right = node

        def search(self, node):
            if self == node:
                return self
            elif node.l < self.l:
                if self.left is None:
                    return None
                return self.left.search(node)
            else:
                if self.right is None:
                    return None
                return self.right.search(node)

        def is_left(self):
            return self.parent and self.parent.left and self.parent.left == self

        def is_right(self):
            return self.parent and self.parent.right and self.parent.right == self

        def find_max(self):
            return self if self.right is None else self.right.find_max()

        def find_predecessor(self):
            return None if self.left is None else self.left.find_max()

        def swap(self, node):
            np, nl, nr = node.parent, node.left, node.right
            n_is_left = node.is_left()
            n_is_right = node.is_right()
            sp, sl, sr = self.parent, self.left, self.right
            s_is_left = self.is_left()
            s_is_right = self.is_right()

            if s_is_left:
                sp.left = node
            elif s_is_right:
                sp.right = node
            node.parent = sp
            node.left = sl
            node.right = sr
            node.max_r = node.r
            if node.left and node.left.r > node.max_r:
                node.max_r = node.left.r
            if node.right and node.right.r > node.max_r:
                node.max_r = node.right.r

            if n_is_left:
                np.left = self
            elif n_is_right:
                np.right = self
            self.paretn = np
            self.left = nl
            self.right = nr
            if self.left and self.left.r > self.max_r:
                self.max_r = self.left.r
            if self.right and self.right.r > self.max_r:
                self.max_r = self.right.r

        def remove(self, node=None):
            print(self)
            if not node or self == node:
                if not self.left:
                    if self.parent:
                        self.parent.max_r = self.parent.r
                    if self.right:
                        self.right.parent = self.parent
                        if self.parent:
                            self.parent.max_r = max(self.parent.max_r, self.right.r)
                    if self.is_left():
                        self.parent.left = self.right
                    elif self.is_right():
                        self.parent.right = self.right
                    new_root = self.right
                    del self
                    return new_root
                else:
                    pred = self.find_predecessor()
                    print('pred: ', pred)
                    if pred:
                        self.swap(pred)
                        self.remove()
                    return pred
            else:
                self.search(node).remove()
                return self


    def __init__(self):
        self.root = None

    def insert(self, interval: Tuple[Any, Any]):
        node = self.Node(interval)
        if not self.root:
            self.root = node
        else:
            self.root.insert(node)

    def remove(self, interval: Union[Tuple[Any, Any], Interval]):
        if isinstance(interval, Interval):
            node = interval
        else:
            node = Interval(*interval)
        self.root = self.root.remove(node)

    def get(self, interval: Tuple[Any, Any]):
        node = Interval(*interval)
        ret = []
        def _rec(root, node):
            if root.overlap(node):
                ret.append(root)
            if root.left and root.left.max_r >= node.l:
                _rec(root.left, node)
            if root.right:
                _rec(root.right, node)
        _rec(self.root, node)
        return ret


class TestInterval(object):
    @pytest.mark.parametrize('intervals, expected', [
        ([[1,2], [2,3]], False),
        ([[1,3], [2,3]], True),
        ([[1,3], [4,5]], False),
        ([[1,10], [2,3]], True),
    ])
    def test_overlap(self, intervals, expected):
        int1 = Interval(*intervals[0])
        int2 = Interval(*intervals[1])
        assert expected == int1.overlap(int2) == int2.overlap(int1)

    @pytest.mark.parametrize('intervals, expected', [
        ([[1,2], [2,3]], False),
        ([[1,3], [2,3]], False),
        ([[1,3], [4,5]], False),
        ([[1,10], [2,3]], False),
        ([[1,2], [1,2]], True),
        ([[0,13], [0,13]], True),
    ])
    def test_eq(self, intervals, expected):
        int1 = Interval(*intervals[0])
        int2 = Interval(*intervals[1])
        assert expected == (int1 == int2)


class TestIntervalTree(object):
    def setup_method(self, method):
        self.tree = IntervalTree()
        self.intervals = [Interval(15, 20), Interval(10, 30),
                     Interval(12, 15), Interval(17, 19),
                     Interval(5, 20), Interval(30, 40)]
        for i in self.intervals:
            self.tree.insert(i)

    def test_insert(self):
        tree = self.tree
        assert self.intervals[0] == tree.root
        assert self.intervals[1] == tree.root.left
        assert self.intervals[2] == tree.root.left.right
        assert self.intervals[3] == tree.root.right
        assert self.intervals[4] == tree.root.left.left
        assert self.intervals[5] == tree.root.right.right
        assert 40 == tree.root.max_r
        assert 30 == tree.root.left.max_r
        assert 15 == tree.root.left.right.max_r
        assert 40 == tree.root.right.max_r
        assert 20 == tree.root.left.left.max_r
        assert 40 == tree.root.right.right.max_r

    @pytest.mark.parametrize('interval, count', [
        ([1, 2], 0),
        ([1, 100], 6),
        ([30, 40], 2),
        ([40, 41], 1),
        ([4, 5], 1),
        ([13, 18], 5),
        ([16, 16], 3),
    ])
    def test_get(self, interval, count):
        overlaps = self.tree.get(interval)
        print()
        pprint(overlaps)
        assert count == len(overlaps)

    @pytest.mark.parametrize('interval, parent', [
        ([15, 20], None),
        ([10, 30], Interval(15, 20)),
        ([5, 20], Interval(10, 30)),
        ([12, 15], Interval(10, 30)),
        ([17, 19], Interval(15, 20)),
        ([30, 40], Interval(17, 19)),
    ])
    def test_search(self, interval, parent):
        actual = self.tree.root.search(Interval(*interval)).parent
        print()
        pprint(actual)
        assert parent == actual

    def test_swap(self):
        self.tree.root.swap(self.tree.root.search(Interval(12, 15)))
        assert self.tree.root == Interval(12, 15)
        node = self.tree.root.search(Interval(12, 15))
        assert node.parent == None
        assert node.left == Interval(10, 30)
        assert node.right == Interval(17, 19)
        node = self.tree.root.search(Interval(15, 20))
        assert node.parent == Interval(15, 30)
        assert node.left == node.right == None

    def test_remove(self):
        self.tree.remove([15, 20])
        assert self.tree.root == Interval(*[12, 15])
        self.tree.remove([10, 30])
        assert self.tree.root.left == Interval(*[5, 20])


