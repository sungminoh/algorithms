#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design a Skiplist without using any built-in libraries.

A skiplist is a data structure that takes O(log(n)) time to add, erase and search. Comparing with treap and red-black tree which has the same function and performance, the code length of Skiplist can be comparatively short and the idea behind Skiplists is just simple linked lists.

For example, we have a Skiplist containing [30,40,50,60,70,90] and we want to add 80 and 45 into it. The Skiplist works this way:

Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons

You can see there are many layers in the Skiplist. Each layer is a sorted linked list. With the help of the top layers, add, erase and search can be faster than O(n). It can be proven that the average time complexity for each operation is O(log(n)) and space complexity is O(n).

See more about Skiplist: https://en.wikipedia.org/wiki/Skip_list

Implement the Skiplist class:

	Skiplist() Initializes the object of the skiplist.
	bool search(int target) Returns true if the integer target exists in the Skiplist or false otherwise.
	void add(int num) Inserts the value num into the SkipList.
	bool erase(int num) Removes the value num from the Skiplist and returns true. If num does not exist in the Skiplist, do nothing and return false. If there exist multiple num values, removing any one of them is fine.

Note that duplicates may exist in the Skiplist, your code needs to handle this situation.

Example 1:

Input
["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
[[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]
Output
[null, null, null, null, false, null, true, false, true, false]

Explanation
Skiplist skiplist = new Skiplist();
skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0); // return False
skiplist.add(4);
skiplist.search(1); // return True
skiplist.erase(0);  // return False, 0 is not in skiplist.
skiplist.erase(1);  // return True
skiplist.search(1); // return False, 1 has already been erased.

Constraints:

	0 <= num, target <= 2 * 104
	At most 5 * 104 calls will be made to search, add, and erase.
"""
from collections import deque
import random
import pytest
import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.up = None
        self.down = None

    def __repr__(self):
        return str(self.value)


class Skiplist:
    """May 05, 2024 11:16"""
    def __init__(self):
        self.head = Node(-float('inf'))

    def __repr__(self):
        lines = []
        node = self.head
        while node.down:
            node = node.down
        while node:
            line = []
            n = node
            while n:
                line.append(n.value)
                n = n.up
            node = node.next
            lines.append(' - '.join(map(str, line)))
        return '\n'.join(lines)

    def _iter(self, num):
        parents = []
        parent = None
        node = self.head
        while node:
            while node and node.value < num:
                parent, node = node, node.next
            parents.append(parent)
            node = parent.down
        return parents

    def search(self, target: int) -> bool:
        node = self._iter(target)[-1].next
        return node is not None and node.value == target

    def add(self, num: int) -> None:
        parents = self._iter(num)
        prv = None
        while parents:
            p = parents.pop()
            node = Node(num)
            node.next, node.down = p.next, prv
            if prv: prv.up = node
            p.next = node
            prv = node
            if random.randint(0, 1) == 0:
                break
        if len(parents) == 0 and random.randint(0, 1) == 0:
            head = Node(-float('inf'))
            self.head.up, head.down = head, self.head
            p = self.head = head
            node = Node(num)
            node.next, node.down = p.next, prv
            if prv: prv.up = node
            p.next = node

    def erase(self, num: int) -> bool:
        parents = self._iter(num)
        node = parents[-1].next
        if not (node and node.value == num):
            return False
        while parents:
            p = parents.pop()
            if p.next and p.next.value == num:
                p.next = p.next.next
        return True


@pytest.mark.parametrize('args', [
    ((["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"],
      [[], [1], [2], [3], [0], [4], [1], [0], [1], [1]],
      [None, None, None, None, False, None, True, False, True, False])),
    ((["Skiplist","add","add","add","add","add","add","add","add","add","erase","search","add","erase","erase","erase","add","search","search","search","erase","search","add","add","add","erase","search","add","search","erase","search","search","erase","erase","add","erase","search","erase","erase","search","add","add","erase","erase","erase","add","erase","add","erase","erase","add","add","add","search","search","add","erase","search","add","add","search","add","search","erase","erase","search","search","erase","search","add","erase","search","erase","search","erase","erase","search","search","add","add","add","add","search","search","search","search","search","search","search","search","search"],
      [[],[16],[5],[14],[13],[0],[3],[12],[9],[12],[3],[6],[7],[0],[1],[10],[5],[12],[7],[16],[7],[0],[9],[16],[3],[2],[17],[2],[17],[0],[9],[14],[1],[6],[1],[16],[9],[10],[9],[2],[3],[16],[15],[12],[7],[4],[3],[2],[1],[14],[13],[12],[3],[6],[17],[2],[3],[14],[11],[0],[13],[2],[1],[10],[17],[0],[5],[8],[9],[8],[11],[10],[11],[10],[9],[8],[15],[14],[1],[6],[17],[16],[13],[4],[5],[4],[17],[16],[7],[14],[1]],
      [None,None,None,None,None,None,None,None,None,None,True,False,None,True,False,False,None,True,True,True,True,False,None,None,None,False,False,None,False,False,True,True,False,False,None,True,True,False,True,True,None,None,False,True,False,None,True,None,True,True,None,None,None,False,False,None,True,False,None,None,True,None,False,False,False,True,True,False,True,None,True,False,False,False,True,True,False,False,None,None,None,None,True,True,True,True,True,True,False,False,True])),
])
def test(args):
    commands, arguments, expecteds = args
    obj = globals()[commands[0]](*arguments[0])
    actual = [None]
    for cmd, arg in zip(commands[1:], arguments[1:]):
        # print('-------------------------------------')
        # print(cmd, arg)
        actual.append(getattr(obj, cmd)(*arg))
        # print(actual[-1])
        # print(obj)
    assert expecteds == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
