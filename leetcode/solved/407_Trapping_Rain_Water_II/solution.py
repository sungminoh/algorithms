#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.

The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.

After the rain, water is trapped between the blocks. The total volume of water trapped is 4.

Constraints:

	1 <= m, n <= 110
	0 <= heightMap[i][j] <= 20000
"""
from heapq import heappush
from heapq import heappop
from heapq import heapify
import sys
from typing import List
import pytest


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        N, M = len(heightMap), len(heightMap[0])
        h = []
        visited = set()
        for j in range(M):
            h.append((heightMap[0][j], 0, j))
            h.append((heightMap[N-1][j], N-1, j))
            visited.add((0, j))
            visited.add((N-1, j))
        for i in range(1, N-1):
            h.append((heightMap[i][0], i, 0))
            h.append((heightMap[i][M-1], i, M-1))
            visited.add((i, 0))
            visited.add((i, M-1))
        heapify(h)

        def neighbor(i, j):
            if i > 0:
                yield i-1, j
            if i < N-1:
                yield i+1, j
            if j > 0:
                yield i, j-1
            if j < M-1:
                yield i, j+1

        m = -float('inf')
        s = 0
        while h:
            x, i, j = heappop(h)
            m = max(m, x)
            for _i, _j in neighbor(i, j):
                if (_i, _j) not in visited:
                    s += max(0, m - heightMap[_i][_j])
                    visited.add((_i, _j))
                    heappush(h, (heightMap[_i][_j], _i, _j))
        return s


@pytest.mark.parametrize('heightMap, expected', [
    ([
        [1,4,3,1,3,2],
        [3,2,1,3,2,4],
        [2,3,3,2,3,1]
    ], 4),
    ([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]], 14),
])
def test(heightMap, expected):
    print()
    assert expected == Solution().trapRainWater(heightMap)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
