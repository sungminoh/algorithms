#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

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

Follow up: Could you do this in one pass?
"""
from typing import Optional
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

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """10/16/2022 16:33"""
        def length(node: ListNode):
            l = 0
            while node:
                l += 1
                node = node.next
            return l

        l = length(head)
        dummy = ListNode()
        dummy.next = head
        p = dummy
        c = head
        for _ in range(l-n):
            p = c
            c = c.next
        p.next = c.next
        return dummy.next


@pytest.mark.parametrize('values, n, expected', [
    ([1,2,3,4,5], 2, [1,2,3,5]),
    ([1], 1, []),
    ([1,2], 1, [1]),
])
def test(values, n, expected):
    assert build_list(expected) == Solution().removeNthFromEnd(build_list(values), n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
