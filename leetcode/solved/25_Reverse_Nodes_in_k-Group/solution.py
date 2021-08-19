#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]

Example 4:

Input: head = [1], k = 1
Output: [1]

Constraints:

	The number of nodes in the list is in the range sz.
	1 <= sz <= 5000
	0 <= Node.val <= 1000
	1 <= k <= sz

Follow-up: Can you solve the problem in O(1) extra memory space?
"""
import sys
from typing import Optional
import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'({self.val}) -> {self.next}'

    def __eq__(self, other):
        return False if self.val != other.val else self.next == other.next


class Solution:
    def reverseKGroup(self, head, k):
        """08/04/2018 22:49"""
        def reverse(s, e):
            prev = ListNode(None)
            cur = s
            while prev != e:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return e, s

        if not head or not head.next:
            return head
        ret = h = ListNode(None)
        h.next = head
        s = e = head
        cnt = 1
        while e:
            n = e.next
            if cnt == k:
                s_, e_ = reverse(s, e)
                h.next = s_
                e_.next = n
                h = e_
                s = n
                cnt = 0
            e = n
            cnt += 1
        return ret.next

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        def reverse_node(parent, start, end):
            parent.next = end
            node = start.next
            start.next = end.next
            cnt = k-1
            while cnt > 0:
                tmp = node.next
                node.next = start
                start = node
                node = tmp
                cnt -= 1

        dummy = ListNode()
        dummy.next = head
        i = 1
        parent = dummy
        node = head
        start = node
        while node:
            if i % k == 0:
                reverse_node(parent, start, node)
                parent = start
                node = parent.next
                start = node
            else:
                node = node.next
            i += 1
        return dummy.next


def build_list(nodes):
    list_nodes = [ListNode(v) for v in nodes]
    for i in range(len(list_nodes)-1):
        list_nodes[i].next = list_nodes[i+1]
    return list_nodes[0] if list_nodes else None


@pytest.mark.parametrize('nodes, k, expected', [
    ([1,2,3,4,5], 2, [2,1,4,3,5]),
    ([1,2,3,4,5], 3, [3,2,1,4,5]),
    ([1,2,3,4,5], 1, [1,2,3,4,5]),
    ([1], 1, [1]),
])
def test(nodes, k, expected):
    head = build_list(nodes)
    actual = Solution().reverseKGroup(head, k)
    print()
    print(actual)
    assert build_list(expected) == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
