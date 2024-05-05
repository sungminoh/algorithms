#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is a 1 million by 1 million grid on an XY-plane, and the coordinates of each grid square are (x, y).

We start at the source = [sx, sy] square and want to reach the target = [tx, ty] square. There is also an array of blocked squares, where each blocked[i] = [xi, yi] represents a blocked square with coordinates (xi, yi).

Each move, we can walk one square north, east, south, or west if the square is not in the array of blocked squares. We are also not allowed to walk outside of the grid.

Return true if and only if it is possible to reach the target square from the source square through a sequence of valid moves.

Example 1:

Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
Output: false
Explanation: The target square is inaccessible starting from the source square because we cannot move.
We cannot move north or east because those squares are blocked.
We cannot move south or west because we cannot go outside of the grid.

Example 2:

Input: blocked = [], source = [0,0], target = [999999,999999]
Output: true
Explanation: Because there are no blocked cells, it is possible to reach the target square.

Constraints:

	0 <= blocked.length <= 200
	blocked[i].length == 2
	0 <= xi, yi < 106
	source.length == target.length == 2
	0 <= sx, sy, tx, ty < 106
	source != target
	It is guaranteed that source and target are not blocked.
"""
from collections import deque
from typing import List
import pytest
import sys


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        """May 04, 2024 12:59"""
        M = N = int(1e6)

        blocked = set(tuple(x) for x in blocked)

        def neighbors(i, j):
            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                x, y = i+dx, j+dy
                if 0<=x<M and 0<=y<N and (x, y) not in blocked:
                    yield x, y

        MAX_AREA = 199*200/2

        def bfs(i, j, target):
            ret = 1
            queue = deque([(i, j)])
            seen = set(queue)
            while queue:
                size = len(queue)
                for _ in range(size):
                    i, j = queue.popleft()
                    if (i, j) == tuple(target):
                        return -1
                    for x, y in neighbors(i, j):
                        if (x, y) not in seen:
                            seen.add((x, y))
                            queue.append((x, y))
                            ret += 1
                        if ret > MAX_AREA:
                            return -1
            return ret

        return bfs(*source, target) == -1 and bfs(*target, source) == -1


@pytest.mark.parametrize('args', [
    (([[0,1],[1,0]], [0,0], [0,2], False)),
    (([], [0,0], [999999,999999], True)),
    (([[10,9],[9,10],[10,11],[11,10]], [0,0], [10,10], False)),
    (([[0,3],[1,0],[1,1],[1,2],[1,3]], [0,0], [0,2], True)),
])
def test(args):
    assert args[-1] == Solution().isEscapePossible(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
