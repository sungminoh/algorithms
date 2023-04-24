#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

Constraints:

	k == lists.length
	0 <= k <= 104
	0 <= lists[i].length <= 500
	-104 <= lists[i][j] <= 104
	lists[i] is sorted in ascending order.
	The sum of lists[i].length will not exceed 104.
"""
from heapq import heapify, heappop, heappush
from typing import Optional
from typing import List
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
    def mergeKLists(self, lists):
        """08/04/2018 22:06"""
        if not lists:
            return None
        from heapq import heappush, heappop
        heap = []
        tmp = 0
        for n in lists:
            if n:
                heappush(heap, (n.val, (tmp, n)))
                tmp += 1
        if not heap:
            return None
        head = cur = ListNode(None)
        while heap:
            v, (_, n) = heappop(heap)
            cur.next = n
            cur = cur.next
            nn = n.next
            if nn:
                heappush(heap, (nn.val, (tmp, nn)))
                tmp += 1
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Time complexity: O(n*m*n)
        Space complexity: O(n)
        """
        dummy = cur = ListNode()
        lists = [x for x in lists if x is not None]
        while lists:
            min_i = 0
            min_n = lists[0]
            for i in range(1, len(lists)):
                if lists[i].val < min_n.val:
                    min_i = i
                    min_n = lists[i]
            cur.next = min_n
            cur = cur.next
            lists[min_i] = lists[min_i].next
            if lists[min_i] is None:
                lists.pop(min_i)
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Feb 18, 2022 11:46
        Time complexity: O(n*m*logn)
        Space complexity: O(n)
        """
        dummy = cur = ListNode()
        heap = []
        i = 0
        for node in lists:
            if node is not None:
                heappush(heap, (node.val, i, node))
                i += 1
        while heap:
            _, _, node = heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next is not None:
                heappush(heap, (node.next.val, i, node.next))
                i += 1
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Apr 13, 2023 00:24"""
        h = [(l.val, i, l) for i, l in enumerate(lists) if l]
        heapify(h)
        dummy = ListNode()
        cur = dummy
        while h:
            _, i, n = heappop(h)
            if n.next:
                heappush(h, (n.next.val, i, n.next))
            cur.next = n
            cur = cur.next
            cur.next = None
        return dummy.next


@pytest.mark.parametrize('args', [
    (([[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6])),
    (([], [])),
    (([[]], [])),
])
def test(args):
    assert build_list(args[-1]) == Solution().mergeKLists([build_list(x) for x in args[0]])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
