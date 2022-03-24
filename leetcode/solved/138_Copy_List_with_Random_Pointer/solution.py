#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

	val: an integer representing Node.val
	random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

Example 1:

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Constraints:

	0 <= n <= 1000
	-104 <= Node.val <= 104
	Node.random is null or is pointing to some node in the linked list.
"""
import sys
from typing import Optional
import pytest


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        """07/24/2018 04:59"""
        memo = dict()
        lst = []
        n = head
        while n:
            node = Node(n.label)
            node.random = id(n.random) if n.random else None
            memo[id(n)] = node
            lst.append(node)
            n = n.next
        for i in range(0, len(lst)-1):
            n = lst[i]
            if n.random:
                n.random = memo[n.random]
            n.next = lst[i+1]
        if lst:
            n = lst[-1]
            if n.random:
                n.random = memo[n.random]
        if lst:
            return lst[0]
        else:
            return None

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cache = {}
        dummy = Node(-1)

        # copy list
        cur = dummy
        n = head
        while n:
            cur.next = cache[id(n)] = Node(n.val)
            n = n.next
            cur = cur.next

        # connect random
        cur = dummy.next
        n = head
        while n:
            cur.random = cache.get(id(n.random))
            n = n.next
            cur = cur.next

        return dummy.next


def deserialize(value_indexes):
    if not value_indexes:
        return None
    nodes = []
    for v, _ in value_indexes:
        node = Node(v)
        if nodes:
            nodes[-1].next = node
        nodes.append(node)
    for i in range(len(nodes)):
        j = value_indexes[i][1]
        nodes[i].random = None if j is None else nodes[j]
    return nodes[0]


def serialize(head: Optional[Node]):
    m = {}
    n = head
    i = 0
    while n:
        m[id(n)] = i
        n = n.next
        i += 1
    ret = []
    n = head
    while n:
        ret.append([n.val, m.get(id(n.random))])
        n = n.next
    return ret


@pytest.mark.parametrize('values, expected', [
    ([[7,None],[13,0],[11,4],[10,2],[1,0]], [[7,None],[13,0],[11,4],[10,2],[1,0]]),
    ([[1,1],[2,1]], [[1,1],[2,1]]),
    ([[3,None],[3,0],[3,None]], [[3,None],[3,0],[3,None]]),
])
def test(values, expected):
    # assert serialize(deserialize(values)) == values
    # assert serialize(deserialize(expected)) == expected
    assert expected == serialize(Solution().copyRandomList(deserialize(values)))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
