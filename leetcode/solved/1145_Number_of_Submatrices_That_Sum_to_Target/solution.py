#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

Example 1:

Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Example 3:

Input: matrix = [[904]], target = 0
Output: 0

Constraints:

	1 <= matrix.length <= 100
	1 <= matrix[0].length <= 100
	-1000 <= matrix[i] <= 1000
	-10^8 <= target <= 10^8
"""
from itertools import accumulate
from pathlib import Path
import json
import sys
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
        Time complexity: O(n^4)
        Space complexity: O(n^2)
        """
        def area(i, j, x, y):
            return integral[i][j] - integral[x-1][j] - integral[i][y-1] + integral[x-1][y-1]

        def build_integral(matrix):
            integral = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
            n, m = len(matrix), len(matrix[0])
            for i in range(n):
                for j in range(m):
                    integral[i][j] = integral[i-1][j] + integral[i][j-1] - integral[i-1][j-1] + matrix[i][j]
            return integral

        if not matrix or not matrix[0]:
            return 0

        n, m = len(matrix), len(matrix[0])
        integral = build_integral(matrix)
        cnt = 0
        for i in range(n):
            for j in range(m):
                for x in range(i):
                    for y in range(j):
                        if area(i, j, x, y) == target:
                            cnt += 1
        return cnt

    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """When all elements are >= 0"""
        def area(mat, x, y, i, j):
            return mat[i][j] - mat[x-1][j] - mat[i][y-1] + mat[x-1][y-1]

        def build_integral(matrix):
            integral = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
            n, m = len(matrix), len(matrix[0])
            for i in range(n):
                for j in range(m):
                    integral[i][j] = integral[i-1][j] + integral[i][j-1] - integral[i-1][j-1] + matrix[i][j]
            return integral

        def bisearch(s, e, t, key=lambda x: x):
            while s <= e:
                m = s + (e-s)//2
                v = key(m)
                if v >= t:
                    e = m-1
                else:
                    s = m+1
            return e+1

        if not matrix or not matrix[0]:
            return 0

        n, m = len(matrix), len(matrix[0])
        integral = build_integral(matrix)
        cnt = 0
        for i in range(n):
            for j in range(m):
                row_idx = bisearch(i, n-1, target, key=lambda x: area(integral, i, j, x, m-1))
                e = m-1
                for x in range(row_idx, n):
                    if e < 0:
                        break;
                    e = bisearch(j, e, target, key=lambda y: area(integral, i, j, x, y))
                    if area(integral, i, j, x, e) == target:
                        cnt += 1
                    e -= 1
        return cnt

    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """05/09/2021 22:46
        For a given two row indexes of integral sum, apply below algrithm which is O(n)
        560_Subarray_Sum_Equals_K
        https://github.com/sungminoh/algorithms/tree/master/leetcode/solved/560_Subarray_Sum_Equals_K

        Time complexity: O(n^3)
        Space complexity: O(n^2) + O(n)
        """
        def area(mat, x, y, i, j):
            return mat[i][j] - mat[x-1][j] - mat[i][y-1] + mat[x-1][y-1]

        def build_integral(matrix):
            integral = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
            n, m = len(matrix), len(matrix[0])
            for i in range(n):
                for j in range(m):
                    integral[i][j] = integral[i-1][j] + integral[i][j-1] - integral[i-1][j-1] + matrix[i][j]
            return integral

        def find(arr, k):
            cnt = 0
            cumsum = defaultdict(int)
            cumsum[0] = 1
            for i, n in enumerate(accumulate(arr)):
                cnt += cumsum.get(n-k, 0)
                cumsum[n] += 1
            return cnt

        if not matrix or not matrix[0]:
            return 0

        n, m = len(matrix), len(matrix[0])
        integral = build_integral(matrix)
        cnt = 0
        for i1 in range(n):
            for i2 in range(i1, n):
                arr = [area(integral, i1, j, i2, j) for j in range(m)]
                cnt += find(arr, target)
        return cnt

    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """08/01/2022 11:15"""
        m, n = len(matrix), len(matrix[0])
        # construct the integral matrix
        integral = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                integral[i][j] = matrix[i][j] + integral[i-1][j] + integral[i][j-1] - integral[i-1][j-1]
        ret = 0
        for i1 in range(m):
            for i2 in range(i1, m):
                cnt = defaultdict(int)
                cnt[0] = 1
                for j2 in range(n):
                    area = integral[i2][j2] - integral[i1-1][j2]
                    ret += cnt.get(area-target, 0)
                    cnt[area] += 1
        return ret


@pytest.mark.parametrize('matrix, target, expected', [
    ([[0,1,0],[1,1,1],[0,1,0]], 0, 4),
    ([[0,1,0],[1,1,1],[0,1,0]], 4, 4),
    ([[0,1,0],[1,1,1],[0,1,0]], 3, 6),
    ([[1,-1],[-1,1]], 0, 5),
    ([[904]], 0, 0),
    (*json.load(open(Path(__file__).parent/'testcase.json')), 3),
])
def test(matrix, target, expected):
    assert expected == Solution().numSubmatrixSumTarget(matrix, target)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
