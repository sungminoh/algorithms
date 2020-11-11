#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].

Note:

	1 <= len(A), len(B) <= 1000
	0 <= A[i], B[i] < 100
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        mat = [[0] * len(B) for _ in range(len(A))]
        for i in range(len(A)):
            if A[i] == B[0]:
                mat[i][0] = 1
        for j in range(len(B)):
            if A[0] == B[j]:
                mat[0][j] = 1
        for i in range(1, len(A)):
            for j in range(1, len(B)):
                if A[i] == B[j]:
                    mat[i][j] = mat[i-1][j-1] + 1
        return max(max(row) for row in mat)

    def _findLength(self, A: List[int], B: List[int]) -> int:
        @lru_cache(None)
        def rec(i, j):
            if i == 0 or j == 0:
                return 1 if A[i] == B[j] else 0
            return 1 + rec(i-1, j-1) if A[i] == B[j] else 0
        return max(rec(i, j) for i in range(len(A)) for j in range(len(B)))


@pytest.mark.parametrize('A, B, expected', [
    ([1,2,3,2,1], [3,2,1,4,7], 3),
    ([0,0,0,0,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,0,0,0,0,0,1,1,1,1,0,1,1,0,0,1,1,1,0,1,1,1,1,0,0,0,1,0,0,0,1,0,1,1,0,0,1,1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,1,1,1,0,0,0,1,1,0,1,0,1,0,0,1,1,0,1,0,0,0,1,1,0,1,1,0,0,1,0,0,1,1,1,0,0,1,1,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,0,1,0,0,1,0,0,1,1,0,0,1,0,1,0,1,1,0,0,1,1,0,0,0,1,0,1,0,0,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,0,1,1,0,1,1,1,0,1,0,1,1,0,1,0,0,1,0,0,1,1,1,0,0,0,1,1,1,0,0,1,0,0,1,0,0,1,0,1,1,0,0,0,0,1,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1,0,1,1,1,1,0,1,0,0,1,0,0,0,1,0,1,1,1,0,1,0,1,1,1,0,0,1,0,0,1,0,1,0,1,1,0,1,0,1,1,1,0,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,0,1,1,0,0,1,0,0,0,1,0,0,0,1,0,0,1,1,0,0,0,1,0,0,1,1,0,1,0,0,0,0,0,1,1,1,0,1,1,1,1,0,0,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,0,1,1,1,0,0,0,0,1,0,1,0,0,0,1,1,0,1,0,0,0,1,0,1,1,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,0,1,0,0,1,0,1,0,0,1,1,1,1,0,0,1,0,1,0,1,0,0,1,1,0,0,0,0,0,0,1,0,1,1,1,1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,1,1,0,0,0,1,1,0,1,0,1,1,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,0,0,1,1,1,0,1,0,1,1,1,1,1,1,0,0,1,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,0,1,1,0,0,1,1,0,0,1,1,1,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,0,1,0,0,1,0,0,1,0,0,1,0,0,0,1,0,1,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,1,0,1,0,1,1,1,0,0,0,1,1,1,1,1,0,1,1,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,1,0,1,1,0,1,0,1,1,0,1,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,0,1,0,1,1,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,1,1,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,1,1,0,0,1,1,1,1,0,1,1,0,1,1,0,1,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,1,0,0,1,0,0,1,1,0,0,0,1,1,1,0,0,0,0,1,0,0,1,0,1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,1,1,0,0,0,0,1,1,0,1],
     [0,1,0,1,1,0,0,1,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,1,1,0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,1,1,1,0,1,1,0,0,1,1,0,1,0,1,0,0,0,0,1,1,0,0,1,1,0,0,0,0,1,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,0,1,1,0,1,0,0,1,0,0,1,0,1,1,0,0,0,1,0,1,0,1,1,0,1,0,1,1,1,1,0,0,1,1,0,1,0,0,1,0,1,0,1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,0,1,0,0,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0,0,1,1,0,1,1,0,1,1,1,0,0,0,1,0,0,1,1,1,1,0,1,0,1,1,0,1,0,0,1,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1,1,0,1,0,1,1,0,1,1,0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,1,0,0,1,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,1,0,0,0,1,0,0,1,0,0,1,1,1,0,0,0,1,1,1,0,0,1,0,0,1,0,0,1,0,1,1,0,0,0,0,1,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1,0,1,1,1,1,0,1,0,0,1,0,0,0,1,0,1,1,1,0,1,0,1,1,1,0,0,1,0,0,1,0,1,0,1,1,0,1,0,1,1,1,0,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,0,1,1,0,0,1,0,0,0,1,0,0,0,1,0,0,1,1,0,0,0,1,0,0,1,1,0,1,0,0,0,0,0,1,1,1,0,1,1,1,1,0,0,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,0,1,1,1,0,0,0,0,1,0,1,0,0,0,1,1,0,1,0,0,0,1,0,1,1,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,0,1,0,0,1,0,1,0,0,1,1,1,1,0,0,1,0,1,0,1,0,0,1,1,0,0,0,0,0,0,1,0,1,1,1,1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,1,1,0,0,0,1,1,0,1,0,1,1,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,0,0,1,1,1,0,1,0,1,1,1,1,1,1,0,0,1,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,0,1,1,0,0,1,1,0,0,1,1,1,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,0,1,0,0,1,0,0,1,0,0,1,0,0,0,1,0,1,1,0,1,0,1,1,1,1,0,0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0,1,0,1,1,0,0,0,0,0,1,0,0,1,1,0,0,1,0,1,1,1,0,0,1,1,0,1,0,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,0,0,1,0,0,1,1,0,0,1,1,1,1,0,1,0,0,1,1,0,1,1,1,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,1,0,0,0,0,0,1,0,1,1], 500),
])
def test(A, B, expected):
    assert expected == Solution().findLength(A, B)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
