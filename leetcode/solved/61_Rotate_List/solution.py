#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:

	The number of nodes in the list is in the range [0, 500].
	-100 <= Node.val <= 100
	0 <= k <= 2 * 109
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
    def rotateRight(self, head, k):
        """12/26/2017 18:12"""
        if head is None:
            return head
        i = 1
        n = head
        while n.next is not None:
            i += 1
            n = n.next
        n.next = head
        n = head
        for _ in range(i-(k%i)-1):
            n = n.next
        head = n.next
        n.next = None
        return head

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        def make_circle_and_return_size(head: Optional[ListNode]):
            if not head:
                return 0
            ret = 1
            parent = head
            cur = head.next
            while cur:
                ret += 1
                parent = cur
                cur = cur.next
            parent.next = head
            return ret

        l = make_circle_and_return_size(head)
        cur = head
        i = l-(k%l)
        while i:
            nxt = cur.next
            if i == 1:
                cur.next = None
            cur = nxt
            i -= 1
        return cur


@pytest.mark.parametrize('values, k, expected', [
    ([1,2,3,4,5], 2, [4,5,1,2,3]),
    ([0,1,2], 4, [2,0,1]),
])
def test(values, k, expected):
    assert build_list(expected) == Solution().rotateRight(build_list(values), k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))

