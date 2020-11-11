#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        memo = [[-1]*len(grid[0]) for _ in range(len(grid))]
        memo[0][0] = grid[0][0]
        for j in range(1, len(grid[0])):
            memo[0][j] = memo[0][j-1] + grid[0][j]
        for i in range(1, len(grid)):
            memo[i][0] = memo[i-1][0] + grid[i][0]

        def short_to(i, j):
            if memo[i][j] >= 0:
                return memo[i][j]
            memo[i][j] = min(short_to(i-1, j), short_to(i, j-1)) + grid[i][j]
            return memo[i][j]
        return short_to(len(grid)-1, len(grid[0])-1)


def main():
    grid = [[1,3,1],
            [1,5,1],
            [4,2,1]]
    print(Solution().minPathSum(grid))


if __name__ == '__main__':
    main()
