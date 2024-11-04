#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.

Example 1:

Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]

Example 2:

Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

Constraints:

	1 <= rows, cols <= 100
	0 <= rStart < rows
	0 <= cStart < cols
"""
from collections import deque
from typing import List
import pytest
import sys


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        """Nov 03, 2024 19:41"""
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # (r, c, direction, length, steps)
        queue = deque([(rStart, cStart, 0, 1, 0)])
        ret = []
        while len(ret) < rows*cols:
            r, c, d, l, s = queue.popleft()
            if 0<=r<rows and 0<=c<cols:
                ret.append([r, c])
            dr, dc = direction[d]
            r += dr
            c += dc
            s += 1
            if s == l:
                d = (d+1)%4
                if d%2 == 0:  # when start to move between columns, length of the side increases
                    l += 1
                s = 0
            queue.append((r, c, d, l, s))

        return ret


@pytest.mark.parametrize('args', [
    ((1, 4, 0, 0, [[0,0],[0,1],[0,2],[0,3]])),
    ((5, 6, 1, 4, [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]])),
])
def test(args):
    assert args[-1] == Solution().spiralMatrixIII(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
