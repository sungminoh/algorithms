#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

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


@pytest.mark.parametrize('args', [
    ((["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"],
      [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]],
      [None, None, None, 1, None, -1, 3, None, -1, 3, 4])),
    ((["LFUCache","put","get","put","get","get"],
      [[1],[2,1],[2],[3,2],[2],[3]],
      [None,None,1,None,-1,2])),
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
