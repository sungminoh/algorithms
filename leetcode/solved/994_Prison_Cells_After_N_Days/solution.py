
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

	If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
	Otherwise, it becomes vacant.

(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation:
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]

Note:
    1. cells.length == 8
    2. cells[i] is in {0, 1}
    3. 1 <= N <= 10^9
"""
import sys
from typing import List
import pytest


def next_state(cells):
    ret = [0]
    for i in range(1, len(cells) - 1):
        if cells[i - 1] + cells[i + 1] in {0, 2}:
            ret.append(1)
        else:
            ret.append(0)
    ret.append(0)
    return tuple(ret)


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        cells = tuple(cells)
        memo = [cells]
        visited = {cells: 0}
        for i in range(N):
            cells = next_state(cells)
            if cells in visited:
                break
            visited[cells] = len(memo)
            memo.append(cells)
        else:
            return list(memo[-1])
        s = visited[cells]
        return list(memo[int((N - s) % (len(memo) - s)) + s])


@pytest.mark.parametrize('cells, N, expected', [
    ([0,1,0,1,1,0,0,1], 7, [0,0,1,1,0,0,0,0]),
    ([1,0,0,1,0,0,1,0], 1000000000, [0,0,1,1,1,1,1,0]),
    ([0,0,1,1,1,1,0,0], 8, [0,0,0,1,1,0,0,0])
])
def test(cells, N, expected):
    assert expected == Solution().prisonAfterNDays(cells, N)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
