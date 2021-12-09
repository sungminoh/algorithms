#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:

Input: matrix = [["0"]]
Output: 0

Example 3:

Input: matrix = [["1"]]
Output: 1

Constraints:

	rows == matrix.length
	cols == matrix[i].length
	1 <= row, cols <= 200
	matrix[i][j] is '0' or '1'.
"""
import sys
from typing import List
import pytest


class Solution:
    def maximalRectangle(self, matrix):
        """08/14/2018 22:15"""
        def largestRectangleArea(heights):
            ret = 0
            stack = []
            heights.append(0)
            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] >= h:
                    ph = heights[stack.pop()]
                    w = i - (stack[-1] if stack else -1) - 1
                    ret = max(ret, ph * w)
                stack.append(i)
            return ret

        if not matrix:
            return 0
        h, w = len(matrix), len(matrix[0])
        m = [[0]*w for _ in range(h)]
        ret = 0
        heights = [0] * w
        for i in range(h):
            for j in range(w):
                heights[j] = (heights[j] + 1) if int(matrix[i][j]) == 1 else 0
            ret = max(ret, largestRectangleArea(heights))
        return ret

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])

        def find_max_area(nums):
            nums += [0]
            ret = 0
            stack = []
            for i, n in enumerate(nums):
                while stack and nums[stack[-1]] >= n:
                    height = nums[stack.pop()]
                    j = -1 if not stack else stack[-1]
                    width = (i-1) - j
                    ret = max(ret, width*height)
                stack.append(i)
            return ret

        ret = 0
        row = [0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    row[j] = 0
                else:
                    row[j] += 1
            ret = max(ret, find_max_area(row))

        return ret


@pytest.mark.parametrize('matrix, expected', [
    ([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], 6),
    ([["0"]], 0),
    ([["1"]], 1),
    ([["0","0","1"],["1","1","1"]], 3),
    ([["0","1","1","0","1"],
      ["1","1","0","1","0"],
      ["0","1","1","1","0"],
      ["1","1","1","1","0"],
      ["1","1","1","1","1"],
      ["0","0","0","0","0"]], 9),
])
def test(matrix, expected):
    assert expected == Solution().maximalRectangle(matrix)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
