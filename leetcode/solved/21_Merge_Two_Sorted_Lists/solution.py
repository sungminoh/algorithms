#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

	The number of nodes in both lists is in the range [0, 50].
	-100 <= Node.val <= 100
	Both list1 and list2 are sorted in non-decreasing order.
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        while list1 or list2:
            if not list2 or (list1 is not None and list1.val < list2.val):
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        return dummy.next


@pytest.mark.parametrize('values1, values2, expected', [
    ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
    ([], [], []),
    ([], [0], [0]),
])
def test(values1, values2, expected):
    assert build_list(expected) == Solution().mergeTwoLists(build_list(values1), build_list(values2))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
