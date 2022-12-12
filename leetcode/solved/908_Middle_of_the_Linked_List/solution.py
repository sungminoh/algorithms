#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:

	The number of nodes in the list is in the range [1, 100].
	1 <= Node.val <= 100
"""
from typing import Optional
import pytest
import sys
sys.path.append('../')
from exercise.list import build_list, ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Jan 07, 2022 18:37"""
        slow = head
        fast = head.next
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        return slow

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Dec 11, 2022 16:00"""
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Feb 18, 2023 19:15"""
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


@pytest.mark.parametrize('values, expected', [
    ([1,2,3,4,5], [3,4,5]),
    ([1,2,3,4,5,6], [4,5,6]),
])
def test(values, expected):
    assert build_list(expected) == Solution().middleNode(build_list(values))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
