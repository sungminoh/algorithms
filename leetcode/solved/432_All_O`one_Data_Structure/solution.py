#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key  with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".

Challenge: Perform all these in O(1) time complexity.
"""
import pytest


class AllOne:
    class Node:
        def __init__(self, *val, cnt=1, left=None, right=None):
            self.val = set(val)
            self.cnt = cnt
            self.left = left
            self.right = right

        def __repr__(self):
            return '%r\n -> %r' % (self.val, self.right)

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dct = {}
        self.head = self.tail = None

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.dct:
            if self.head is None:
                self.head = self.tail = self.Node(key)
            elif self.head.cnt == 1:
                self.head.val.add(key)
            else:
                new_head = self.Node(key)
                new_head.right = self.head
                self.head.left = new_head
                self.head = new_head
            self.dct[key] = self.head
        else:
            node = self.dct[key]
            node.val.remove(key)
            if node.right and node.right.cnt == node.cnt + 1:
                node.right.val.add(key)
                self.dct[key] = node.right
            else:
                new_node = self.Node(key, cnt=node.cnt+1, left=node, right=node.right)
                self.dct[key] = new_node
                if node.right:
                    node.right.left = new_node
                else:
                    self.tail = new_node
                node.right = new_node
            if len(node.val) == 0:
                if node.left is None:
                    self.head = node.right
                else:
                    node.left.right = node.right
                node.right.left = node.left

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.dct:
            return
        node = self.dct[key]
        node.val.remove(key)
        if node.cnt == 1:
            self.dct.pop(key)
        elif node.left and node.left.cnt == node.cnt - 1:
            node.left.val.add(key)
            self.dct[key] = node.left
        else:
            new_node = self.Node(key, cnt=node.cnt-1, left=node.left, right=node)
            self.dct[key] = new_node
            if node.left:
                node.left.right = new_node
            else:
                self.head = new_node
            node.left = new_node
        if len(node.val) == 0:
            if node.right is None:
                self.tail = node.left
            else:
                node.right.left = node.left
            if node.left is None:
                self.head = node.right
            else:
                node.left.right = node.right

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return next(iter(self.tail.val)) if self.tail else ""

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return next(iter(self.head.val)) if self.head else ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()


@pytest.mark.parametrize('', [
])
def test():
    pass
