#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import pytest
from typing import Callable
from typing import Any
from typing import List
from dataclasses import dataclass

class SegmentTree(object):
    @dataclass
    class Node(object):
        v: Any

        def __repr__(self):
            return str(self.v)

    def __init__(self,
                 nums: List[int],
                 func=lambda l, r: sum(l, r)):
        self.func = func
        self.size = len(nums)
        if not nums:
            self.arr = []
            self.depth = -1
            return
        self.depth = 0
        while 2 ** self.depth < len(nums):
            self.depth += 1
        self.arr = [self.Node(None) for _ in range(pow(2, self.depth + 1) - 1)]

        def _rec(root, l, r, i, j):
            if l == r:
                self.arr[root].v = nums[l]
                return
            m = l + ((r - l) // 2)
            v = None
            if i <= m:
                _rec(self.left(root), l, m, i, min(j, m))
                v = self.arr[self.left(root)].v
            if j > m:
                _rec(self.right(root), m + 1, r, m + 1, j)
                if v is None:
                    v = self.arr[self.right(root)].v
                else:
                    v = self.func(v, self.arr[self.right(root)].v)
            self.arr[root].v = v

        _rec(0, 0, pow(2, self.depth) - 1, 0, len(nums) - 1)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2

    def update(self, i: int, val: int) -> None:
        def _rec(root, l, r, i, val):
            if l == r == i:
                self.arr[root].v = val
                return
            m = l + ((r - l) // 2)
            if i <= m:
                _rec(self.left(root), l, m, i, val)
                if m + 1 <= self.size - 1:
                    self.arr[root].v = self.func(self.arr[self.left(root)].v, self.arr[self.right(root)].v)
                else:
                    self.arr[root].v = self.arr[self.left(root)].v
            else:
                _rec(self.right(root), m + 1, r, i, val)
                self.arr[root].v = self.func(self.arr[self.left(root)].v, self.arr[self.right(root)].v)
        _rec(0, 0, pow(2, self.depth) - 1, i, val)

    def query(self, i: int, j: int) -> int:
        def _rec(root, l, r, i, j):
            if l >= i and r <= j:
                return self.arr[root].v
            m = l + ((r - l) // 2)
            if i <= m and j <= m:
                return _rec(self.left(root), l, m, i, j)
            elif m < i and m < j:
                return _rec(self.right(root), m + 1, r, i, j)
            else:
                return self.func(_rec(self.left(root), l, m, i, m),
                                 _rec(self.right(root), m + 1, r, m + 1, j))
        return _rec(0, 0, pow(2, self.depth) - 1, i, j)


class SimpleSegmentTree:
    def __init__(self, vals: List[Any], merge: Callable[[Any, Any], Any]):
        def build(l, r):
            if l == r:
                return [vals[l], None, None]
            m = l + ((r-l)//2)
            left = build(l, m)
            right = build(m+1, r)
            return [merge(left[0], right[0]), left, right]
        self.tree = build(0, len(vals)-1)
        self.size = len(vals)
        self.merge = merge

    def update(self, i: int, val: int) -> None:
        def change_value(l, r, tree):
            if l == r == i:
                tree[0] = val
                return
            m = l + ((r-l)//2)
            if i <= m:
                change_value(l, m, tree[1])
            if i > m:
                change_value(m+1, r, tree[2])
            tree[0] = self.merge(tree[1][0], tree[2][0])

        change_value(0, self.size-1, self.tree)

    def query(self, i, j):
        def find(i, j, l, r, tree):
            if i <= l and r <= j:
                return tree[0]
            m = l + ((r-l)//2)
            if j <= m:
                return find(i, j, l, m, tree[1])
            if i > m:
                return find(i, j, m+1, r, tree[2])
            return self.merge(
                find(i, m, l, m, tree[1]),
                find(m+1, j, m+1, r, tree[2]),
            )

        return find(i, j, 0, self.size-1, self.tree)


def test_init():
    nums = [1,2,3,4,5,6,7,8,9]
    tree = SegmentTree(nums, lambda x, y: x + y)

    def get_node(i):
        return tree.arr[i].v

    assert get_node(0) == sum(range(1, 10))
    assert get_node(1) == sum(range(1, 9))
    assert get_node(2) == 9
    assert get_node(3) == sum(range(1, 5))

    nums = []
    tree = SegmentTree(nums, lambda x, y: x + y)


def test_update():
    nums = [1,2,3,4,5,6,7,8,9]
    tree = SegmentTree(nums, lambda x, y: x + y)
    tree.update(0, 10)

    def get_node(i):
        return tree.arr[i].v

    assert get_node(0) == sum(range(1, 10)) + 9
    assert get_node(1) == sum(range(1, 9)) + 9
    assert get_node(2) == 9
    assert get_node(3) == sum(range(1, 5)) + 9

    tree.update(8, 1)
    assert get_node(0) == sum(range(1, 10)) + 9 - 8
    assert get_node(2) == 1


def test_range():
    nums = [1,2,3,4,5,6,7,8,9]
    tree = SegmentTree(nums, lambda x, y: x + y)

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            assert tree.query(i, j) == sum(nums[i:j + 1])


def test_simple_init():
    nums = [1,2,3,4,5,6,7,8,9]
    tree = SimpleSegmentTree(nums, lambda x, y: x + y)

    assert tree.query(0, 8) == sum(range(1, 10))
    assert tree.query(0, 7) == sum(range(1, 9))
    assert tree.query(8, 8) == 9
    assert tree.query(0, 3) == sum(range(1, 5))

    # nums = []
    # tree = SimpleSegmentTree(nums, lambda x, y: x + y)


def test_simple_update():
    nums = [1,2,3,4,5,6,7,8,9]
    tree = SimpleSegmentTree(nums, lambda x, y: x + y)
    tree.update(0, 10)

    assert tree.query(0, 8) == sum(range(1, 10)) + 9
    assert tree.query(0, 7) == sum(range(1, 9)) + 9
    assert tree.query(8, 8) == 9
    assert tree.query(0, 3) == sum(range(1, 5)) + 9

    tree.update(8, 1)
    assert tree.query(0, 8) == sum(range(1, 10)) + 9 - 8
    assert tree.query(8, 8) == 1


def test_simple_range():
    nums = [1,2,3,4,5,6,7,8,9]
    tree = SimpleSegmentTree(nums, lambda x, y: x + y)

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            assert tree.query(i, j) == sum(nums[i:j + 1])

