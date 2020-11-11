#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        memo = triangle.pop()
        while triangle:
            last = triangle.pop()
            for i, n in enumerate(last):
                memo[i] = n + min(memo[i], memo[i+1])
        return memo[0]



def main():
    triangle = []
    row = [int(x) for x in input().split()]
    while row:
        triangle.append(row)
        row = [int(x) for x in input().split()]
    print(Solution().minimumTotal(triangle))


if __name__ == '__main__':
    main()
