
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

Example 1:

Input: m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:

Input: m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:

Note:
	1. Once you move the ball out of boundary, you cannot move it back.
	2. The length and height of the grid is in range [1,50].
	3. N is in range [0,50].
"""
import sys
from functools import lru_cache
import pytest


class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        @lru_cache(None)
        def _rec(i, j, k):
            if k == 0:
                return 0
            cnt = 0
            if i == 0:
                cnt += 1
            if i == m-1:
                cnt += 1
            if j == 0:
                cnt += 1
            if j == n-1:
                cnt += 1

            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    cnt += _rec(x, y, k-1) % (1e9 + 7)
            return cnt

        return _rec(i, j, N) % (1e9 + 7)



@pytest.mark.parametrize('m, n, N, i, j, expected', [
    (2, 2, 2, 0, 0, 6),
    (1, 3, 3, 0, 1, 12),
    (8, 50, 23, 5, 26, 914783380),
])
def test(m, n, N, i, j, expected):
    assert expected == Solution().findPaths(m, n, N, i, j)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
