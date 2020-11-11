#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
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


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def main():
    cache = None
    # commands = input().split()
    # args = []
    # for c in commands:
        # args.append([int(x) for x in input().split()])

    commands = ['LRUCache', 'put', 'put', 'get', 'put', 'get', 'put', 'get', 'get', 'get']
    args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    commands = ["LRUCache","put","get"]
    args = [[1],[2,1],[2]]
    commands = ["LRUCache","put","get","put","get","get"]
    args = [[1],[2,1],[2],[3,2],[2],[3]]
    for i, c in enumerate(commands):
        arg = args[i]
        print(f'{c}({arg})', end=' ')
        if c == 'LRUCache':
            cache = LRUCache(*arg)
            print()
        elif c == 'put':
            cache.put(*arg)
            print()
        elif c == 'get':
            print(cache.get(*arg))


if __name__ == '__main__':
    main()
