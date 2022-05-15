#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Example 1:

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Example 2:

Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

Example 3:

Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.

Constraints:

	rows == heights.length
	columns == heights[i].length
	1 <= rows, columns <= 100
	1 <= heights[i][j] <= 106
"""
from heapq import heappop
from heapq import heappush
from pathlib import Path
import json
import operator
import itertools
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        DFS
        TLE
        """
        m, n = len(heights), len(heights[0])
        ret = float('inf')
        @lru_cache(None)
        def dfs(i, j, remain, d) -> int:
            nonlocal ret
            if i == m-1 and j == n-1:
                ret = min(ret, d)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                _i, _j = i+dx, j+dy
                if 0<=_i<m and 0<=_j<n:
                    bit = 1<<(_i*n + _j)
                    diff = abs(heights[i][j] - heights[_i][_j])
                    if remain&bit and diff < ret:
                        dfs(_i, _j, remain^bit, max(d, diff))

        dfs(0, 0, (1<<(m*n))-1, 0)
        return ret

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        DFS
        TLE
        """
        m, n = len(heights), len(heights[0])
        ret = float('inf')
        memo = {}
        def dfs(i, j, remain, d):
            key = (i, j, remain)
            if memo.get(key, float('inf')) <= d:
                return
            memo[key] = d
            nonlocal ret
            if i == m-1 and j == n-1:
                ret = min(ret, d)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                _i, _j = i+dx, j+dy
                if 0<=_i<m and 0<=_j<n:
                    bit = 1<<(_i*n + _j)
                    diff = abs(heights[i][j] - heights[_i][_j])
                    if remain&bit and diff < ret:
                        dfs(_i, _j, remain^bit, max(d, diff))

        dfs(0, 0, (1<<(m*n))-1, 0)
        return ret

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Binary search with dfs
        Max recursion depth exceeded
        """
        m, n = len(heights), len(heights[0])

        def diff(i, j, _i, _j):
            return abs(heights[i][j] - heights[_i][_j])

        max_diff = 0
        for i in range(m):
            for j in range(n):
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    _i, _j = i+dx, j+dy
                    if 0<=_i<m and 0<=_j<n:
                        max_diff = max(max_diff, diff(i, j, _i, _j))

        @lru_cache(None)
        def dfs(i, j, remain, k):
            if i == m-1 and j == n-1:
                return True
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                _i, _j = i+dx, j+dy
                if 0<=_i<m and 0<=_j<n:
                    bit = 1<<(_i*n + _j)
                    if remain&bit and diff(i, j, _i, _j) <= k:
                        if dfs(_i, _j, remain^bit, k):
                            return True
            return False

        def bisearch(s, e, func):
            while s <= e:
                p = s + (e-s)//2
                if func(p):
                    e = p-1
                else:
                    s = p+1
            return e+1

        return bisearch(0, max_diff, lambda k: dfs(0, 0, (1<<(m*n))-1, k))

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Binary search with dfs discarding path
        Max recursion depth exceeded
        """
        m, n = len(heights), len(heights[0])

        def diff(i, j, _i, _j):
            return abs(heights[i][j] - heights[_i][_j])

        max_diff = 0
        for i in range(m):
            for j in range(n):
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    _i, _j = i+dx, j+dy
                    if 0<=_i<m and 0<=_j<n:
                        max_diff = max(max_diff, diff(i, j, _i, _j))

        def dfs(i, j, visited, k):
            if i == m-1 and j == n-1:
                return True
            visited.add((i, j))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                _i, _j = i+dx, j+dy
                if 0<=_i<m and 0<=_j<n and (_i, _j) not in visited and diff(i, j, _i, _j) <= k:
                    if dfs(_i, _j, visited, k):
                        return True
            return False

        def bisearch(s, e, func):
            while s <= e:
                p = s + (e-s)//2
                if func(p):
                    e = p-1
                else:
                    s = p+1
            return e+1

        return bisearch(0, max_diff, lambda k: dfs(0, 0, set(), k))

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Union find with heap
        """
        m, n = len(heights), len(heights[0])

        def diff(i, j, _i, _j):
            return abs(heights[i][j] - heights[_i][_j])

        heap = []
        for i in range(m):
            for j in range(n):
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    _i, _j = i+dx, j+dy
                    if 0<=_i<m and 0<=_j<n:
                        heappush(heap, (diff(i, j, _i, _j), (i, j), (_i, _j)))

        class UnionFind:
            def __init__(self):
                self.rep = {}

            def find(self, a):
                if a not in self.rep:
                    self.rep[a] = a
                while a != self.rep[a]:
                    self.rep[a], a = self.rep[self.rep[a]], self.rep[a]
                return self.rep[a]

            def union(self, a, b):
                pa = self.find(a)
                pb = self.find(b)
                self.rep[pa] = self.rep[pb] = min(pa, pb)

        uf = UnionFind()
        while heap:
            d, p1, p2 = heappop(heap)
            uf.union(p1, p2)
            if uf.find((0, 0)) == uf.find((m-1, n-1)):
                return d
        return 0

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Dijkstra (like BFS with heap)
        """
        m, n = len(heights), len(heights[0])

        def diff(i, j, _i, _j):
            return abs(heights[i][j] - heights[_i][_j])

        heap = []
        heappush(heap, (0, (0, 0)))
        visited = set()
        while heap:
            d, (i, j) = heappop(heap)
            if i == m-1 and j == n-1:
                return d
            if (i, j) in visited:
                continue
            visited.add((i, j))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                _i, _j = i+dx, j+dy
                if 0<=_i<m and 0<=_j<n:
                    heappush(heap, (max(d, diff(i, j, _i, _j)), (_i, _j)))
        return 0


@pytest.mark.parametrize('heights, expected', [
    ([[1,2,2],[3,8,2],[5,3,5]], 2),
    ([[1,2,3],[3,8,4],[5,3,5]], 1),
    ([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]], 0),
    ([[10,8], [10,8], [1,2], [10,3], [1,3], [6,3], [5,2]], 6),
    ([[4,3,4,10,5,5,9,2], [10,8,2,10,9,7,5,6], [5,8,10,10,10,7,4,2], [5,1,3,1,1,3,1,9], [6,4,10,6,10,9,4,6]], 5),
    ([[8,3,2,5,2,10,7,1,8,9], [1,4,9,1,10,2,4,10,3,5], [4,10,10,3,6,1,3,9,8,8], [4,4,6,10,10,10,2,10,8,8], [9,10,2,4,1,2,2,6,5,7], [2,9,2,6,1,4,7,6,10,9], [8,8,2,10,8,2,3,9,5,3], [2,10,9,3,5,1,7,4,5,6], [2,3,9,2,5,10,2,7,1,8], [9,10,4,10,7,4,9,3,1,6]], 5),
    ([[1,10,6,7,9,10,4,9]], 9),
    (*json.load(open(Path(__file__).parent/'testcase.json')), 430152),
    ([[3]], 0),
])
def test(heights, expected):
    assert expected == Solution().minimumEffortPath(heights)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
