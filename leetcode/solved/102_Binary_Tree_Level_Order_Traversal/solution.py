#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

Constraints:

	The number of nodes in the tree is in the range [0, 2000].
	-1000 <= Node.val <= 1000
"""
from collections import defaultdict
from collections import deque
from typing import List
import pytest
import sys
sys.path.append('../../')
from exercise.tree import TreeNode, build_tree


class Solution:
    memo = defaultdict(list)
    def tree2list(self, r, d=0):
        if d == 0:
            self.memo.clear()
        if not r:
            return
        self.memo[d].append(r.val)
        self.tree2list(r.left, d+1)
        self.tree2list(r.right, d+1)

    def levelOrder(self, root):
        """05/06/2018 22:20"""
        self.tree2list(root)
        return [v for k, v in sorted(self.memo.items(), key=lambda x: x[0])]


    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(0, root)])
        ret = []
        level = []
        cur = 0
        while queue:
            l, n = queue.popleft()
            if l != cur:
                ret.append(level)
                level = []
                cur = l
            level.append(n.val)
            if n.left:
                queue.append((l+1, n.left))
            if n.right:
                queue.append((l+1, n.right))
        ret.append(level)
        return ret


@pytest.mark.parametrize('nodes, expected', [
    ([3,9,20,None,None,15,7], [[3],[9,20],[15,7]]),
    ([1], [[1]]),
    ([], []),
])
def test(nodes, expected):
    print()
    root = build_tree(nodes)
    print(root)
    assert expected == Solution().levelOrder(root)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
