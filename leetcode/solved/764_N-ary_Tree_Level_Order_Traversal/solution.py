
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

Constraints:

	The height of the n-ary tree is less than or equal to 1000
	The total number of nodes is between [0, 10^4]
"""
import sys
from typing import Any
from typing import List
from collections import deque
import pytest


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque([(0, root)])
        ret = []
        while queue:
            l, n = queue.popleft()
            if l < len(ret):
                ret[l].append(n.val)
            else:
                ret.append([n.val])
            if n.children:
                for c in n.children:
                    queue.append((l + 1, c))
        return ret


def deserialize(arr: List[Any]) -> 'Node':
    if not arr:
        return None
    root = Node(arr[0])
    queue = deque([root])
    i = 2
    while i < len(arr):
        vals = []
        while i < len(arr) and arr[i] is not None:
            vals.append(Node(arr[i]))
            queue.append(vals[-1])
            i += 1
        node = queue.popleft()
        node.children = vals
        i += 1
    return root


@pytest.mark.parametrize('arr, expected', [
    ([1,None,3,2,4,None,5,6], [[1],[3,2,4],[5,6]]),
    ([1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14], [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]])
])
def test(arr, expected):
    assert expected == Solution().levelOrder(deserialize(arr))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
