#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

Example 1:

Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].

Example 2:

Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

Constraints:

	The number of nodes in the list is in the range [0, 1000].
	0 <= Node.val <= 1000
	1 <= k <= 50
"""
import sys
from typing import List
from typing import Optional
import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'({self.val}) -> {self.next}'

    def __eq__(self, other):
        return False if self.val != other.val else self.next == other.next


def build(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    node = head
    for v in vals[1:]:
        node.next = ListNode(v)
        node = node.next
    return head


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        """09/03/2020 23:27"""
        def get_size(root: ListNode):
            cnt = 0
            while root:
                cnt += 1
                root = root.next
            return cnt

        size = get_size(root)
        q, r = divmod(size, k)
        ret = []
        node = root
        while node:
            ret.append(node)
            n = q
            if r:
                n += 1
                r -= 1
            while node and n-1:
                n -= 1
                node = node.next
            node.next, node = None, node.next
        while len(ret) < k:
            ret.append(None)
        return ret

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next

        ret = []

        q, r = divmod(n, k)
        node = head
        start = node
        l = 1
        while node:
            next_node = node.next
            if l == q + min(1, r):
                ret.append(start)
                start = node.next
                node.next = None
                r = max(0, r-1)
                l = 0
            l += 1
            node = next_node

        while len(ret) < k:
            ret.append(None)

        return ret


@pytest.mark.parametrize('nodes, k, expected', [
    ([1,2,3], 5, [[1],[2],[3],[],[]]),
    ([1,2,3,4,5,6,7,8,9,10], 3, [[1,2,3,4],[5,6,7],[8,9,10]]),
    ([], 3, [[],[],[]]),
])
def test(nodes, k, expected):
    assert [build(x) for x in expected] == Solution().splitListToParts(build(nodes), k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
