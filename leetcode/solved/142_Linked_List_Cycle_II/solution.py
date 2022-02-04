#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Constraints:

	The number of the nodes in the list is in the range [0, 104].
	-105 <= Node.val <= 105
	pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""
from typing import Optional
import pytest
import sys
sys.path.append('../')
from exercise.list import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        if head.next == head:
            return head
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                while head is not slow:
                    slow = slow.next
                    head = head.next
                return head

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = f = head
        while f and f.next and f.next.next:
            s = s.next
            f = f.next.next
            if s is f:
                while s is not head:
                    s = s.next
                    head = head.next
                return head

        return None


def build_cyclic_list(values):
    m = {}
    arr = []
    for v in values:
        node = m.get(v, ListNode(v))
        m[v] = node
        arr.append(node)
    for i in range(len(arr)-1):
        arr[i].next = arr[i+1]
    return arr[0]


@pytest.mark.parametrize('values, expected', [
    ([3,2,0,-4, 2], 2),
    ([1,2, 1], 1),
    ([1], -1),
])
def test(values, expected):
    actual = Solution().detectCycle(build_cyclic_list(values))
    assert expected == (actual.val if actual is not None else -1)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
