from typing import Optional

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:

Input: head = []
Output: []

Example 3:

Input: head = [1]
Output: [1]

Constraints:

	The number of nodes in the list is in the range [0, 100].
	0 <= Node.val <= 100
"""
import pytest
import sys
sys.path.append('../')
from exercise.list import ListNode, build_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Feb 28, 2022 12:18"""
        if not head:
            return
        if not head.next:
            return head
        nodes = [head, head.next]
        nodes[0].next = self.swapPairs(nodes[1].next)
        nodes[1].next = nodes[0]
        return nodes[1]

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Sep 22, 2023 15:48"""
        if not head:
            return head

        def swap(p, n, nn):
            p.next, n.next, nn.next = nn, nn.next, n

        dummy = ListNode()
        dummy.next = head
        p = dummy
        n = head
        while n and n.next:
            swap(p, n, n.next)
            p, n = n, n.next
        return dummy.next


@pytest.mark.parametrize('args', [
    (([1,2,3,4], [2,1,4,3])),
    (([], [])),
    (([1], [1])),
])
def test(args):
    assert build_list(args[-1]) == Solution().swapPairs(build_list(args[0]))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
