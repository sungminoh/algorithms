#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:

	The number of nodes in the list is in the range [0, 300].
	-100 <= Node.val <= 100
	The list is guaranteed to be sorted in ascending order.
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
    def deleteDuplicates(self, head):
        """05/01/2018 06:17"""
        dummy = ListNode(None)
        dummy.next = head
        c = dummy
        while c:
            if not c.next or not c.next.next:
                return dummy.next
            n = c.next
            nn = n.next
            deduped = False
            while nn and n.val == nn.val:
                deduped = True
                nn = nn.next
            if deduped:
                c.next = nn
            else:
                c = c.next
        return dummy.next

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        pre = None
        while head:
            while head.next and head.next.val == head.val:
                pre = head
                head = head.next
            if not pre or pre.val != head.val:
                cur.next = head
                cur = cur.next
            pre = head
            head = head.next
        cur.next = None
        return dummy.next


@pytest.mark.parametrize('values, expected', [
    ([1,2,3,3,4,4,5], [1,2,5]),
    ([1,1,1,2,3], [2,3]),
    ([1,2,2], [1]),
])
def test(values, expected):
    assert build_list(expected) == Solution().deleteDuplicates(build_list(values))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
