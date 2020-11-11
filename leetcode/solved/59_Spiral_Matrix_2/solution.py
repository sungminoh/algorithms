#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a positive integer n, generate a square matrix filled with elements
from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class Solution:
    def i2v(self, i, j, n):
        dist_to_side = [j, n-1-i, n-1-j, i]
        layer = min(dist_to_side)
        for s, d in enumerate(dist_to_side):
            if d == layer:
                side = s
                break
        outer = 4 * layer * (n - layer)
        pre = side * (n - 1 - (2 * layer))
        remain = [i, j, n-1-i, n-1-j][side] - layer + 1
        return outer + pre + remain

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        return [[self.i2v(i, j, n) for i in range(n)] for j in range(n)]


def main():
    for l in Solution().generateMatrix(int(input())):
        print(l)


if __name__ == '__main__':
    main()
