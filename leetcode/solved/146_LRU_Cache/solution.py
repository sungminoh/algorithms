#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

	LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
	int get(int key) Return the value of the key if the key exists, otherwise return -1.
	void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:

	1 <= capacity <= 3000
	0 <= key <= 104
	0 <= value <= 105
	At most 2 * 105 calls will be made to get and put.
"""
from collections import deque
import pytest
import sys


class Node(object):
    def __init__(self, k, v, p=None, n=None):
        self.k = k
        self.v = v
        self.p = p
        self.n = n

    def pop(self, h, t):
        if self == h:
            h = self.n
        if self == t:
            t = self.p
        p = self.p
        n = self.n
        if p:
            self.p.n = self.n
        if n:
            self.n.p = self.p
        self.p = self.n = None
        return self, h, t

    def __repr__(self):
        return 'Node(%s, %s)' % (self.k, self.v)


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.table = dict()
        self.head = self.tail = None

    def print_status(self):
        print('-- table --')
        print(self.table)
        print('-- cache --')
        node = self.head
        while node:
            print(node)
            node = node.n
        print('-- head, tail --')
        print(self.head, self.tail)

    def update_node(self, node):
        if self.count == 1:
            return
        node, self.head, self.tail = node.pop(self.head, self.tail)
        self.tail.n, node.p = node, self.tail
        self.tail = node

    def add_node(self, node):
        if self.count == 0:
            self.head = self.tail = node
        else:
            self.tail.n, node.p = node, self.tail
            self.tail = node
        self.count += 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.table:
            return -1
        elif self.count == 1:
            return self.head.v
        else:
            node = self.table[key]
            self.update_node(node)
            return node.v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.table:
            node = self.table[key]
            node.v = value
            self.update_node(node)
            return
        if self.count == self.capacity:
            oldest = self.head
            # print('evicts', oldest)
            self.table.pop(oldest.k)
            self.head = oldest.n
            del oldest
            self.count -= 1
        node = Node(key, value)
        self.table[key] = node
        self.add_node(node)


class LRUCache:
    """Apr 29, 2024 18:34"""
    class Value:
        def __init__(self, v):
            self.v = v
            self.valid = True

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque([])
        self.d = {}

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        v = self.d[key]
        v.valid = False
        self.d[key] = self.Value(v.v)
        self.queue.append((key, self.d[key]))
        return v.v

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.pop(key).valid = False
        self.d[key] = self.Value(value)
        self.queue.append((key, self.d[key]))
        while len(self.d) > self.capacity:
            k, v = self.queue.popleft()
            if v.valid:
                self.d.pop(k)


@pytest.mark.parametrize('args', [
    ((["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
      [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
      [None, None, None, 1, None, -1, None, -1, 3, 4])),
    ((["LRUCache","put","get"],
      [[1],[2,1],[2]],
      [None, None, 1],
      )),
    ((["LRUCache","put","get","put","get","get"],
      [[1],[2,1],[2],[3,2],[2],[3]],
      [None, None, 1, None, -1, 2]
      )),

])
def test(args):
    commands, arguments, expecteds = args
    obj = globals()[commands.pop(0)](*arguments.pop(0))
    actual = []
    for cmd, arg in zip(commands, arguments):
        actual.append(getattr(obj, cmd)(*arg))
    assert expecteds[1:] == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
