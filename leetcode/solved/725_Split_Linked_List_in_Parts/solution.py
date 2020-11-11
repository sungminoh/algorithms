#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1.  This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples
1->2->3->4, k = 5 // 5 equal parts
[ [1],
[2],
[3],
[4],
null ]

Example 1:

Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].

Example 2:

Input:
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

Note:
The length of root will be in the range [0, 1000].
Each value of a node in the input will be an integer in the range [0, 999].
k will be an integer in the range [1, 50].
"""
import sys
from typing import List
import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'({self.val}) -> {self.next!r}'


class Solution:
    def get_size(self, root: ListNode):
        cnt = 0
        while root:
            cnt += 1
            root = root.next
        return cnt

    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        size = self.get_size(root)
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

def build_node(vals):
    root = None
    tail = None
    for v in vals:
        n = ListNode(v)
        if not root:
            root = tail = n
        else:
            tail.next = n
            tail = n
    return root


def node_to_list(root):
    ret = []
    while root:
        ret.append(root.val)
        root = root.next
    return ret


@pytest.mark.parametrize('nodes, k, expected', [
    ([1,2,3], 5, [[1],[2],[3],[],[]]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]),
    ([], 3, [[],[],[]]),
])
def test(nodes, k, expected):
    print()
    root = build_node(nodes)
    print(root)
    actual = Solution().splitListToParts(root, k)
    print(actual)
    actual = [node_to_list(x) for x in actual]
    print(actual)
    assert expected == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
