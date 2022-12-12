#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Constraints:

	The number of nodes in the linked list is in the range [0, 104].
	-106 <= Node.val <= 106
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
    def oddEvenList(self, head: ListNode) -> ListNode:
        """04/06/2020 23:13"""
        if not head or not head.next or not head.next.next:
            return head
        even, odd = head, head.next
        even_tail, odd_tail = even, odd
        i = 2
        node = head.next.next
        while node:
            if i % 2 == 0:
                even_tail.next = node
                even_tail = node
            else:
                odd_tail.next = node
                odd_tail = node
            i += 1
            node = node.next
        even_tail.next = odd
        odd_tail.next = None
        return even

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Dec 09, 2021 10:13"""
        heads = [ListNode(), ListNode()]
        tails = heads[:]
        i = 0
        while head:
            tails[i%2].next = head
            tails[i%2] = tails[i%2].next
            head = head.next
            i += 1
        tails[0].next = heads[1].next
        tails[1].next = None
        return heads[0].next

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Dec 11, 2022 16:08"""
        even = ListNode()
        odd = ListNode()
        pointers = [even, odd]
        i = 0
        while head:
            pointers[i%2].next = pointers[i%2] = head
            head = head.next
            i = i+1
        pointers[0].next = odd.next
        pointers[1].next = None
        return even.next

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Feb 18, 2023 19:23"""
        eohead = [ListNode(), ListNode()]
        eotail = eohead[:]
        i = 0
        node = head
        while node:
            i += 1
            eotail[i%2].next = node
            eotail[i%2] = node
            node = node.next
        eotail[0].next = None
        eotail[1].next = eohead[0].next
        return eohead[1].next


@pytest.mark.parametrize('values, expected', [
    ([1,2,3,4,5], [1,3,5,2,4]),
    ([2,1,3,5,6,4,7], [2,3,6,7,1,5,4]),
])
def test(values, expected):
    assert build_list(expected) == Solution().oddEvenList(build_list(values))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
