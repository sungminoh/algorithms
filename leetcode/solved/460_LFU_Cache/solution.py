#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design and implement a data structure for Least Frequently Used (LFU) cache.

Implement the LFUCache class:

	LFUCache(int capacity) Initializes the object with the capacity of the data structure.
	int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
	void put(int key, int value) Sets or inserts the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be evicted.

Notice that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.

Follow up:
Could you do both operations in O(1) time complexity?

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
LFUCache lFUCache = new LFUCache(2);
lFUCache.put(1, 1);
lFUCache.put(2, 2);
lFUCache.get(1);      // return 1
lFUCache.put(3, 3);   // evicts key 2
lFUCache.get(2);      // return -1 (not found)
lFUCache.get(3);      // return 3
lFUCache.put(4, 4);   // evicts key 1.
lFUCache.get(1);      // return -1 (not found)
lFUCache.get(3);      // return 3
lFUCache.get(4);      // return 4

Constraints:

	0 <= capacity, key, value <= 104
	At most 105 calls will be made to get and put.
"""
import sys
import pytest


class Node:
    def __init__(self, val, cnt=1, key=None, left=None, right=None):
        self.val = val
        self.cnt = cnt
        self.key = key
        self.left = left
        self.right = right

    def remove(self):
        self.left.right = self.right
        self.right.left = self.left
        self.left = self.right = None
        return self

    def append_right(self, node: 'Node'):
        self.right.left = node
        node.right = self.right
        self.right = node
        node.left = self

    def append_left(self, node: 'Node'):
        self.left.right = node
        node.left = self.left
        self.left = node
        node.right = self


class LinkedList:
    def __init__(self):
        self._head = Node('head', cnt=0)
        self._tail = Node('tail', cnt=0)
        self._head.right = self._tail
        self._tail.left = self._head
        self.size = 0

    def __len__(self):
        return self.size

    def append_right(self, node):
        self.size += 1
        self._tail.append_left(node)

    def append_left(self, node):
        self.size += 1
        self._head.append_right(node)

    def is_tail(self, node):
        return node.right == self._tail

    def is_head(self, node):
        return self._head.right == node

    def remove(self, node):
        self.size -= 1
        return node.remove()

    @property
    def head(self):
        return self._head.right

    @property
    def tail(self):
        return self._tail.left

    def to_list(self):
        ret = []
        node = self.head
        while node and node.val != 'tail':
            ret.append(node.val)
            node = node.right
        return ret


class LFUCache:
    def __init__(self, capacity: int):
        self.cnt = 0
        self.cap = capacity
        self.lst = LinkedList()
        self.dic = {}

    def update(self, n, m):
        n.val.remove(m)
        if n.cnt+1 == n.right.cnt:
            node = n.right
            node.val.append_right(m)
        else:
            l = LinkedList()
            l.append_right(m)
            node = Node(l, cnt=n.cnt + 1)
            n.append_right(node)
        if len(n.val) == 0:
            self.lst.remove(n)
        return node, m

    def evict(self):
        self.cnt -= 1
        least = self.lst.head
        target = least.val.head
        least.val.remove(target)
        if len(least.val) == 0:
            self.lst.remove(least)
        self.dic.pop(target.key)

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        n, m = self.dic[key]
        self.dic[key] = self.update(n, m)
        return m.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.dic:
            n, m = self.dic[key]
            m.val = value
            self.dic[key] = self.update(n, m)
        else:
            if self.cnt == self.cap:
                self.evict()
            self.cnt += 1
            m = Node(value, key=key)
            if self.lst.head.cnt == 1:
                n = self.lst.head
                n.val.append_right(m)
            else:
                l = LinkedList()
                l.append_right(m)
                n = Node(l, cnt=1)
                self.lst.append_left(n)
            self.dic[key] = (n, m)

    def __repr__(self):
        return '\n'.join(map(str, [str(node.to_list()) for node in self.lst.to_list()]))


@pytest.mark.parametrize('commands, args', [
    (["LFUCache","put","put","get","put","get","get","put","get","get","get"], [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]])
])
def test(commands, args):
    print()
    o = LFUCache(*args[0])
    for c, a in zip(commands[1:], args[1:]):
        print(getattr(o, c)(*a))
        print(o)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
