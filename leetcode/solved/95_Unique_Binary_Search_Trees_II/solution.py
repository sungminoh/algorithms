#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

Example 2:

Input: n = 1
Output: [[1]]

Constraints:

	1 <= n <= 8
"""
from collections import defaultdict
from pathlib import Path
from typing import Optional
from typing import List
import pytest
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))
from exercise.tree import TreeNode, build_tree


class Solution:
    def generateTrees(self, n):
        """05/06/2018 05:51"""
        memo = defaultdict(dict)
        def generateTreesDP(n, add):
            if n == 0:
                return [None]
            if n == 1:
                return [TreeNode(1 + add)]
            if n in memo and add in memo[n]:
                return memo[n][add]
            ret = []
            for i in range(1, n+1):
                left_trees = generateTreesDP(i-1, add)
                right_trees = generateTreesDP(n-i, add+i)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(add+i)
                        root.left = left
                        root.right = right
                        ret.append(root)
            memo[n][add] = ret
            return ret

        if n == 0:
            return []
        return generateTreesDP(n, 0)

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def build(a, b):
            if a > b:
                yield None
            elif a == b:
                yield TreeNode(a)
            else:
                for i in range(a, b+1):
                    for left in build(a, i-1):
                        for right in build(i+1, b):
                            yield TreeNode(i, left=left, right=right)
        return list(build(1, n))


@pytest.mark.parametrize('n, expected', [
    (3, [[1,None,2,None,3],[1,None,3,2],[2,1,3],[3,1,None,None,2],[3,2,None,1]]),
    (1, [[1]]),
])
def test(n, expected):
    trees = [build_tree(x) for x in expected]
    actual = Solution().generateTrees(n)
    for t in actual:
        print('--------')
        print(t)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
