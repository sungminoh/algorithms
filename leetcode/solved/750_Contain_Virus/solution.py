#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.

The world is modeled as an m x n binary grid isInfected, where isInfected[i][j] == 0 represents uninfected cells, and isInfected[i][j] == 1 represents cells contaminated with the virus. A wall (and only one wall) can be installed between any two 4-directionally adjacent cells, on the shared boundary.

Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. Resources are limited. Each day, you can install walls around only one region (i.e., the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night). There will never be a tie.

Return the number of walls used to quarantine all the infected regions. If the world will become fully infected, return the number of walls used.

Example 1:

Input: isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
Output: 10
Explanation: There are 2 contaminated regions.
On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:

On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.

Example 2:

Input: isInfected = [[1,1,1],[1,0,1],[1,1,1]]
Output: 4
Explanation: Even though there is only one cell saved, there are 4 walls built.
Notice that walls are only built on the shared boundary of two different cells.

Example 3:

Input: isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
Output: 13
Explanation: The region on the left only builds two new walls.

Constraints:

	m == isInfected.length
	n == isInfected[i].length
	1 <= m, n <= 50
	isInfected[i][j] is either 0 or 1.
	There is always a contiguous viral region throughout the described process that will infect strictly more uncontaminated squares in the next round.
"""
from typing import List
import pytest
import sys


class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        """Apr 13, 2024 14:08"""

        class UnionFind:
            def __init__(self):
                self.d = {}

            def find(self, x):
                if x not in self.d:
                    self.d[x] = x
                while self.d.get(x) != x:
                    self.d[x] = self.find(self.d.get(x))
                    x = self.d[x]
                return x

            def union(self, *xs):
                pxs = [self.find(x) for x in xs]
                p = min(pxs)
                for px in pxs:
                    self.d[px] = p
                return p

        node_region = {}
        uf = UnionFind()

        M, N = len(isInfected), len(isInfected[0])
        def iter_neighbors(i, j):
            for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                x, y = i+dx, j+dy
                if 0<=x<M and 0<=y<N:
                    yield x, y

        class Region:
            def __init__(self, coordinates) -> None:
                self.representative = min(coordinates)
                self.nodes = set(coordinates)
                self.boundaries = set(coordinates)
                self._targets = None
                self._edges = None
                self._adjacent_regions = None
                self.blocked = False

            def update(self):
                if self.blocked:
                    return
                for i, j in self.targets:
                    isInfected[i][j] = 1
                self.boundaries = self.targets
                self.nodes.update(self.targets)
                self.representative = uf.union(self.representative, *self.targets)
                for t in self.targets:
                    node_region[t] = self

                self.reset()

            def merge_all(self, *regions):
                for r in regions:
                    self.nodes.update(r.nodes)
                    self.boundaries.update(r.boundaries)
                self.reset()

            def reset(self):
                self._targets = None
                self._edges = None
                self._adjacent_regions = None

            @property
            def edges(self):
                if self._edges is None:
                    self.peak()
                return self._edges

            @property
            def targets(self):
                if self._targets is None:
                    self.peak()
                return self._targets

            @property
            def adjacent_regions(self):
                if self._adjacent_regions is None:
                    self.peak()
                return self._adjacent_regions

            def peak(self):
                self._edges = 0
                self._targets = set()
                self._adjacent_regions = []
                for i, j in self.boundaries:
                    for x, y in iter_neighbors(i, j):
                        if isInfected[x][y] == 0:
                            self._edges += 1
                            self._targets.add((x, y))
                        r = get_region((x, y))
                        if r and not r.blocked:
                            self._adjacent_regions.append(r)

        def get_region(coordinate):
            repre = uf.find(coordinate)
            if repre not in node_region:
                return None
            r = node_region[repre]
            return node_region[uf.find(r.representative)]

        def bfs(i, j):
            q = []
            if isInfected[i][j] == 1:
                isInfected[i][j] = -1
                q.append((i, j))
            while q:
                _q = []
                for i, j in q:
                    yield (i, j)
                    for x, y in iter_neighbors(i, j):
                        if isInfected[x][y] == 1:
                            isInfected[x][y] = -1
                            _q.append((x, y))
                q = _q

        regions = []
        for i in range(M):
            for j in range(N):
                infected_coordinates = list(bfs(i, j))
                if infected_coordinates:
                    r = Region(infected_coordinates)
                    regions.append(r)
                    for coordinate in infected_coordinates:
                        node_region[coordinate] = r
                    uf.union(*infected_coordinates)

        def print_mat():
            print('--------------------')
            for i in range(M):
                for j in range(N):
                    if isInfected[i][j] == 0:
                        print(0, end=' ')
                    else:
                        r = get_region((i, j))
                        if r.blocked:
                            print(2, end=' ')
                        else:
                            print(1, end=' ')
                print()
            print('--------------------')


        ret = 0
        while regions:
            # block
            r = max(regions, key=lambda x: len(x.targets))
            r.blocked = True
            ret += r.edges
            # update
            for r in regions:
                r.update()
            # merge
            for r in regions:
                repre = uf.union(r.representative, *[_r.representative for _r in r.adjacent_regions])
                get_region(repre).merge_all(r, *r.adjacent_regions)
            # next
            representatives = set(uf.find(r.representative) for r in regions if not r.blocked)
            regions = [get_region(repre) for repre in representatives]
            # print_mat()
        return ret


@pytest.mark.parametrize('args', [
    (([[0,1,0,0,0,0,0,1],
       [0,1,0,0,0,0,0,1],
       [0,0,0,0,0,0,0,1],
       [0,0,0,0,0,0,0,0]], 10)),
    (([[1,1,1],[1,0,1],[1,1,1]], 4)),
    (([[1,1,1,0,0,0,0,0,0],
       [1,0,1,0,1,1,1,1,1],
       [1,1,1,0,0,0,0,0,0]], 13)),
    (([[0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0],
       [1,0,0,0,0,0,0,0,0,0],
       [0,0,1,0,0,0,1,0,0,0],
       [0,0,0,0,0,0,1,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,1,0],
       [0,0,0,0,1,0,1,0,0,0],
       [0,0,0,0,0,0,0,0,0,0]], 56)),
])
def test(args):
    assert args[-1] == Solution().containVirus(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
