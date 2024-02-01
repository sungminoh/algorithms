import math
from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).

Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.

Example 1:

Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Example 2:

Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138

Constraints:

	m == img.length
	n == img[i].length
	1 <= m, n <= 200
	0 <= img[i][j] <= 255
"""
import pytest
import sys


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        """Jan 31, 2024 22:12"""
        M = len(img)
        N = len(img[0])

        integral = [[0]*(N+1)]
        for i in range(M):
            row = [0]
            acc = 0
            for j in range(N):
                acc += img[i][j]
                row.append(acc + integral[-1][j+1])
            integral.append(row)

        def get_avg(i, j):
            brx = min(M-1, i+1)
            bry = min(N-1, j+1)
            tlx = max(-1, i-2)
            tly = max(-1, j-2)
            s = integral[brx+1][bry+1] - integral[brx+1][tly+1] - integral[tlx+1][bry+1] + integral[tlx+1][tly+1]
            cnt = (brx-tlx) * (bry-tly)
            return math.floor(s/cnt)

        ret = []
        for i in range(M):
            row = []
            for j in range(N):
                row.append(get_avg(i, j))
            ret.append(row)
        return ret


@pytest.mark.parametrize('args', [
    (([[1,1,1],[1,0,1],[1,1,1]], [[0,0,0],[0,0,0],[0,0,0]])),
    (([[100,200,100],[200,50,200],[100,200,100]], [[137,141,137],[141,138,141],[137,141,137]])),
])
def test(args):
    assert args[-1] == Solution().imageSmoother(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
