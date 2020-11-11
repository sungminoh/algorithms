#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        def travel(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])\
                    or visited[i][j] or grid[i][j] != '1':
                return False
            visited[i][j] = True
            travel(i - 1, j)
            travel(i + 1, j)
            travel(i, j - 1)
            travel(i, j + 1)
            return True

        ret = 0
        visited = [[None] * len(grid[0]) for _ in grid]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if travel(i, j):
                    ret += 1
        return ret


def main():
    inputs = []
    inputs.append(("11110 11010 11000 00000".split(), 1))
    inputs.append(("11000 11000 00100 00011".split(), 3))
    for grid, expected in inputs:
        actual = Solution().numIslands(grid)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')




if __name__ == '__main__':
    main()
