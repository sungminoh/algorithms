#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

Example 3:

Input: head = []
Output: []
Explanation: There could be empty list in the input.

Constraints:

	The number of Nodes will not exceed 1000.
	1 <= Node.val <= 105

How the multilevel linked list is represented in test cases:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]

To serialize all levels together, we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,    2,    3, 4, 5, 6, null]
             |
[null, null, 7,    8, 9, 10, null]
                   |
[            null, 11, 12, null]

Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
"""
import itertools
import sys
import pytest


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __str__(self):
        lines = [f'{self.val:>3}']
        if self.child:
            lines.extend(str(self.child).split('\n'))
        max_width = len(max(lines, key=len))
        ret = []
        for a, b in itertools.zip_longest(lines, str(self.next).split('\n')):
            a = a or ''
            b = b or ''
            ret.append(f'{a:<{max_width}} {b}')
        return '\n'.join(ret)

    def __eq__(self, other):
        if not other:
            return False
        return self.val == other.val and self.child == self.child and self.next == other.next


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        """04/29/2020 23:53"""
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

    def flatten(self, head: 'Node') -> 'Node':
        def flatten_head_tail(head: 'Node'):
            if not head:
                return None, None

            prev_node = None
            node = head
            next_node = node.next
            while node:
                child_head, child_tail = flatten_head_tail(node.child)
                node.child = None
                if child_head:
                    node.next = child_head
                    child_head.prev= node
                    child_tail.next = next_node
                    if next_node:
                        next_node.prev = child_tail
                prev_node = child_tail or node
                node = next_node
                if next_node:
                    next_node = next_node.next

            return head, prev_node

        return flatten_head_tail(head)[0]


def build_list(values):
    def build_from(i):
        if i == len(values):
            return None

        nodes = []
        while i < len(values):
            if values[i] is not None:
                nodes.append(Node(values[i], None, None, None))
                i += 1
            else:
                i += 1
                break
        _i = i
        while i < len(values) and values[i] is None:
            i += 1
        parent = nodes[i - _i]
        parent.child = build_from(i)

        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
            nodes[i+1].prev = nodes[i]

        return nodes[0]

    return build_from(0)


@pytest.mark.parametrize('nodes, expected', [
    ([1,2,3,4,5,6,None,None,None,7,8,9,10,None,None,11,12], [1,2,3,7,8,11,12,9,10,4,5,6]),
    ([1,2,None,3], [1,3,2]),
    ([], []),
    ([1,None,2,None,3,None], [1,2,3])
])
def test(nodes, expected):
    head = build_list(nodes)
    print('head')
    print(head)
    expected = build_list(expected)
    print('expected')
    print(expected)
    actual = Solution().flatten(head)
    print('actual')
    print(actual)
    assert expected == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
