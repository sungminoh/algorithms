#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0.  What is the largest axis-aligned plus sign of 1s contained in the grid?  Return the order of the plus sign.  If there is none, return 0.

An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s.  This is demonstrated in the diagrams below.  Note that there could be 0s or 1s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.

Examples of Axis-Aligned Plus Signs of Order k:
Order 1:
000
010
000

Order 2:
00000
00100
01110
00100
00000

Order 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000

Example 1:
Input: N = 5, mines = [[4, 2]]
Output: 2
Explanation:
11111
11111
11111
11111
11011
In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.

Example 2:
Input: N = 2, mines = []
Output: 1
Explanation:
There is no plus sign of order 2, but there is of order 1.

Example 3:
Input: N = 1, mines = [[0, 0]]
Output: 0
Explanation:
There is no plus sign, so return 0.

Note:
N will be an integer in the range [1, 500].
mines will have length at most 5000.
mines[i] will be length 2 and consist of integers in the range [0, N-1].
(Additionally, programs submitted in C, C++, or C# will be judged with a slightly smaller time limit.)
"""
import sys
from typing import List
import pytest


class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        mat = [[1] * N for _ in range(N)]
        for i, j in mines:
            mat[i][j] = 0

        if not mat:
            return 0

        leftup = [[(0, 0)] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                e = mat[i][j]
                toleft = leftup[i][j-1][0]*e+e
                toup = leftup[i-1][j][1]*e+e
                leftup[i][j] = (toleft, toup)

        rightdown = [[(0, 0)] * N for _ in range(N)]
        for i in range(N-1, -1, -1):
            for j in range(N-1, -1, -1):
                e = mat[i][j]
                toright = rightdown[i][(j+1)%N][0]*e+e
                todown = rightdown[(i+1)%N][j][1]*e+e
                rightdown[i][j] = (toright, todown)

        return max(min([*leftup[i][j], *rightdown[i][j]]) for i in range(N) for j in range(N))


@pytest.mark.parametrize('N, mines, expected', [
    (5, [[4, 2]], 2),
    (2, [], 1),
    (1, [[0, 0]], 0),
])
def test(N, mines, expected):
    print()
    assert expected == Solution().orderOfLargestPlusSign(N, mines)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
