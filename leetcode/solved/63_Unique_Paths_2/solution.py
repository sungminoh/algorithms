#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
63. Unique Paths II
DescriptionHintsSubmissionsDiscussSolution
DiscussPick One
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        l = [1]*len(obstacleGrid[0])
        try:
            obstacle_idx = obstacleGrid[0].index(1, 0)
            l[obstacle_idx:] = [0]*(len(obstacleGrid[0]) - obstacle_idx)
        except Exception:
            pass
        for i, row in enumerate(obstacleGrid[1:]):
            if row[0] == 1:
                l[0] = 0
            for i in range(1, m):
                l[i] = (l[i-1] + l[i]) if row[i] == 0 else 0
        return l[-1]


def main():
    grid = []
    row = list(map(int, list(input())))
    while row:
        grid.append(row)
        row = list(map(int, list(input())))
    print(Solution().uniquePathsWithObstacles(grid))


if __name__ == '__main__':
    main()
