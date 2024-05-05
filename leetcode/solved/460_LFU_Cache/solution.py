#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

from pathlib import Path

"""
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

	LFUCache(int capacity) Initializes the object with the capacity of the data structure.
	int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
	void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.

To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3

Constraints:

	1 <= capacity <= 104
	0 <= key <= 105
	0 <= value <= 109
	At most 2 * 105 calls will be made to get and put.
"""
import json
from collections import defaultdict
from typing import Any
from typing import List
from typing import Dict
import pytest
import sys


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
    """Oct 24, 2020 22:05"""
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


class LFUCache:
    """Mar 15, 2023 23:59"""
    class Node:
        def __init__(self, k, v, cnt=0, parent=None, left=None, right=None):
            self.k = k
            self.v = v
            self.cnt = cnt
            self.parent = parent
            self.left = left
            self.right = right

        def __repr__(self):
            n = self
            values = []
            while n:
                values.append(n.v)
                n = n.right
            return str(values)

    def _create_freq_node(self, freq):
        n = self.Node(None, None, freq)
        f = self.Node(n, n, freq)
        n.parent = f
        return f

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.tail = self._create_freq_node(-float('inf'))
        self.dct = {}

    def get(self, key: int) -> int:
        node = self._get(key)
        return node.v if node else -1

    @classmethod
    def _pop(cls, node):
        node.right.left = node.left
        if node.left:
            node.left.right = node.right
        if node.parent and node.left is None:
            node.parent.v = node.right
        ret = node.parent
        node.right = node.left = node.parent = None
        return ret

    def _get(self, key: int) -> Node:
        if key not in self.dct:
            return None
        node = self.dct[key]
        node.cnt += 1
        freq = self._pop(node)
        if freq.left and freq.left.cnt == node.cnt:
            node.parent = freq.left
            self._insert_a_before_b(node, freq.left.v)
        else:
            f = self._create_freq_node(node.cnt)
            node.parent = f
            self._insert_a_before_b(f, freq)
            self._insert_a_before_b(node, f.v)
        if freq.v.v is None:
            self._pop(freq)
        return node

    def _insert_a_before_b(self, a, b):
        a.left = b.left
        a.right = b
        a.parent = b.parent
        if b.left:
            b.left.right = a
        b.left = a
        if b.parent and not a.left:
            b.parent.v = a

    def put(self, key: int, value: int) -> None:
        if key in self.dct:
            self._get(key).v = value
            return
        if len(self.dct) == self.capacity:
            if self.tail.left:
                self.dct.pop(self.tail.left.k.left.k)
                f = self._pop(self.tail.left.k.left)
                if f.v.v is None:
                    self._pop(f)

        n = self.Node(key, value, 1)
        self.dct[key] = n
        if self.tail.left and self.tail.left.cnt == 1:
            n.parent = self.tail.left
            self._insert_a_before_b(n, self.tail.left.v)
        else:
            f = self._create_freq_node(1)
            n.parent = f
            self._insert_a_before_b(n, f.v)
            self._insert_a_before_b(f, self.tail)

    def __repr__(self):
        lines = []
        n = self.tail
        while n:
            lines.append(str((n.cnt, str(n.v))))
            n = n.left
        return '\n'.join(reversed(lines))


class LFUCache:
    """TLE"""
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack: List[Any] = []
        self.freq: Dict[Any, int] = defaultdict(int)
        self.keyidx: Dict[Any, int] = {}
        self.idxkey: Dict[int, Any] = {}

    def __swap(self, i, j):
        ki, kj = self.idxkey[i], self.idxkey[j]
        vi, vj = self.stack[i], self.stack[j]
        self.keyidx[ki], self.keyidx[kj] = j, i
        self.idxkey[i], self.idxkey[j] = kj, ki
        self.stack[i], self.stack[j] = vj, vi

    def get(self, key: int) -> int:
        if key not in self.keyidx:
            return -1
        self.freq[key] += 1
        i = self.keyidx[key]
        v = self.stack[i]
        while i > 0 and self.freq[self.idxkey[i]] >= self.freq[self.idxkey[i-1]]:
            self.__swap(i, i-1)
            i = i-1
        return v

    def put(self, key: int, value: int) -> None:
        if key not in self.keyidx:
            if len(self.stack) == self.capacity:
                self.stack.pop()
                k = self.idxkey.pop(len(self.stack))
                self.keyidx.pop(k)
                self.freq.pop(k)
            idx = len(self.stack)
            self.keyidx[key] = idx
            self.idxkey[idx] = key
            self.stack.append(None)
        self.freq[key] += 1
        i = self.keyidx[key]
        self.stack[i] = value
        while i > 0 and self.freq[self.idxkey[i]] >= self.freq[self.idxkey[i-1]]:
            self.__swap(i, i-1)
            i = i-1


class LFUCache:
    """Apr 29, 2024 22:04"""
    class Node:
        def __init__(self, k, v):
            self.k = k
            self.v = v
            self.freq = 1
            self.prv = self.nxt = None
            self.left = self.right = None

        def __repr__(self):
            return f'({self.k}:{self.v}, {self.freq})'

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cnt = 0
        self.lists = self.Node(None, None)
        self.key_node = {}
        self.freq_head = {}
        self.freq_tail = {}

    def show(self):
        node = self.lists.nxt
        while node:
            nxt_node = node.nxt
            print(node.freq, end=': ')
            while node:
                print(node, end=' ')
                node = node.right
            print()
            node = nxt_node

    def remove(self, key):
        node = self.key_node.pop(key)
        head = self.freq_head[node.freq]
        tail = self.freq_tail[node.freq]
        if head == tail:
            ret = head.prv
            if node.nxt:
                node.nxt.prv = node.prv
            node.prv.nxt = node.nxt
            self.freq_head.pop(node.freq)
            self.freq_tail.pop(node.freq)
        elif head == node:
            ret = head.right
            head.right.prv, head.right.nxt = head.prv, head.nxt
            if head.nxt:
                head.nxt.prv = head.right
            head.prv.nxt = head.right
            head.right.left = None
            self.freq_head[node.freq] = head.right
        elif tail == node:
            ret = head
            tail.left.right = None
            self.freq_tail[node.freq] = tail.left
        else:
            ret = head
            node.left.right, node.right.left = node.right, node.left
        node.left = node.right = node.prv = node.nxt = None
        return ret

    def insert(self, prv_head, node):
        self.key_node[node.k] = node
        if not prv_head.nxt:
            prv_head.nxt = node
            node.prv = prv_head
            self.freq_tail[node.freq] = self.freq_head[node.freq] = node
        else:
            if prv_head.nxt.freq == node.freq:
                tail = self.freq_tail[node.freq]
                tail.right, node.left = node, tail
                self.freq_tail[node.freq] = node
            else:
                node.prv, node.nxt = prv_head, prv_head.nxt
                prv_head.nxt.prv = prv_head.nxt = node
                self.freq_tail[node.freq] = self.freq_head[node.freq] = node

    def update(self, key):
        n = self.key_node[key]
        h = self.remove(key)
        n.freq += 1
        self.insert(h, n)

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1
        ret = self.key_node[key].v
        self.update(key)
        return ret

    def put(self, key: int, value: int) -> None:
        if key in self.key_node:
            self.key_node[key].v = value
            self.update(key)
        else:
            if len(self.key_node) == self.capacity:
                self.remove(self.lists.nxt.k)
            self.insert(self.lists, self.Node(key, value))


@pytest.mark.parametrize('args', [
    ((["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"],
      [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]],
      [None, None, None, 1, None, -1, 3, None, -1, 3, 4])),
    ((["LFUCache","put","get","put","get","get"],
      [[1],[2,1],[2],[3,2],[2],[3]],
      [None,None,1,None,-1,2])),
    ((["LFUCache","get","put","get","put","put","get","get"],
      [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]],
      [None,-1,None,-1,None,None,2,6])),
    (json.load(open(Path(__file__).parent/'testcase.json'))),
    ((["LFUCache","put","put","put","get","put","put","get","put","put","get","put","get","get","get","put","put","get","put","get"],
      [[10],[7,28],[7,1],[8,15],[6],[10,27],[8,10],[8],[6,29],[1,9],[6],[10,7],[1],[2],[13],[8,30],[1,5],[1],[13,2],[12]],
      [None, None, None, None, -1, None, None, 10, None, None, 29, None, 9, -1, -1, None, None, 5, None, -1])),
    ((["LFUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"],
      [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]],
      [None, None, None, None, None, None, -1, None, 19, 17, None, -1, None, None, None, -1, None, -1, 5, -1, 12, None, None, 3, 5, 5, None, None, 1, None, -1, None, 30, 5, 30, None, None, None, -1, None, -1, 24, None, None, 18, None, None, None, None, 14, None, None, 18, None, None, 11, None, None, None, None, None, 18, None, None, -1, None, 4, 29, 30, None, 12, 11, None, None, None, None, 29, None, None, None, None, 17, -1, 18, None, None, None, -1, None, None, None, 20, None, None, None, 29, 18, 18, None, None, None, None, 20, None, None, None, None, None, None, None])),
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
