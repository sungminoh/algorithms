#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:

Input: head = [2,1], x = 2
Output: [1,2]

Constraints:

	The number of nodes in the list is in the range [0, 200].
	-100 <= Node.val <= 100
	-200 <= x <= 200
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
    def partition(self, head, x):
        """05/01/2018 06:46"""
        less = ListNode(None)
        lp = less
        greater = ListNode(None)
        gp = greater
        while head:
            if head.val < x:
                lp.next = head
                lp = lp.next
            else:
                gp.next = head
                gp = gp.next
            head = head.next
        lp.next = greater.next
        gp.next = None
        return less.next

    def partition(self, head: ListNode, x: int) -> ListNode:
        """04/28/2021 00:43"""
        smaller_head = smaller_tail = ListNode(None)
        larger_head = larger_tail = ListNode(None)
        node = head
        while node:
            if node.val < x:
                smaller_tail.next = node
                smaller_tail = node
            else:
                larger_tail.next = node
                larger_tail = node
            node = node.next
        if not smaller_head.next or not larger_head.next:
            return head

        start = smaller_head.next
        tail = smaller_tail
        tail.next = larger_head.next
        tail = larger_tail
        tail.next = None
        return start

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller = ListNode(None)
        larger = ListNode(None)
        sp = smaller
        lp = larger
        node = head
        while node:
            if node.val < x:
                sp.next = node
                sp = sp.next
            else:
                lp.next = node
                lp = lp.next
            node = node.next
        lp.next = None
        sp.next = larger.next
        return smaller.next


@pytest.mark.parametrize('values, x, expected', [
    ([1,4,3,2,5,2], 3, [1,2,2,4,3,5]),
    ([2,1], 2, [1,2]),
])
def test(values, x, expected):
    assert build_list(expected) == Solution().partition(build_list(values), x)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
