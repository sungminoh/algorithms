#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

	intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
	listA - The first linked list.
	listB - The second linked list.
	skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
	skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.

The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

Example 1:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:

Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:

Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

Constraints:

	The number of nodes of listA is in the m.
	The number of nodes of listB is in the n.
	1 <= m, n <= 3 * 104
	1 <= Node.val <= 105
	0 <= skipA < m
	0 <= skipB < n
	intersectVal is 0 if listA and listB do not intersect.
	intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?
"""
from typing import Optional
import pytest
import sys
sys.path.append('../')
from exercise.list import ListNode, build_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """06/18/2022 11:06
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        visited = set()
        node = headA
        while node:
            visited.add(id(node))
            node = node.next
        node = headB
        while node:
            if id(node) in visited:
                return node
            node = node.next

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """06/18/2022 12:53
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n1 = headA
        n2 = headB
        while id(n1) != id(n2):
            n1 = n1.next if n1 else headB
            n2 = n2.next if n2 else headA
        return n1


def build_list_with_intersect(listA, listB, skipA, skipB):
    dummyA = ListNode()
    dummyA.next = build_list(listA[:skipA])
    dummyB = ListNode()
    dummyB.next = build_list(listB[:skipB])
    tail = build_list(listA[skipA:])

    def connect(l1, l2):
        p = None
        n = l1
        while n:
            p, n = n, n.next
        if p:
            p.next = l2

    connect(dummyA, tail)
    connect(dummyB, tail)
    return dummyA.next, dummyB.next


@pytest.mark.parametrize('intersectVal, listA, listB, skipA, skipB, expected', [
    (8, [4,1,8,4,5], [5,6,1,8,4,5], 2, 3, 8),
    (2, [1,9,1,2,4], [3,2,4], 3, 1, 2),
    (0, [2,6,4], [1,5], 3, 2, None),
])
def test(intersectVal, listA, listB, skipA, skipB, expected):
    actual = Solution().getIntersectionNode(*build_list_with_intersect(listA, listB, skipA, skipB))
    assert (expected is None and actual is None) or expected == actual.val


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
