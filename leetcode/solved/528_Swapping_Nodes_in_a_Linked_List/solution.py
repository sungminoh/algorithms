#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Constraints:

	The number of nodes in the list is n.
	1 <= k <= n <= 105
	0 <= Node.val <= 100
"""
from typing import Tuple
from typing import List
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
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def length(head):
            cnt = 0
            while head:
                cnt += 1
                head = head.next
            return cnt

        def get_nths(head, indexes) -> List[ListNode]:
            indexes.sort()
            i = 0
            ret = []
            j = 0
            while head and i < len(indexes):
                if indexes[i] == j:
                    ret.append(head)
                    i += 1
                j += 1
                head = head.next
            return ret

        n = length(head)
        indexes = [k - 1, n+1-k - 1]  # -1 to get parent nodes
        if indexes[0] == indexes[1]:
            return head

        dummy = ListNode()
        dummy.next = head
        parents = get_nths(dummy, indexes)
        p1, p2 = parents[0], parents[1]
        n1 = p1.next
        n2 = p2.next
        if indexes[0]+1 == indexes[1]:
            n1.next = n2.next
            n2.next = n1
            p1.next = n2
        else:
            n1.next, n2.next = n2.next, n1.next
            p1.next, p2.next = p2.next, p1.next
        return dummy.next


@pytest.mark.parametrize('values, k, expected', [
    ([1,2,3,4,5], 2, [1,4,3,2,5]),
    ([7,9,6,6,7,8,3,0,9,5], 5, [7,9,6,6,8,7,3,0,9,5]),
])
def test(values, k, expected):
    assert build_list(expected) == Solution().swapNodes(build_list(values), k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
