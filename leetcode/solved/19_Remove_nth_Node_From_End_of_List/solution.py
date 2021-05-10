#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

	The number of nodes in the list is sz.
	1 <= sz <= 30
	0 <= Node.val <= 100
	1 <= n <= sz
"""
import sys
import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        ret = f'{self.val}'
        if self.next:
            ret += f' -> {self.next}'
        return ret

    def __eq__(self, other):
        if other.val != self.val:
            return False
        return self.next == other.next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        One pass using two pointers
        Time complexity: O(n)
        Space complexity: O(1)
        """
        node = head
        while n and node:
            node = node.next
            n -= 1
        if n:
            return head
        pp = None
        p = head
        while node:
            node = node.next
            pp = p
            p = p.next
        if not pp:
            return p.next
        pp.next = p.next
        return head


def build_node(values):
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    return nodes[0] if nodes else None


@pytest.mark.parametrize('values, n, expected', [
    ([1,2,3,4,5], 2, [1,2,3,5]),
    ([1], 1, []),
    ([1,2], 1, [1]),
])
def test(values, n, expected):
    node = build_node(values)
    expected = build_node(expected)
    assert expected == Solution().removeNthFromEnd(node, n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
