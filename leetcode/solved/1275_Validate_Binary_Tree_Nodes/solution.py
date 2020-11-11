#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

Example 1:

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true

Example 2:

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false

Example 3:

Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false

Example 4:

Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
Output: false

Constraints:

	1 <= n <= 10^4
	leftChild.length == rightChild.length == n
	-1 <= leftChild[i], rightChild[i] <= n - 1
"""
import sys
from typing import List
import pytest


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [None] * n
        def dfs(i, root):
            if leftChild[i] != -1:
                if parent[leftChild[i]] == root:
                    return False
                if parent[leftChild[i]] is not None:
                    parent[leftChild[i]] = root
                else:
                    parent[leftChild[i]] = root
                    if not dfs(leftChild[i], root):
                        return False
            if rightChild[i] != -1:
                if parent[rightChild[i]] == root:
                    return False
                if parent[rightChild[i]] is not None:
                    parent[rightChild[i]] = root
                else:
                    if not dfs(rightChild[i], root):
                        return False
                    parent[rightChild[i]] = root
            return True

        for i in range(n):
            if parent[i] is not None:
                continue
            parent[i] = i
            if not dfs(i, i):
                return False
        return sum(1 if i == p else 0 for i, p in enumerate(parent)) == 1


@pytest.mark.parametrize('n, leftChild, rightChild, expected', [
    (4, [1,-1,3,-1], [2,-1,-1,-1], True),
    (4, [1,-1,3,-1], [2,3,-1,-1], False),
    (2, [1,0], [-1,-1], False),
    (6, [1,-1,-1,4,-1,-1], [2,-1,-1,5,-1,-1], False),
])
def test(n, leftChild, rightChild, expected):
    assert expected == Solution().validateBinaryTreeNodes(n, leftChild, rightChild)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
