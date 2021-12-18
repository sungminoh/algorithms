#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example 1:

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:

Input: head = [0]
Output: 0

Constraints:

	The Linked List is not empty.
	Number of nodes will not exceed 30.
	Each node's value is either 0 or 1.
"""
import sys
import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ret = 0
        while head:
            ret <<= 1
            ret += head.val
            head = head.next
        return ret


def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    node = head
    for v in values[1:]:
        node.next = ListNode(v)
        node = node.next
    return head


@pytest.mark.parametrize('values, expected', [
    ([1,0,1], 5),
    ([0], 0),
])
def test(values, expected):
    assert expected == Solution().getDecimalValue(build_list(values))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
