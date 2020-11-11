
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:

After flattening the multilevel linked list it becomes:

Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL

Example 3:

Input: head = []
Output: []

How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]

To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]

Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]

Constraints:

	Number of Nodes will not exceed 1000.
	1
"""
import sys
from typing import Any
from typing import List
import pytest


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __str__(self):
        s = f'{self.val} - {self.next}'
        if self.child is not None:
            s += f'\n{self.child}'
        return s



class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def inorder(cur, tail):
            tail.next = cur
            if not cur:
                return tail
            cur.prev = tail
            nxt = cur.next
            tail = inorder(cur.child, cur)
            cur.child = None
            return inorder(nxt, tail)
        dummy = Node(None, None, None, None)
        inorder(head, dummy)
        root = dummy.next
        if root:
            root.prev = None
        return root


def deserialize_list(lst: List[Any]):
    def deserialize(lsts: List[List[Any]]):
        if not lsts[0]:
            return None
        if len(lsts) > 1 and lsts[1][0] is not None:
            root = deserialize([lsts[0]])
            root.child = deserialize(lsts[1:])
            return root
        else:
            first = lsts[0]
            e = first.pop(0)
            if e is None:
                return None
            root = Node(e, None, None, None)
            if len(lsts) > 1:
                lsts[1].pop(0)
            root.next = deserialize(lsts)
            return root

    lsts = []
    l = []
    for i, e in enumerate(lst):
        l.append(e)
        if e is None and lst[i - 1] is not None:
            lsts.append(l)
            l = []
    if l:
        lsts.append(l)
    return deserialize(lsts)



def compare(h1, h2):
    if h1 is None and h2 is None:
        return True
    print('compare')
    print(h1)
    print(h2)
    return h1.val == h2.val and compare(h1.next, h2.next) and compare(h1.child, h2.child)

@pytest.mark.parametrize('lsts, expected', [
    ([1,2,3,4,5,6,None,None,None,7,8,9,10,None,None,11,12,None], [1,2,3,7,8,11,12,9,10,4,5,6]),
    ([1,2,3,4,5,6,None,None,None,7,8,9,10,None,None,11,12], [1,2,3,7,8,11,12,9,10,4,5,6]),
])
def test(lsts, expected):
    head = Solution().flatten(deserialize_list(lsts))
    actual = []
    node = head
    while node:
        actual.append(node.val)
        node = node.next
    assert expected, actual

    _head = Solution()._flatten(deserialize_list(lsts))
    assert compare(head, _head)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
