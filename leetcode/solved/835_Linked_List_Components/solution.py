
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We are given head, the head node of a linked list containing unique integer values.

We are also given the list G, a subset of the values in the linked list.

Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.

Example 1:

Input:
head: 0->1->2->3
G = [0, 1, 3]
Output: 2
Explanation:
0 and 1 are connected, so [0, 1] and [3] are the two connected components.

Example 2:

Input:
head: 0->1->2->3->4
G = [0, 3, 1, 4]
Output: 2
Explanation:
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.

Note:

	If N is the length of the linked list given by head, 1 .
	The value of each node in the linked list will be in the range [0, N - 1].
	1 .
	G is a subset of all values in the linked list.
"""
import sys
from typing import List
import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        G = set(G)
        cnt = 0
        node = head
        started = False
        while node:
            if not started:
                if node.val in G:
                    started = True
                else:
                    pass
            elif started:
                if node.val in G:
                    pass
                else:
                    started = False
                    cnt += 1
            node = node.next
        if started:
            cnt += 1
        return cnt


@pytest.mark.parametrize('nums, G, expected', [
    ([0,1,2,3], [0,1,3], 2),
    ([0,1,2,3,4], [0,3,1,4], 2),
])
def test(nums, G, expected):
    dummy = ListNode()
    node = dummy
    for n in nums:
        node.next = ListNode(n)
        node = node.next
    head = dummy.next
    assert expected == Solution().numComponents(head, G)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
