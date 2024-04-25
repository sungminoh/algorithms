#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an m x n grid grid where:

	'.' is an empty cell.
	'#' is a wall.
	'@' is the starting point.
	Lowercase letters represent keys.
	Uppercase letters represent locks.

You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

Example 1:

Input: grid = ["@.a..","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open all the locks.

Example 2:

Input: grid = ["@..aA","..B#.","....b"]
Output: 6

Example 3:

Input: grid = ["@Aa"]
Output: -1

Constraints:

	m == grid.length
	n == grid[i].length
	1 <= m, n <= 30
	grid[i][j] is either an English letter, '.', '#', or '@'. 
	There is exactly one '@' in the grid.
	The number of keys in the grid is in the range [1, 6].
	Each key in the grid is unique.
	Each key in the grid has a matching lock.
"""
from collections import deque
from typing import List
import pytest
import sys


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        """Apr 18, 2024 23:12"""
        M, N = len(grid), len(grid[0])
        start = next(iter((i, j) for i in range(M) for j in range(N) if grid[i][j] == '@'))
        num_keys = len([(i, j) for i in range(M) for j in range(N) if 'a' <= grid[i][j] <= 'z'])
        ALL_KEYS = (1 << num_keys) - 1

        def iter_neighbor(i, j):
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = i+dx, j+dy
                if 0<=x<M and 0<=y<N:
                    yield x, y

        def has_key(keys, lock):
            return keys & (1 << (ord(lock.lower()) - ord('a')))

        def add_key(keys, lock):
            return keys | (1 << (ord(lock.lower()) - ord('a')))

        def deserialize_keys(keys):
            ret = []
            i = 0
            while keys:
                if keys % 2:
                    ret.append(chr(ord('a') + i))
                keys //= 2
                i += 1
            return ret

        ret = 0
        queue = deque([(*start, 0)])
        visited = set()
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j, keys = queue.popleft()
                if 'a' <= grid[i][j] <= 'z':
                    keys = add_key(keys, grid[i][j])
                if keys == ALL_KEYS:
                    return ret
                for x, y in iter_neighbor(i, j):
                    if (x, y, keys) in visited:
                        continue
                    visited.add((x, y, keys))
                    if (
                        grid[x][y] == '.'
                        or 'A' <= grid[x][y] <= 'Z' and has_key(keys, grid[x][y])
                        or 'a' <= grid[x][y] <= 'z'
                        or grid[x][y] == '@'
                    ):
                        queue.append((x, y, keys))
            ret += 1
        return -1


@pytest.mark.parametrize('args', [
    ((["@.a..","###.#","b.A.B"], 8)),
    ((["@..aA","..B#.","....b"], 6)),
    ((["@Aa"], -1)),
    ((["@...a",
       ".###A",
       "b.BCc"], 10)),
])
def test(args):
    assert args[-1] == Solution().shortestPathAllKeys(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
