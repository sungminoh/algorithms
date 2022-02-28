#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:

Input: head = []
Output: []

Example 3:

Input: head = [1]
Output: [1]

Constraints:

	The number of nodes in the list is in the range [0, 100].
	0 <= Node.val <= 100
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        nodes = [head, head.next]
        nodes[0].next = self.swapPairs(nodes[1].next)
        nodes[1].next = nodes[0]
        return nodes[1]


@pytest.mark.parametrize('values, expected', [
    ([1,2,3,4], [2,1,4,3]),
    ([], []),
    ([1], [1]),
])
def test(values, expected):
    assert build_list(expected) == Solution().swapPairs(build_list(values))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
