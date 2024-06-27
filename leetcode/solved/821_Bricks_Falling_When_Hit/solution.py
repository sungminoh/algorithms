#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an m x n binary grid, where each 1 represents a brick and 0 represents an empty space. A brick is stable if:

	It is directly connected to the top of the grid, or
	At least one other brick in its four adjacent cells is stable.

You are also given an array hits, which is a sequence of erasures we want to apply. Each time we want to erase the brick at the location hits[i] = (rowi, coli). The brick on that location (if it exists) will disappear. Some other bricks may no longer be stable because of that erasure and will fall. Once a brick falls, it is immediately erased from the grid (i.e., it does not land on other stable bricks).

Return an array result, where each result[i] is the number of bricks that will fall after the ith erasure is applied.

Note that an erasure may refer to a location with no brick, and if it does, no bricks drop.

Example 1:

Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
Output: [2]
Explanation: Starting with the grid:
[[1,0,0,0],
 [1,1,1,0]]
We erase the underlined brick at (1,0), resulting in the grid:
[[1,0,0,0],
 [0,1,1,0]]
The two underlined bricks are no longer stable as they are no longer connected to the top nor adjacent to another stable brick, so they will fall. The resulting grid is:
[[1,0,0,0],
 [0,0,0,0]]
Hence the result is [2].

Example 2:

Input: grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
Output: [0,0]
Explanation: Starting with the grid:
[[1,0,0,0],
 [1,1,0,0]]
We erase the underlined brick at (1,1), resulting in the grid:
[[1,0,0,0],
 [1,0,0,0]]
All remaining bricks are still stable, so no bricks fall. The grid remains the same:
[[1,0,0,0],
 [1,0,0,0]]
Next, we erase the underlined brick at (1,0), resulting in the grid:
[[1,0,0,0],
 [0,0,0,0]]
Once again, all remaining bricks are still stable, so no bricks fall.
Hence the result is [0,0].

Constraints:

	m == grid.length
	n == grid[i].length
	1 <= m, n <= 200
	grid[i][j] is 0 or 1.
	1 <= hits.length <= 4 * 104
	hits[i].length == 2
	0 <= xi <= m - 1
	0 <= yi <= n - 1
	All (xi, yi) are unique.
"""
from typing import List
import pytest
import sys
import json
from pathlib import Path


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        """TLE"""
        M, N = len(grid), len(grid[0])

        def iter_neighbors(i, j):
            for dx, dy in ((-1,0), (1,0), (0,1), (0,-1)):
                x, y = i+dx, j+dy
                if 0<=x<M and 0<=y<N:
                    yield x, y

        seen = set()
        def dfs_stable(i, j):
            if i == 0:
                return True
            ret = False
            for x, y in iter_neighbors(i, j):
                if grid[x][y] == 1 and x*M+y not in seen:
                    seen.add(x*M+y)
                    ret |= dfs_stable(x, y)
                    seen.remove(x*M+y)
            return ret

        def dfs_remove(i, j):
            grid[i][j] = 0
            ret = 1
            for x, y in iter_neighbors(i, j):
                if grid[x][y] == 1 and x*M+y not in seen:
                    seen.add(x*M+y)
                    ret += dfs_remove(x, y)
                    seen.remove(x*M+y)
            return ret

        ret = []
        for i, j in hits:
            if grid[i][j] == 0:
                ret.append(0)
            else:
                grid[i][j] = 0
                cnt = 0
                for x, y in iter_neighbors(i, j):
                    if grid[x][y] and not dfs_stable(x, y):
                        cnt += dfs_remove(x, y)
                ret.append(cnt)
        return ret

    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        """Apr 15, 2024 22:28"""
        reverse_hits = []
        for i, j in hits:
            if grid[i][j] == 1:
                grid[i][j] = 0
                reverse_hits.append((i, j))
            else:
                reverse_hits.append(None)
        reverse_hits.reverse()

        M, N = len(grid), len(grid[0])

        def iter_neighbors(i, j):
            for dx, dy in ((-1,0), (0,-1), (0,1), (1,0)):
                x, y = i+dx, j+dy
                if 0<=x<M and 0<=y<N:
                    yield x, y

        class UnionFind:
            def __init__(self) -> None:
                self.parent = {}
                self.rank = {}

            def find(self, x):
                if x not in self.parent:
                    self.parent[x] = x
                    self.rank[x] = 1
                stack = []
                while x != self.parent[x]:
                    stack.append(x)
                    x = self.parent[x]
                while stack:
                    y = stack.pop()
                    self.parent[y] = x
                return x

            def union(self, a, b):
                pa = self.find(a)
                pb = self.find(b)
                if pa == pb:
                    return
                p, c = sorted([pa, pb])
                self.parent[c] = p
                self.rank[p] += self.rank[c]

        uf = UnionFind()

        seen = set()
        def dfs(i, j):
            for x, y in iter_neighbors(i, j):
                if grid[x][y] == 1 and (x, y) not in seen:
                    seen.add((x, y))
                    uf.union((i, j), (x, y))
                    dfs(x, y)
            return uf.find((i, j))

        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1 and (i, j) not in seen:
                    seen.add((i, j))
                    dfs(i, j)

        STABLE = (0, -1)
        for j in range(N):
            if grid[0][j] == 1:
                uf.union(STABLE, (0, j))

        ret = []
        stable_count = uf.rank.get(STABLE, 1)
        for ij in reverse_hits:
            if ij is None:
                ret.append(0)
                continue
            i, j = ij
            grid[i][j] = 1
            if i == 0:
                uf.union(STABLE, (i, j))
            for x, y in iter_neighbors(i, j):
                if grid[x][y] == 1:
                    uf.union((i, j), (x, y))
            new_stable_count = uf.rank.get(STABLE, 1)
            ret.append(max(0, new_stable_count - stable_count - 1))
            stable_count = new_stable_count

        return ret[::-1]


@pytest.mark.parametrize('args', [
    (([[1,0,0,0],
       [1,1,1,0]], [[1,0]], [2])),
    (([[1,0,0,0],
       [1,1,0,0]], [[1,1],[1,0]], [0,0])),
    (([[1],[1],[1],[1],[1]], [[3,0],[4,0],[1,0],[2,0],[0,0]], [1,0,1,0,0])),
    (([[1,0,1],
       [1,1,1]], [[0,0],[0,2],[1,1]], [0, 3, 0])),
    (([[1,0,1],[0,0,1]], [[1,0],[0,0]], [0, 0])),
    (([[0,1,1,1,1],
       [1,1,1,1,0],
       [1,1,1,1,0],
       [0,0,1,1,0],
       [0,0,1,0,0],
       [0,0,1,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0]],
      [[6,0],[1,0],[4,3],[1,2],[7,1],[6,3],[5,2],[5,1],[2,4],[4,4],[7,3]],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])),
    (([[1,0,1,1,1,1,0,1,1,1,0,0,1,0,1,1,1,1,0,0,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,0,0,1,1,1,1,1,1,1,1,0,1,1,1,1],[0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,0,1,1,1],[0,1,1,1,0,0,1,1,1,1,1,0,1,0,0,1,1,0,1,1,0,1,1,1,0,1,1,1,1,0,0,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1],[1,0,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0],[1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,1,0,1,1,1,1,0,1,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1],[1,0,1,1,0,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,1,0,1,1,0,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,0,0,1],[1,1,1,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0],[1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1],[1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,0,1,1],[0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1],[1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,0,1,1,1,1,1,0,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1],[1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,1,1,1,1,1,0,1,0,0,1],[0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,0,0,1,1,1,1,1,1,0,1,0,1,1,1,0,0,1,1,0,1,1,1,0],[1,1,0,1,1,0,1,1,0,1,1,1,0,1,0,0,1,1,1,1,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1],[0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,1,1,0,1,1,0,1,0,0,0,1],[0,1,0,1,0,0,1,1,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1],[0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,1,1,0,0,0,0,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0,0,1,0,1,0,1,1,1,1,1,0,1,1],[1,0,0,1,0,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1,1,1],[1,0,0,1,0,1,0,0,0,1,0,1,1,0,1,0,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1],[1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,0,1,0,1,1,1,1,1,1,1,0,0,1,1,1,0,0,1],[0,0,1,1,1,1,1,0,1,1,0,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,1,1,1,1,1,0,0,1,1,1,0,1,1,1],[1,1,1,0,1,0,0,1,0,0,0,1,1,1,0,0,0,0,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,1,0,1,0,1,1,0,1,1,1,1,1,1,1],[1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0,1,0,1,1,1,0,1,1,0,0,1,1,0,1,1,0,1,0,1,1,1,0,0,1,0,1,1,1,1,1,1,0,0,1],[0,1,0,1,1,1,1,1,0,1,1,0,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1,1,1,0,1,1,1,1,0,0,0,1,1,1,1,1,1,0,1,0,1,1,1,0,1,0],[1,1,1,0,1,1,1,0,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1],[1,1,1,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1],[1,1,0,1,1,0,0,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,1,1,1,0,1,0,1,0,0,1,0,1,1,0,0,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,1,1,0,0,1,1,1,1,0,1,1,0,1,1,1],[1,1,0,1,1,0,1,1,1,1,1,0,1,0,1,1,0,1,1,1,0,1,1,1,0,1,0,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0],[0,1,1,0,1,1,1,0,1,1,1,1,0,1,1,0,1,0,0,1,0,0,1,1,1,1,1,0,1,1,1,0,1,0,0,0,1,1,0,1,1,1,1,0,0,0,0,0,1,1,0,1],[1,0,1,0,1,0,0,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,1,0,1,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,0,0,1,1],[0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1,0,1,0,0,1,1,1,1,0,1],[1,1,0,0,1,0,1,1,1,0,1,1,0,0,1,1,1,1,1,0,1,1,1,1,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,1,1],[1,1,1,1,0,1,1,0,0,0,0,1,0,0,1,0,1,1,1,0,0,1,0,0,0,0,0,0,1,1,0,1,1,1,0,1,0,0,1,0,0,0,1,1,1,1,0,1,1,0,1,1],[1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,1,0,1,1,1,1,0,1,1,0,0,1,1,0,1,0,1,1,1,0,1,1,0,1,1,0,0,1,1,1,1,1,1,1,1,1],[1,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,1,1,1,0,1,0,0,1,1,1,1,0,0,1,1,1,0,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,0,1,0,1],[1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,1,1],[1,1,0,0,1,1,0,1,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,1,1,1,1],[1,0,1,0,0,1,1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,0,1,0,0,1,1,1,0,0,1,1],[1,0,1,1,1,0,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1,0,0,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,1,1,1,0,1,0,1,0,1,1,1,0],[0,1,0,0,1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1,0,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,0,0,1,1,1,1,0,1,1,1],[0,1,0,0,1,1,1,1,1,1,0,0,0,1,0,1,1,0,0,0,0,1,1,1,1,1,1,0,1,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1,1,1,1,1,1,1,0],[0,1,1,0,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1,1],[1,0,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,1,1,0,0,1,1,1,1,1,0,0,1],[0,0,1,1,1,1,1,1,1,0,1,1,0,0,1,0,1,1,0,1,1,1,1,0,1,1,1,0,1,0,0,0,1,1,0,0,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,1],[1,1,0,1,1,0,1,1,1,1,1,1,0,1,0,0,1,1,1,0,1,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,0,0,0],[1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,1],[1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,1,1,0,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,0,0,1,1,1,1,1,1,1],[0,0,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,1,1,1,1,1,1,0,1,0,0,0,1,0,0,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1,1],[0,1,1,1,0,1,1,0,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1],[0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1],[1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,0,1,0,0,0,1,0,0,1,0,0,1,0,1,1,0,0,1,0,1,1,1,0,1,0,1,1,1,1],[1,1,0,1,1,0,1,1,0,1,0,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,0,1,1,1],[0,1,0,0,1,0,1,1,1,1,1,0,1,1,0,0,1,1,0,1,1,0,0,0,0,1,0,1,1,0,1,0,0,1,1,1,0,0,1,0,0,1,1,1,0,0,1,1,0,0,1,1],[1,0,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,1,0,0,1,0,1,1,0,1,1,1,1,1,0,1,0,0,1,0,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1]],
      [[3,19],[15,10],[31,31],[25,27],[21,2],[5,13],[44,39],[27,14],[7,43],[41,38],[1,30],[24,22],[50,27],[18,6],[45,20],[17,14],[5,47],[13,46],[19,20],[49,1],[29,9],[4,25],[17,26],[46,16],[32,48],[31,7],[51,25],[3,44],[35,27],[54,1],[6,34],[18,28],[16,24],[47,17],[53,16],[5,7],[28,4],[46,15],[0,22],[12,1],[49,51],[3,41],[35,1],[54,4],[23,7],[4,21],[49,14],[51,22],[39,31],[33,40],[55,16],[44,47],[16,6],[26,8],[0,49],[27,16],[36,29],[29,27],[12,43],[50,25],[41,8],[34,27],[35,19],[48,4],[46,3],[27,31],[37,1],[30,11],[29,17],[1,4],[35,41],[12,12],[5,35],[15,26],[52,20],[38,30],[21,12],[38,38],[8,39],[14,20],[8,46],[16,51],[49,24],[23,26],[5,15],[3,50],[25,4],[10,27],[11,7],[33,17],[47,13],[20,39],[2,40],[50,39],[37,29],[19,10],[25,12],[47,48],[39,45],[52,42],[16,28],[29,21],[41,5],[40,7],[35,9],[47,15],[37,37],[24,1],[39,15],[47,36],[2,23],[16,17],[51,20],[23,18],[8,1],[26,46],[37,38],[20,27],[11,27],[13,14],[51,1],[13,4],[37,19],[35,35],[53,30],[7,24],[53,51],[49,44],[40,6],[10,8],[54,16],[32,23],[55,4],[25,44],[1,48],[33,37],[39,29],[34,14],[6,8],[12,14],[14,1],[16,21],[32,27],[1,3],[46,1],[4,16],[8,51],[32,26],[13,35],[44,46],[19,19],[18,24],[34,33],[9,18],[48,24],[44,27],[32,44],[33,4],[28,36],[41,51],[30,33],[31,11],[21,41],[37,12],[1,1],[15,1],[37,50],[17,18],[20,16],[42,14],[7,26],[14,7],[4,22],[10,42],[39,51],[33,5],[27,0],[28,18],[50,15],[2,28],[46,39],[29,50],[23,23],[31,3],[43,1],[32,41],[28,9],[7,50],[20,40],[44,17],[0,21],[9,11],[18,43],[21,4],[10,35],[23,32],[53,15],[53,34],[25,45],[53,38],[14,50],[14,42],[5,16],[19,30],[21,28],[52,8],[4,12],[54,3],[18,4],[34,43],[3,42],[55,19],[42,44],[48,8],[15,22],[38,13],[26,18],[11,32],[24,47],[32,19],[9,41],[53,49],[40,27],[31,18],[21,27],[50,42],[3,48],[16,8],[45,45],[43,46],[17,17],[7,20],[16,19],[48,38],[49,31],[22,15],[32,21],[0,1],[49,37],[12,9],[53,10],[40,26],[43,5],[19,18],[39,28],[28,31],[23,13],[45,31],[0,23],[39,33],[23,42],[12,26],[26,45],[10,34],[4,35],[20,2],[45,51],[13,34],[7,19],[38,0],[51,44],[25,34],[42,31],[46,28],[44,45],[34,42],[41,48],[42,15],[24,2],[19,7],[26,41],[41,20],[28,34],[35,10],[38,16],[41,0],[29,10],[52,26],[47,24],[3,38],[33,32],[41,34],[38,10],[18,1],[31,43],[27,34],[1,27],[38,1],[37,24],[21,18],[12,49],[30,17],[32,51],[2,20],[8,47],[23,3],[52,27],[24,14],[17,3],[36,25],[45,39],[32,29],[2,19],[15,38],[41,16],[38,24],[13,47],[55,9],[39,49],[11,16],[0,47],[2,38],[39,0],[34,8],[54,49],[33,35],[31,21],[26,33],[39,1],[55,51],[20,42],[11,19],[34,45],[14,22],[5,46],[44,33],[14,45],[54,37],[28,28],[27,11],[40,46],[52,39],[37,45],[21,49],[12,39],[34,6],[43,4],[21,15],[52,32],[40,0],[37,22],[45,18],[24,24],[4,42],[17,10],[40,4],[52,40],[32,15],[37,4],[19,33],[47,38],[0,26],[47,42],[42,0],[53,3],[47,25],[2,31],[42,30],[4,36],[50,41],[27,40],[53,28],[42,47],[6,12],[3,26],[46,14],[7,35],[36,27],[7,47],[7,27],[38,37],[27,22],[39,10],[30,10],[43,21],[19,23],[2,27],[0,35],[4,23],[9,37],[1,38],[41,12],[24,3],[13,0],[16,27],[1,26],[20,30],[13,48],[17,1],[49,22],[27,45],[37,23],[4,17],[21,35],[18,0],[33,41],[12,0],[10,17],[41,37],[9,31],[14,3],[0,31],[49,5],[54,47],[50,48],[28,15],[30,6],[0,33],[55,36],[31,30],[15,39],[37,0],[31,41],[54,22],[41,47],[17,34],[50,8],[7,51],[41,28],[20,4],[22,13],[31,28],[29,4],[5,20],[12,4],[14,25],[46,11],[6,28],[45,33],[14,43],[47,49],[18,18],[9,40],[33,13],[14,19],[0,13],[39,19],[31,34],[37,8],[45,28],[7,36],[6,40],[43,51],[9,51],[49,33],[52,35],[17,5],[26,51],[9,49],[50,17],[53,7],[27,38],[18,34],[4,37],[32,2],[44,20],[29,20],[13,6],[12,5],[5,32],[44,43],[18,8],[49,50],[36,3],[35,34],[38,11],[12,27],[27,42],[49,17],[36,11],[7,44],[18,35],[34,48],[45,34],[8,43],[34,30],[50,31],[28,19],[12,17],[38,23],[38,22],[40,9],[35,22],[38,5],[43,9],[29,40],[39,22],[55,27],[2,45],[3,16],[42,45],[40,5],[54,36],[54,11],[7,45],[49,30],[45,8],[30,18],[48,42],[10,7],[15,2],[35,46],[44,23],[14,35],[32,3],[20,49],[24,0],[44,44],[7,33],[55,23],[43,32],[7,9],[19,26],[0,14],[44,37],[8,49],[49,10],[3,22],[52,16],[50,6],[8,25],[6,30],[8,48],[29,11],[38,49],[34,23],[27,28],[44,36],[27,41],[27,24],[8,7],[14,34],[24,42],[31,36],[51,9],[50,14],[51,29],[28,44],[11,17],[18,42],[31,45],[50,32],[42,17],[26,13],[43,10],[20,11],[46,40],[26,5],[48,0],[30,35],[23,34],[3,17],[7,8],[25,39],[39,50],[51,21],[0,43],[5,3],[20,47],[6,23],[2,24],[25,8],[1,41],[17,40],[24,43],[48,12],[7,12],[13,39],[47,34],[29,19],[3,25],[44,29],[47,51],[44,3],[6,36],[19,5],[14,26],[36,14],[34,51],[53,48],[14,40],[51,16],[45,16],[5,38],[37,6],[4,33],[54,12],[35,16],[19,36],[13,15],[42,1],[41,33],[25,43],[7,22],[47,46],[35,23],[2,34],[6,37],[6,48],[8,50],[39,34],[18,26],[2,32],[8,20],[44,19],[0,24],[5,50],[42,28],[35,0],[15,11],[32,7],[38,33],[31,2],[9,12],[30,32],[11,46],[31,40],[34,4],[38,39],[29,48],[0,15],[1,42],[4,19],[54,32],[52,11],[22,26],[12,32],[3,23],[22,27],[2,8],[32,28],[33,21],[2,48],[50,19],[22,47],[46,5],[9,8],[44,31],[35,48],[27,19],[15,15],[19,22],[30,40],[52,3],[6,9],[26,3],[12,16],[53,9],[16,14],[3,13],[33,47],[48,36],[8,34],[7,49],[42,22],[1,50],[47,26],[54,10],[4,30],[19,42],[52,29],[3,1],[17,9],[25,1],[38,34],[0,7],[3,46],[3,15],[18,48],[9,20],[49,20],[28,23],[18,33],[46,34],[34,36],[40,16],[13,20],[20,50],[44,22],[44,0],[32,1],[39,8],[4,34],[53,4],[10,13],[29,51],[45,1],[34,7],[20,46],[38,21],[52,34],[49,49],[8,37],[45,9],[41,26],[1,36],[55,5],[25,49],[33,34],[45,41],[54,39],[34,50],[47,30],[14,36],[40,35],[4,43],[46,36],[55,2],[0,30],[31,17],[31,26],[14,6],[48,43],[28,49],[26,32],[46,2],[44,1],[49,6],[52,0],[30,51],[44,51],[18,22],[5,14],[27,26],[45,27],[13,31],[51,5],[42,39],[27,29],[43,48],[7,18],[26,21],[21,7],[39,25],[26,4],[26,23],[12,6],[10,2],[51,27],[50,49],[15,33],[31,42],[47,10],[10,39],[33,30],[33,16],[32,32],[8,42],[46,24],[19,35],[29,16],[21,30],[1,31],[51,48],[16,36],[6,21],[47,18],[27,23],[53,35],[54,8],[18,17],[28,32],[49,45],[48,10],[2,49],[12,51],[30,2],[8,17],[18,25],[42,35],[40,2],[23,35],[29,30],[53,1],[51,47],[26,36],[2,1],[2,11],[27,27],[54,7],[12,28],[45,25],[9,19],[5,19],[30,14],[27,30],[31,33],[53,47],[22,25],[46,21],[2,42],[29,18],[18,10],[55,6],[25,13],[28,10],[28,2],[9,35],[5,51],[9,0],[22,49],[36,6],[47,22],[21,42],[39,6],[44,26],[51,45],[23,2],[28,37],[43,43],[37,18],[9,23],[9,47],[31,13],[39,7],[30,28],[5,6],[17,28],[21,48],[37,13],[11,36],[14,0],[13,19],[26,39],[20,1],[16,11],[19,8],[11,24],[9,17],[23,21],[17,4],[12,19],[22,2],[25,6],[10,31],[22,28],[52,43],[48,27],[40,33],[35,43],[4,39],[40,1],[42,13],[45,3],[37,35],[30,0],[2,43],[55,40],[51,26],[49,18],[34,34],[40,44],[54,5],[33,29],[8,24],[55,33],[12,13],[43,35],[38,50],[37,25],[10,0],[21,5],[10,50],[48,49],[50,33],[32,10],[10,51],[40,37],[37,49],[28,33],[24,19],[36,43],[20,29],[11,14],[40,14],[18,21],[39,17],[31,14],[51,33],[10,5],[21,31],[15,42],[2,6],[41,36],[34,19],[48,21],[25,19],[55,31],[22,24],[13,10],[48,6],[23,49],[36,31],[55,25],[27,47],[17,51],[33,11],[21,22],[12,41],[2,21],[54,50],[20,48],[8,44],[13,45],[52,28],[3,7],[13,16],[54,30],[24,33],[35,50],[55,37],[1,28],[14,10],[16,32],[30,3],[28,25],[52,18],[20,22],[52,13],[14,28],[55,29],[10,30],[3,43],[36,45],[9,34],[54,31],[22,1],[1,49],[33,22],[44,25],[23,37],[30,1],[21,36],[22,32],[38,47],[22,44],[55,49],[22,36],[14,15],[43,36],[41,39],[44,7],[18,29],[22,19],[12,23],[16,29],[36,17],[15,9],[26,1],[19,16],[33,6],[17,35],[37,31],[0,19],[49,26],[11,11],[9,36],[13,12],[46,47],[55,15],[6,7],[55,46],[41,6],[11,41],[48,23],[48,44],[20,31],[23,51],[2,3],[30,15],[7,29],[6,38],[29,32],[33,15],[1,34],[31,46],[31,23],[35,24],[42,36],[54,43],[55,32],[5,42],[42,12],[9,38],[26,0],[24,41],[7,38],[6,14],[25,30],[6,20],[35,45],[53,36],[37,51],[26,9],[32,43],[26,34],[21,14],[20,0],[7,46],[23,10],[41,15],[44,41],[43,38],[20,36],[32,9],[29,12],[40,15],[46,25],[42,46],[39,24],[50,10],[18,46],[35,26],[43,30],[20,5],[24,16],[14,30],[19,0],[1,32],[6,32],[34,2],[52,6],[25,29],[9,29],[8,19],[4,7],[29,0],[28,50],[20,7],[15,21],[34,47],[0,34],[20,6],[51,30],[42,51],[39,46],[42,41],[16,18],[34,20],[19,6],[52,10],[5,4],[12,44],[17,15],[54,41],[20,12],[7,10],[15,18],[25,20],[3,36],[21,13],[22,33],[20,34],[2,33],[32,46],[21,11],[27,5],[50,23],[3,51],[45,4],[3,21],[6,42],[17,30],[3,34],[53,25],[1,43],[32,38],[22,35],[23,24],[43,24],[7,7],[39,30],[17,29],[19,37],[10,24],[32,50],[44,13],[46,12],[4,1],[55,47],[22,9],[13,9],[18,11],[19,13],[53,41],[1,21],[50,9],[18,40],[4,0],[16,10],[16,25],[50,38],[9,21],[33,36],[53,40],[6,4],[19,50],[6,0],[38,43],[9,16],[16,5],[6,39],[7,48],[49,39],[46,51],[54,20],[43,0],[31,50],[28,12],[0,27],[13,42],[19,28],[41,27],[10,23],[41,49],[39,36],[44,32],[9,3],[34,35],[26,11],[46,18],[37,46],[48,32],[29,28],[55,43],[17,50],[16,1],[38,18],[24,18],[45,12],[50,44],[13,50],[36,46],[28,17],[37,48],[7,41],[1,14],[23,8],[21,39],[48,1],[16,38],[35,36],[32,49],[15,32],[30,12],[24,40],[36,33],[16,3],[26,29],[32,45],[54,40],[13,1],[28,0],[30,8],[31,24],[4,3],[33,9],[43,31],[19,41],[22,43],[0,46],[53,22],[33,44],[28,51],[46,50],[6,29],[49,42],[24,31],[11,5],[20,17],[31,5],[31,35],[52,37],[1,12],[19,49],[8,32],[15,48],[42,4],[51,35],[33,2],[42,26],[15,4],[13,5],[32,47],[3,30],[21,43],[27,2],[43,25],[55,28],[25,14],[19,38],[46,17],[19,1],[1,5],[2,30],[41,23],[38,8],[45,26],[30,49],[24,26],[11,10],[43,23],[51,41],[45,23],[22,10],[30,19],[51,34],[16,15],[34,31],[8,4],[29,2],[23,5],[1,45],[0,39],[36,8],[9,32],[31,8],[1,51],[55,41],[31,12],[26,43],[26,2],[29,35],[37,39],[43,42],[31,1],[52,9],[26,44],[35,39],[32,31],[36,0],[20,45],[25,41],[37,21],[16,4],[6,5],[30,34],[4,29],[25,31],[32,40],[8,41],[31,29],[7,6],[1,40],[55,1],[35,15],[2,51],[27,6],[33,51],[31,4],[18,50],[48,11],[41,1],[17,45],[44,28],[49,4],[28,16],[10,16],[10,37],[36,24],[33,25],[5,44],[54,35],[40,48],[0,8],[12,47],[36,4],[38,9],[33,39],[6,16],[9,6],[55,12],[29,13],[53,11],[47,14],[24,38],[28,22],[54,42],[45,46],[30,9],[48,26],[29,47],[21,33],[8,5],[13,22],[49,32],[11,30],[14,29],[41,19],[39,44],[29,36],[3,47],[20,14],[39,14],[25,21],[28,38],[48,15],[41,25],[40,21],[9,39],[12,22],[25,37],[14,12],[24,35],[6,45],[28,40],[15,16],[36,39],[12,21],[46,0],[13,43],[5,37],[25,2],[5,39],[7,0],[50,47],[25,50],[43,49],[11,6],[49,38],[11,25],[6,22],[18,38],[49,40],[37,9],[24,44],[45,24],[19,2],[33,0],[34,13],[47,20],[55,18],[8,2],[45,50],[48,20],[55,3],[25,33],[11,45],[37,43],[0,0],[22,40],[50,30],[0,6],[54,38],[20,18],[55,21],[7,32],[36,16],[1,9],[6,31],[43,40],[49,16],[50,3],[16,13],[11,15],[47,27],[30,41],[18,44],[43,18],[30,31],[13,13],[44,49],[35,40],[45,42],[16,48],[8,45],[32,25],[21,26],[16,41],[42,10],[22,8],[9,4],[29,39],[10,46],[50,36],[27,4],[3,32],[11,18],[2,47],[44,21],[25,32],[10,45],[42,21],[33,38],[45,10],[11,51],[5,25],[36,30],[32,13],[50,29],[26,38],[36,41],[54,2],[17,6],[42,43],[15,50],[16,40],[20,28],[45,0],[32,18],[20,20],[40,42],[18,30],[22,14],[21,37],[17,47],[15,24],[24,29],[27,3],[47,41],[15,19],[11,0],[0,44],[37,40],[16,43],[29,34],[13,17],[32,12],[14,18],[27,17],[45,22],[9,7],[29,41],[37,20],[28,41],[19,21],[28,8],[44,6],[32,42],[34,26],[8,33],[39,12],[27,49],[8,14],[14,38],[23,12],[26,40],[41,7],[11,28],[49,46],[51,37],[6,2],[29,3],[17,8],[40,23],[36,2],[33,43],[4,38],[24,10],[24,45],[18,2],[39,43],[43,34],[37,41],[21,20],[6,11],[25,40],[23,16],[7,14],[0,16],[29,14],[5,10],[48,31],[51,10],[5,49],[41,32],[53,12],[11,20],[39,48],[2,0],[35,21],[2,13],[25,47],[17,46],[2,16],[7,1],[40,8],[3,5],[47,39],[18,14],[41,17],[0,4],[50,37],[10,20],[55,34],[23,31],[45,30],[31,32],[18,49],[35,6],[10,14],[31,19],[55,7],[12,50],[39,16],[37,2],[24,46],[48,45],[40,20],[51,39],[28,42],[0,2],[13,3],[3,40],[54,15],[2,5],[34,9],[32,34],[35,49],[27,33],[36,13],[22,51],[54,48],[27,15],[46,49],[11,49],[15,27],[36,47],[2,7],[30,29],[27,39],[37,47],[9,9],[46,33],[47,1],[17,37],[1,46],[3,0],[9,33],[34,0],[43,37],[3,35],[54,14],[43,39],[33,45],[41,22],[34,29],[3,11],[19,4],[42,32],[38,31],[8,10],[3,20],[29,6],[28,35],[38,46],[43,27],[23,28],[38,6],[55,24],[16,20],[39,38],[0,51],[30,23],[30,47],[35,4],[21,8],[37,30],[2,36],[28,26],[16,47],[53,43],[35,20],[12,20],[29,25],[46,20],[23,46],[21,51],[28,30],[25,17],[51,7],[0,11],[33,33],[5,29],[30,30],[39,42],[46,9],[50,13],[28,20],[38,7],[16,33],[36,20],[36,22],[13,29],[7,3],[19,14],[15,34],[35,3],[21,10],[26,49],[40,32],[25,0],[44,24],[7,34],[35,12],[31,0],[15,37],[38,29],[51,4],[54,46],[43,6],[7,42],[50,4],[23,25],[26,20],[12,2],[17,16],[36,23],[29,44],[14,49],[42,20],[22,4],[6,1],[8,9],[38,28],[4,28],[55,20],[30,4],[9,22],[30,43],[1,19],[34,40],[37,26],[44,2],[34,37],[27,48],[14,46],[14,37],[26,16],[23,48],[24,13],[30,27],[49,9],[41,43],[28,27],[20,32],[41,9],[28,7],[40,51],[15,29],[50,16],[50,51],[34,21],[19,46],[17,0],[12,31],[15,8],[34,1],[13,11],[34,17],[26,14],[20,24],[39,40],[22,5],[54,18],[25,38],[47,8],[44,9],[47,3],[46,35],[38,35],[54,34],[38,32],[40,19],[12,33],[41,18],[39,9],[26,30],[49,0],[44,12],[4,32],[22,46],[9,15],[2,9],[51,43],[9,5],[6,17],[13,37],[53,18],[12,11],[31,51],[32,8],[11,34],[39,13],[22,39],[22,18],[7,21],[55,44],[36,9],[6,35],[36,15],[0,18],[0,25],[52,44],[10,40],[40,41],[47,29],[24,7],[22,37],[34,16],[4,40],[43,3],[3,18],[11,29],[44,50],[11,50],[55,45],[5,41],[45,37],[44,30],[41,3],[43,50],[51,51],[8,40],[5,8],[20,51],[42,23],[50,24],[11,44],[14,31],[2,18],[32,37],[14,11],[11,2],[15,36],[2,2],[13,21],[10,15],[37,33],[17,33],[44,34],[46,26],[21,25],[1,33],[48,17],[55,22],[15,12],[12,10],[25,5],[32,6],[11,35],[26,25],[48,35],[43,29],[24,12],[50,45],[3,39],[30,25],[22,21],[6,51],[21,3],[31,10],[12,36],[45,7],[38,51],[54,13],[6,47],[42,19],[34,3],[25,23],[0,9],[38,40],[14,39],[25,48],[46,32],[11,21],[8,8],[10,22],[24,32],[18,51],[41,10],[54,26],[4,44],[50,35],[34,49],[40,38],[4,6],[52,47],[37,42],[6,6],[26,6],[51,24],[34,38],[48,47],[0,42],[29,8],[36,5],[54,51],[50,1],[11,38],[27,12],[49,23],[11,26],[6,15],[20,15],[46,4],[34,11],[5,30],[55,48],[39,37],[5,43],[35,17],[17,21],[48,46],[46,46],[27,50],[49,28],[53,17],[1,23],[39,2],[29,45],[45,49],[28,24],[17,25],[23,22],[42,38],[19,25],[36,34],[9,28],[45,36],[18,32],[1,39],[22,48],[50,5],[19,32],[36,35],[41,13],[22,38],[0,48],[45,32],[50,12],[29,31],[12,40],[34,24],[44,18],[40,34],[19,45],[46,41],[53,6],[14,47],[11,4],[51,11],[53,19],[33,1],[52,36],[52,31],[55,14],[25,46],[15,51],[47,2],[43,12],[23,20],[8,0],[2,50],[20,3],[51,42],[46,30],[24,28],[11,3],[52,38],[30,44],[47,47],[40,29],[36,32],[21,38],[46,19],[46,8],[53,50],[40,50],[52,22],[38,20],[28,6],[45,47],[22,3],[34,10],[17,43],[0,20],[41,2],[9,42],[23,43],[26,15],[17,23],[28,14],[55,30],[0,5],[40,31],[47,45],[24,11],[4,15],[20,38],[26,31],[4,49],[8,12],[50,0],[43,22],[48,22],[37,36],[25,10],[20,9],[15,25],[4,41],[19,43],[6,41],[2,17],[34,5],[29,37],[54,29],[22,45],[1,7],[54,23],[25,22],[21,44],[10,3],[5,11],[3,49],[26,35],[15,20],[50,40],[49,21],[55,11],[35,38],[12,34],[42,25],[27,43],[45,38],[51,2],[4,5],[43,20],[2,25],[17,13],[42,3],[22,0],[43,15],[38,2],[24,49],[51,18],[0,40],[45,29],[27,7],[44,48],[36,42],[20,44],[33,23],[47,6],[49,48],[44,40],[22,7],[53,31],[26,50],[55,26],[40,12],[46,10],[24,30],[23,27],[8,31],[51,38],[47,43],[23,11],[10,43],[29,49],[14,17],[28,48],[0,32],[48,48],[44,42],[51,17],[22,42],[25,26],[20,35],[33,20],[34,41],[45,2],[24,9],[17,20],[15,49],[11,1],[17,31],[17,42],[48,2],[7,2],[1,29],[33,19],[31,25],[0,28],[8,16],[7,30],[17,2],[48,7],[42,29],[35,13],[21,46],[28,29],[18,31],[24,25],[15,3],[6,46],[53,8],[31,15],[53,32],[16,23],[22,31],[44,14],[55,39],[42,48],[39,27],[46,44],[28,13],[35,37],[40,28],[51,46],[23,1],[29,42],[15,7],[50,26],[37,15],[18,12],[13,36],[2,39],[1,47],[43,44],[6,26],[51,19],[4,26],[21,47],[36,7],[42,7],[21,32],[31,44],[5,34],[12,7],[10,6],[21,17],[14,21],[4,14],[43,41],[13,24],[5,5],[4,2],[19,29],[44,38],[50,7],[16,34],[23,14],[6,18],[15,35],[27,36],[25,51],[51,6],[16,46],[29,24],[44,4],[53,0],[36,1],[16,16],[52,1],[7,15],[10,10],[38,36],[20,37],[49,11],[38,12],[22,41],[14,33],[19,39],[5,21],[29,22],[35,28],[6,49],[15,40],[9,48],[44,10],[19,3],[31,37],[20,26],[7,17],[3,24],[48,14],[21,1],[29,23],[24,23],[39,23],[19,12],[47,4],[19,44],[37,5],[54,28],[35,5],[14,24],[30,22],[20,10],[14,16],[42,18],[1,25],[21,6],[54,25],[22,6],[49,35],[33,24],[36,19],[33,3],[12,46],[4,9],[8,23],[20,33],[32,17],[33,46],[50,18],[7,37],[3,9],[48,51],[5,28],[47,16],[14,14],[14,32],[45,14],[51,36],[43,33],[32,5],[32,22],[45,43],[49,13],[15,46],[39,21],[17,24],[17,32],[41,44],[26,12],[38,25],[25,25],[5,12],[0,10],[24,21],[49,19],[32,11],[45,48],[24,51],[49,8],[10,49],[48,41],[45,17],[42,9],[17,19],[5,26],[0,37],[29,5],[53,5],[49,29],[22,23],[6,13],[13,23],[23,30],[35,31],[22,50],[34,12],[50,28],[10,47],[19,51],[42,50],[29,26],[20,41],[24,27],[30,48],[41,41],[43,26]],
      [])),
    # ((*json.load(open(Path(__file__).parent/'testcase.json')), [])),
])
def test(args):
    assert args[-1] == Solution().hitBricks(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))