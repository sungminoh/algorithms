#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:

Input: head = [], val = 1
Output: []

Example 3:

Input: head = [7,7,7,7], val = 7
Output: []

Constraints:

	The number of nodes in the list is in the range [0, 104].
	1 <= Node.val <= 50
	0 <= val <= 50
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
        return other is not None and self.val == other.val and self.next == other.next

    def __repr__(self):
        return f'{self.val} -> {self.next}'


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        if head.val == val:
            return self.removeElements(head.next, val)

        parent, node = head, head.next
        while node:
            if node.val == val:
                parent.next = node.next
                node = node.next
            else:
                parent, node = node, node.next

        return head


def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    node = head
    for v in values[1:]:
        node.next = ListNode(v)
        node = node.next
    return head


@pytest.mark.parametrize('values, val, expected', [
    ([1,2,6,3,4,5,6], 6, [1,2,3,4,5]),
    ([], 1, []),
    ([7,7,7,7], 7, []),
    ([1,2,2,1], 2, [1,1]),
])
def test(values, val, expected):
    assert build_list(expected) == Solution().removeElements(build_list(values), val)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
