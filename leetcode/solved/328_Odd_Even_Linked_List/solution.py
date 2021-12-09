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

	n == number of nodes in the linked list
	0 <= n <= 104
	-106 <= Node.val <= 106
"""
import sys
from typing import Optional
import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if other is None:
            return False
        return self.val == other.val and self.next == other.next

    def __repr__(self):
        ret = f'({self.val})'
        if self.next:
            ret += f' - {self.next}'
        return ret


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


def build_list(values):
    if not values: return None
    head = ListNode(values[0])
    tail = head
    for i in range(1, len(values)):
        node = ListNode(values[i])
        tail.next = node
        tail = node
    return head


@pytest.mark.parametrize('values, expected', [
    ([1,2,3,4,5], [1,3,5,2,4]),
    ([2,1,3,5,6,4,7], [2,3,6,7,1,5,4]),
])
def test(values, expected):
    expected = build_list(expected)
    actual = Solution().oddEvenList(build_list(values))
    assert expected == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
