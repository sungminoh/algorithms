#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.

Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.

Example 1:

Input: n = 5, mines = [[4,2]]
Output: 2
Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.

Example 2:

Input: n = 1, mines = [[0,0]]
Output: 0
Explanation: There is no plus sign, so return 0.

Constraints:

	1 <= n <= 500
	1 <= mines.length <= 5000
	0 <= xi, yi < n
	All the pairs (xi, yi) are unique.
"""
import sys
from typing import List
import pytest


class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        """09/10/2020 01:12
        Top left and bottom right DP
        Time complexity: O(n^2)
        Time complexity: O(n^2)
        """
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

    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        """
        Horizontal and vertical line sweep
        Time complexity: O(n^2)
        Time complexity: O(n^2)
        """
        board = [[1]*n for _ in range(n)]
        for x, y in mines:
            board[x][y] = 0

        def slide(i, row):
            if row:
                arr = board[i]
            else:
                arr = [r[i] for r in board]
            left = [arr[0]]
            for x in arr[1:]:
                if x == 1:
                    left.append(left[-1]+1)
                else:
                    left.append(0)
            right = [arr[-1]]
            for x in reversed(arr[:-1]):
                if x == 1:
                    right.append(right[-1]+1)
                else:
                    right.append(0)
            right.reverse()
            return [min(left[i], right[i]) for i in range(len(arr))]

        horizontal = [slide(i, True) for i in range(n)]
        vertical = [slide(j, False) for j in range(n)]

        ret = 0
        for i in range(n):
            for j in range(n):
                ret = max(ret, min(horizontal[i][j], vertical[j][i]))
        return ret


@pytest.mark.parametrize('n, mines, expected', [
    (2, [], 1),
    (5, [[4,2]], 2),
    (1, [[0,0]], 0),
    (2, [[0,0],[0,1],[1,0]], 1)
])
def test(n, mines, expected):
    assert expected == Solution().orderOfLargestPlusSign(n, mines)


if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))


