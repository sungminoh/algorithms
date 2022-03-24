#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

	The number of nodes in each linked list is in the range [1, 100].
	0 <= Node.val <= 9
	It is guaranteed that the list represents a number that does not have leading zeros.
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
    def addTwoNumbers(self, l1, l2):
        """01/13/2018 01:49"""
        head = ListNode(-1)
        p = head
        s = 0
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            s += (n1 + n2)
            r = s % 10
            s //= 10
            p.next = ListNode(r)
            p = p.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if s:
            p.next = ListNode(s)
        return head.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2:
            v = carry
            if l1:
                v += l1.val
                l1 = l1.next
            if l2:
                v += l2.val
                l2 = l2.next
            carry, v = divmod(v, 10)
            cur.next = ListNode(v)
            cur = cur.next
        if carry:
            cur.next = ListNode(carry)
        return dummy.next


@pytest.mark.parametrize('values1, values2, expected', [
    ([2,4,3], [5,6,4], [7,0,8]),
    ([0], [0], [0]),
    ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1]),
])
def test(values1, values2, expected):
    assert build_list(expected) == Solution().addTwoNumbers(build_list(values1), build_list(values2))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
