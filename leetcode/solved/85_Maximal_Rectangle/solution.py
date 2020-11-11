#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6

"""

class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        h, w = len(matrix), len(matrix[0])
        m = [[0]*w for _ in range(h)]
        ret = 0
        heights = [0] * w
        for i in range(h):
            for j in range(w):
                heights[j] = (heights[j] + 1) if int(matrix[i][j]) == 1 else 0
            ret = max(ret, self.largestRectangleArea(heights))
        return ret

    def largestRectangleArea(self, heights):
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


def main():
    matrix = []
    row = [int(x) for x in input().split()]
    while row:
        matrix.append(row)
        row = [int(x) for x in input().split()]
    print(Solution().maximalRectangle(matrix))




if __name__ == '__main__':
    main()
