#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.

Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.

Example 3:

Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.

Constraints:

	1 <= stones.length <= 1000
	0 <= xi, yi <= 104
	No two stones are at the same coordinate point.
"""
from collections import deque
from collections import defaultdict
from heapq import heappop, heappush
from typing import List
import pytest
import sys


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """05/29/2020 00:14
        Incorrect
        """
        stones = {tuple(p) for p in stones}
        def find_min():
            p = None
            m = float('inf')
            for i, (x, y) in enumerate(stones):
                overlaps = len(xp[x].union(yp[y])) - 1
                if 0 < overlaps < m:
                    m = overlaps
                    p = (x, y)
            return p

        def remove_stone(p):
            xp[p[0]].remove(p)
            yp[p[1]].remove(p)
            stones.remove(p)

        xp = defaultdict(set)
        yp = defaultdict(set)

        for i, p in enumerate(stones):
            xp[p[0]].add(p)
            yp[p[1]].add(p)

        cnt = 0
        while True:
            p = find_min()
            if p is None:
                return cnt
            remove_stone(p)
            cnt += 1
        return cnt

    def removeStones(self, stones: List[List[int]]) -> int:
        """05/29/2020 00:55"""
        xs = defaultdict(set)
        ys = defaultdict(set)
        for i, (x, y) in enumerate(stones):
            xs[x].add(y)
            ys[y].add(x)

        cnt = 0
        while xs:
            cnt += 1
            x, y = xs.popitem()
            xstack = set([x])
            ystack = set(y)
            while xstack or ystack:
                while xstack:
                    x = xstack.pop()
                    if x not in xs:
                        continue
                    ystack.update(xs.get(x, set()))
                    xs.pop(x)
                while ystack:
                    y = ystack.pop()
                    if y not in ys:
                        continue
                    xstack.update(ys.get(y, set()))
                    ys.pop(y)
        return len(stones) - cnt

    def removeStones(self, stones: List[List[int]]) -> int:
        """11/20/2022 14:57"""
        rowcol = [defaultdict(set), defaultdict(set)]
        for i, j in stones:
            rowcol[0][i].add(j)
            rowcol[1][j].add(i)

        heap = []
        for i, j in stones:
            degree = len(rowcol[0][i])-1 + len(rowcol[1][j])-1
            heappush(heap, (-degree, (i, j)))
        remains = set()
        removed_rowcol = [set(), set()]
        while heap:
            _, (i, j) = heappop(heap)
            if i not in removed_rowcol[0] and j not in removed_rowcol[1]:
                remains.add((i, j))
            queue = deque([(0, i), (1, j)])
            while queue:
                rc, v = queue.popleft()
                removed_rowcol[rc].add(v)
                for j in rowcol[rc][v]:
                    if j not in removed_rowcol[(rc+1)%2]:
                        queue.append(((rc+1)%2, j))

        return len(stones) - len(remains)

    def removeStones(self, stones: List[List[int]]) -> int:
        """11/20/2022 15:04"""
        rowcol = [defaultdict(set), defaultdict(set)]
        for i, j in stones:
            rowcol[0][i].add(j)
            rowcol[1][j].add(i)

        cnt = 0
        removed_rowcol = [set(), set()]
        for i, j in stones:
            if i in removed_rowcol[0] or j in removed_rowcol[1]:
                continue
            cnt += 1
            queue = deque([(0, i), (1, j)])
            while queue:
                rc, v = queue.popleft()
                removed_rowcol[rc].add(v)
                for j in rowcol[rc][v]:
                    if j not in removed_rowcol[(rc+1)%2]:
                        queue.append(((rc+1)%2, j))

        return len(stones) - cnt


def to_grid(stones):
    r = max([x[0] for x in stones])+1
    c = max([x[1] for x in stones])+1
    mat = [[0] * c for _ in range(r)]
    for i, j in stones:
        mat[i][j] = 1
    return mat


@pytest.mark.parametrize('stones, expected', [
    ([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]], 5),
    ([[0,0],[0,2],[1,1],[2,0],[2,2]], 3),
    ([[0,0]], 0),
    ([[0,1],[1,0],[1,1]], 2),
    ([[0,0],[0,1],[1,0],[1,1],[2,1],[2,2],[3,2],[3,3],[3,4],[4,3],[4,4]], 10),
    ([[5,9],[9,0],[0,0],[7,0],[4,3],[8,5],[5,8],[1,1],[0,6],[7,5],[1,6],[1,9],[9,4],[2,8],[1,3],[4,2],[2,5],[4,1],[0,2],[6,5]], 19),
])
def test(stones, expected):
    print()
    grid = to_grid(stones)
    for row in grid:
        print(row)
    assert expected == Solution().removeStones(stones)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
