#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:

	The number of nodes in the list is in the range [1, 5 * 104].
	1 <= Node.val <= 1000
"""
from collections import deque
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
    def reorderList(self, head):
        """07/26/2018 05:12"""
        if not head or not head.next or not head.next.next:
            return
        cur = head
        lst = []
        while cur:
            lst.append(cur)
            cur = cur.next
        i = 0
        j = -i if i < 0 else -(i+1)
        while lst[i] != lst[j]:
            lst[i].next = lst[j]
            i = j
            j = -i if i < 0 else -(i+1)
        lst[i].next = None

    def reorderList(self, head):
        """07/26/2018 05:45"""
        if not head or not head.next or not head.next.next:
            return

        def get_mid(head):
            slow = fast = head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            ret = slow.next
            slow.next = None
            return ret

        def reverse(head):
            prev, cur = None, head
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev

        def merge(a, b):
            while b:
                an, bn = a.next, b.next
                a.next = b
                b.next = an
                a, b = an, bn

        mid = get_mid(head)
        left = head
        right = reverse(mid)
        merge(left, right)

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()
        while head:
            q.append(head)
            head = head.next

        dummy = ListNode()
        tail = dummy
        while q:
            tail.next = q.popleft()
            tail = tail.next
            if q:
                tail.next = q.pop()
                tail = tail.next
        tail.next = None


@pytest.mark.parametrize('values, expected', [
    ([1,2,3,4], [1,4,2,3]),
    ([1,2,3,4,5], [1,5,2,4,3]),
])
def test(values, expected):
    head = build_list(values)
    Solution().reorderList(head)
    assert build_list(expected) == head


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
