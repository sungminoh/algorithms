#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:

Input: head = []
Output: []

Constraints:

	The number of nodes in the list is in the range [0, 5 * 104].
	-105 <= Node.val <= 105

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
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
    def sortList(self, head):
        """07/27/2018 18:33"""
        def get_mid(head):
            slow = fast = head
            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge(a, b):
            dummy = ListNode(None)
            cur = dummy
            while a or b:
                if not b or (a and a.val < b.val):
                    cur.next = a
                    a = a.next
                else:
                    cur.next = b
                    b = b.next
                cur = cur.next
            return dummy.next

        if not head or not head.next:
            return head
        mid = get_mid(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        return merge(left, right)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def split(head):
            slow = head
            fast = slow.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            tail = slow.next
            slow.next = None
            return head, tail

        def merge_sort(head):
            if head is None or head.next is None:
                return head
            a, b = split(head)
            a = merge_sort(a)
            b = merge_sort(b)
            i, j = a, b
            dummy = ListNode()
            cur = dummy
            while i or j:
                if not i:
                    cur.next = j
                    j = j.next
                elif not j:
                    cur.next = i
                    i = i.next
                elif i.val <= j.val:
                    cur.next = i
                    i = i.next
                else:
                    cur.next = j
                    j = j.next
                cur = cur.next
            return dummy.next

        return merge_sort(head)


@pytest.mark.parametrize('values, expected', [
    ([4,2,1,3], [1,2,3,4]),
    ([-1,5,3,4,0], [-1,0,3,4,5]),
    ([], []),
])
def test(values, expected):
    print()
    assert build_list(expected) == Solution().sortList(build_list(values))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
