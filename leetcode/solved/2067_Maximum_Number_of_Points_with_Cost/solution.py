#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

	x for x >= 0.
	-x for x < 0.

Example 1:

Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9.

Example 2:

Input: points = [[1,5],[2,3],[4,2]]
Output: 11
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
You add 5 + 3 + 4 = 12 to your score.
However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
Your final score is 12 - 1 = 11.

Constraints:

	m == points.length
	n == points[r].length
	1 <= m, n <= 105
	1 <= m * n <= 105
	0 <= points[r][c] <= 105
"""
from pathlib import Path
import json
from typing import List
import pytest
import sys


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """TLE"""
        M, N = len(points), len(points[0])
        cur = [p for p in points[0]]
        for i in range(1, M):
            new = [-float('inf')]*N
            for j in range(N):
                for k in range(N):
                    new[j] = max(new[j], points[i][j] + cur[k] - abs(j - k))
            cur = new
        return max(cur)

    def maxPoints(self, points: List[List[int]]) -> int:
        """Nov 06, 2024 16:56"""
        M, N = len(points), len(points[0])

        def cummax(arr):
            ret = [arr[0]]
            for i in range(1, N):
                ret.append(max(ret[-1] - 1, arr[i]))
            return ret

        cur = points[0]
        leftmax = cummax(cur)
        rightmax = cummax(cur[::-1])[::-1]
        for i in range(1, M):
            cur = [points[i][j] + max(l, r) for j, (l, r) in enumerate(zip(leftmax, rightmax))]
            leftmax_ = cummax(cur)
            rightmax_ = cummax(cur[::-1])[::-1]
            leftmax = leftmax_
            rightmax = rightmax_
        return max(cur)


@pytest.mark.parametrize('args', [
    (([[1,2,3],[1,5,1],[3,1,1]], 9)),
    (([[1,5],[2,3],[4,2]], 11)),
    ((json.load(open(Path(__file__).parent/'testcase.json')), 108657)),
])
def test(args):
    assert args[-1] == Solution().maxPoints(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
