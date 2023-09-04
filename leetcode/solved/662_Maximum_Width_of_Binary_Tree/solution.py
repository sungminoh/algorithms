from collections import defaultdict
from collections import deque
from typing import Optional

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

Example 1:

Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

Example 2:

Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

Example 3:

Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).

Constraints:

	The number of nodes in the tree is in the range [1, 3000].
	-100 <= Node.val <= 100
"""
import pytest
import sys
sys.path.append('../')
from exercise.tree import TreeNode, build_tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        """08/11/2020 22:36"""
        minmax = defaultdict(lambda: [float('inf'), -float('inf')])

        def traverse(node, depth, pos):
            if node is None:
                return
            minmax[depth][0] = min(minmax[depth][0], pos)
            minmax[depth][1] = max(minmax[depth][1], pos)
            traverse(node.left, depth+1, pos*2 - 1)
            traverse(node.right, depth+1, pos*2)

        traverse(root, 0, 1)
        return max(m - n + 1 for n, m in minmax.values())

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        """08/11/2020 22:36"""
        q = deque([(root, 0, 1)])
        d = 0
        n, m = 1, 1
        ret = 1
        while q:
            node, depth, pos = q.popleft()
            if depth != d:
                ret = max(ret, m-n+1)
                n = m = pos
                d = depth
            else:
                n = min(n, pos)
                m = max(m, pos)
            if node.left:
                q.append((node.left, depth+1, pos*2-1))
            if node.right:
                q.append((node.right, depth+1, pos*2))
        ret = max(ret, m-n+1)
        return ret

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """03/11/2022 16:55"""
        ret = 0
        queue = deque()
        if root:
            queue.append((0, root))
        while queue:
            size = len(queue)
            mn = float('inf')
            mx = -float('inf')
            for _ in range(size):
                idx, node = queue.popleft()
                mn = min(mn, idx)
                mx = max(mx, idx)
                if node.left:
                    queue.append((idx<<1, node.left))
                if node.right:
                    queue.append(((idx<<1) + 1, node.right))
            ret = max(ret, mx-mn+1)
        return ret

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """Sep 03, 2023 21:33"""
        depth_lr = {}

        def dfs(node, d, i):
            if not node:
                return
            mn, mx = depth_lr.setdefault(d, [float('inf'), -float('inf')])
            depth_lr[d] = [min(mn, i), max(mx, i)]
            dfs(node.left, d+1, 2*i)
            dfs(node.right, d+1, 2*i+1)

        dfs(root, 0, 0)
        ret = 0
        for l, r in depth_lr.values():
            ret = max(ret, r-l+1)
        return ret


@pytest.mark.parametrize('args', [
    (([1,3,2,5,3,None,9], 4)),
    (([1,3,2,5,None,None,9,6,None,7], 7)),
    (([1,3,2,5], 2)),
    (([1,3,None,5,3], 2)),
    (([1,3,2,5,None,None,9,6,None,None,7], 8)),
])
def test(args):
    assert args[-1] == Solution().widthOfBinaryTree(build_tree(*args[:-1]))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
