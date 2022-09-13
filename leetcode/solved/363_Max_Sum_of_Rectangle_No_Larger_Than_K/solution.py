#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than k.

Example 1:

Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).

Example 2:

Input: matrix = [[2,2,-1]], k = 3
Output: 3

Constraints:

	m == matrix.length
	n == matrix[i].length
	1 <= m, n <= 200
	-100 <= matrix[i][j] <= 100
	-105 <= k <= 105

Follow up: What if the number of rows is much larger than the number of columns?
"""
import bisect
from pathlib import Path
import json
import sys
import itertools
from typing import List
import pytest


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """10/13/2020 16:52"""
        if not matrix or not matrix[0]:
            return 0
        integral = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        integral[0][0] = matrix[0][0]
        for j in range(1, len(matrix[0])):
            integral[0][j] = matrix[0][j] + integral[0][j-1]
        for i in range(1, len(matrix)):
            integral[i][0] = matrix[i][0] + integral[i-1][0]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                integral[i][j] = matrix[i][j] + integral[i-1][j] + integral[i][j-1] - integral[i-1][j-1]
        ret = -float('inf')
        # print(integral)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for _i in range(i+1):
                    for _j in range(j+1):
                        s = integral[i][j] \
                            - (0 if _i == 0 else integral[_i-1][j]) \
                            - (0 if _j == 0 else integral[i][_j-1]) \
                            + (0 if _i == 0 or _j == 0 else integral[_i-1][_j-1])
                        # print(i, j, _i, _j, s)
                        if s <= k:
                            ret = max(ret, s)
        return ret

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        Sum by column between two rows to get an array.
        Then, apply find the max sum smaller than or equal to k
        Time complexity: O(n^3 * logn)
        Space complexity: O(n)
        """
        def max_sum_smaller_than_or_equal_to_k(arr, k):
            """
            Sum cumulatively and find a previous cumulative sum to subtract
            that makes the subtraction of two cumulative sum is smaller or
            equal to k
            Time complexity: O(n*logn)
            Space complexity: O(n)
            """
            sums = [0]
            cumulative_sum = 0
            m = -float('inf')
            for n in arr:
                cumulative_sum += n
                # Find an index of a previous cumulative sum that is larger or
                #  equal to cumulative_sum - k.
                #  So that cumulative_sum - (the previous cumulative sum) <= k
                i = bisect.bisect_left(sums, cumulative_sum-k)
                if i < len(sums):
                    m = max(m, cumulative_sum-sums[i])
                bisect.insort(sums, cumulative_sum)
            return m

        ret = -float('inf')
        m, n = len(matrix), len(matrix[0])
        for ri in range(m):
            sum_row = [0] * n
            for rj in range(ri, m):
                for ci in range(n):
                    sum_row[ci] += matrix[rj][ci]
                ret = max(ret, max_sum_smaller_than_or_equal_to_k(sum_row, k))
        return ret


    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        Time Complexity: O(n^4)
        Space Complexity: O(n^2)
        """
        m, n = len(matrix), len(matrix[0])

        integral = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                integral[i][j] = matrix[i][j] + integral[i-1][j] + integral[i][j-1] - integral[i-1][j-1]

        ret = -float('inf')
        for r1 in range(m):
            for r2 in range(r1, m):
                for c1 in range(n):
                    for c2 in range(c1, n):
                        area = integral[r2][c2] - integral[r1-1][c2] - integral[r2][c1-1] + integral[r1-1][c1-1]
                        if ret < area <= k:
                           ret = area
        return ret

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        Time Complexity: O(n^3 * logn) without considering insort
        Space Complexity: O(n)
        """
        m, n = len(matrix), len(matrix[0])
        ret = -float('inf')
        for r1 in range(m):
            cols = [0]*n
            for r2 in range(r1, m):
                for c in range(n):
                    cols[c] += matrix[r2][c]
                acc = [0]
                s = 0
                for c in range(n):
                    s += cols[c]
                    i = bisect.bisect_left(acc, s-k)
                    if i < len(acc):
                        ret = max(ret, s-acc[i])
                    bisect.insort(acc, s)
        return ret

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        Time Complexity: O(n^3 * logn)
        Space Complexity: O(n)
        """
        class TreeNode:
            def __init__(self, val):
                self.val = val
                self.left = None
                self.right = None

        def tree_find(root, val):
            if not root:
                return None
            if root.val < val:
                return tree_find(root.right, val)
            if root.val > val:
                ret = tree_find(root.left, val)
                if ret is not None:
                    return ret
            return root.val

        def tree_insert(root, val):
            if root.val <= val:
                if root.right is None:
                    root.right = TreeNode(val)
                else:
                    tree_insert(root.right, val)
            else:
                if root.left is None:
                    root.left = TreeNode(val)
                else:
                    tree_insert(root.left, val)

        def find(arr, k):
            tree = TreeNode(0)
            s = 0
            ret = -float('inf')
            for c in range(n):
                s += arr[c]
                val = tree_find(tree, s-k)
                if val is not None:
                    ret = max(ret, s-val)
                tree_insert(tree, s)
            return ret

        m, n = len(matrix), len(matrix[0])
        ret = -float('inf')
        for r1 in range(m):
            cols = [0]*n
            for r2 in range(r1, m):
                for c in range(n):
                    cols[c] += matrix[r2][c]
                ret = max(ret, find(cols, k))
        return ret


@pytest.mark.parametrize('matrix, k, expected', [
    ([[1,0,1],[0,-2,3]], 2, 2),
    ([[2,2,-1]], 3, 3),
    ([[2,2,-1]], 0, -1),
    ([[5,-4,-3,4],
      [-3,-4,4,5],
      [5,1,5,-4]], 3, 2),
    (*json.load(open(Path(__file__).parent/'testcase.json')), 287),
    (*json.load(open(Path(__file__).parent/'testcase2.json')), 287),
])
def test(matrix, k, expected):
    actual = Solution().maxSumSubmatrix(matrix, k)
    assert actual <= k
    assert expected == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
