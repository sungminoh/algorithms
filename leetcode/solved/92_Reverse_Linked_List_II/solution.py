#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:

	The number of nodes in the list is n.
	1 <= n <= 500
	-500 <= Node.val <= 500
	1 <= left <= right <= n

Follow up: Could you do it in one pass?
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
    def reverseBetween(self, head, m, n):
        """05/06/2018 01:00"""
        if m >= n:
            return head
        parent = None
        p = head
        for _ in range(m-1):
            parent = p
            p = p.next
        t = p
        tmp = p.next
        child = tmp
        for _ in range(n-m):
            child = tmp
            if child:
                tmp = child.next
                child.next = p
                p = child
            else:
                break
        t.next = tmp
        if parent:
            parent.next = p
            return head
        else:
            return child

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """08/08/2021 17:38"""
        pre, cur, pos = None, head, head.next
        p, s, e = None, None, None
        i = 1
        while cur:
            _pre, _cur = cur, cur.next
            _pos = _cur.next if _cur else None
            if s:
                cur.next = pre
            if i == left:
                p = pre
                s = cur
            if i == right:
                s.next = pos
                if p: p.next = cur
                e = cur
                break
            pre, cur, pos = _pre, _cur, _pos
            i += 1
        return head if p or not s else e


    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """07/31/2022 23:12"""
        if not head or left == right:
            return head

        dummy = ListNode(None)
        dummy.next = head
        parent = dummy
        node = head

        i = 1
        left_node = None
        pointer = None
        while node:
            if left_node is None:
                if i == left:
                    left_parent = parent
                    left_node = pointer = node
                    node = node.next
                else:
                    parent, node = node, node.next
            else:
                next_node = node.next
                node.next = pointer
                if i != right:
                    pointer = node
                    node = next_node
                else:
                    parent.next = node
                    left_node.next = next_node
                    break
            i += 1
        return dummy.next


@pytest.mark.parametrize('values, left, right, expected', [
    ([1,2,3,4,5], 2, 4, [1,4,3,2,5]),
    ([5], 1, 1, [5]),
    ([3,5], 1, 2, [5,3]),
    ([3,5], 1, 1, [3,5]),
])
def test(values, left, right, expected):
    assert build_list(expected) == Solution().reverseBetween(build_list(values), left, right)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
