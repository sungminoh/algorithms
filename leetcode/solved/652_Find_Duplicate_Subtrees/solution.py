#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

Example 1:

Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:

Input: root = [2,1,1]
Output: [[1]]

Example 3:

Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]

Constraints:

	The number of the nodes in the tree will be in the range [1, 5000]
	-200 <= Node.val <= 200
"""
from collections import defaultdict
from typing import List
from typing import Optional
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
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        """Jul 07, 2020 21:12"""
        ret = dict()
        id_map = defaultdict()
        def get_id(node):
            if not node:
                return
            left = get_id(node.left)
            right = get_id(node.right)
            key = (node.val, left, right)
            if key not in id_map:
                id_map[key] = len(id_map)
            else:
                ret[key] = node
            return id_map[key]
        get_id(root)
        return list(ret.values())

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """Apr 02, 2023 19:20"""
        ret = []
        cache = {}
        visited = set()
        def dfs(node):
            if not node:
                return tuple()
            nonlocal ret, cache
            key = (node.val, dfs(node.left), dfs(node.right))
            if key in cache and key not in visited:
                visited.add(key)
                ret.append(node)
            cache.setdefault(key, node)
            return key
        dfs(root)
        return ret

@pytest.mark.parametrize('args', [
    (([1,2,3,4,None,2,4,None,None,4], [[2,4],[4]])),
    (([2,1,1], [[1]])),
    (([2,2,2,3,None,3,None], [[2,3],[3]])),
    (([1,2,3,4,None,2,4,None,None,4], [[2,4],[4]])),
    (([0,0,0,0,None,None,0,None,None,None,0], [[0]])),
])
def test(args):
    expected = [build_tree(x) for x in args[-1]]
    for x in Solution().findDuplicateSubtrees(build_tree(*args[:-1])):
        assert any(x == exp for exp in expected)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
