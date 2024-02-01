from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.

Example 1:
​

Input: points = [[8,7],[9,9],[7,4],[9,7]]
Output: 1
Explanation: Both the red and the blue area are optimal.

Example 2:

Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
Output: 3

Constraints:

	n == points.length
	2 <= n <= 105
	points[i].length == 2
	0 <= xi, yi <= 109
"""
import pytest
import sys


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        """Jan 31, 2024 22:30"""
        points.sort()
        return max(points[i+1][0]-points[i][0] for i in range(len(points)-1))


@pytest.mark.parametrize('args', [
    (([[8,7],[9,9],[7,4],[9,7]], 1)),
    (([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]], 3)),
    (([[1,1],[1,2],[1,3]], 0)),
])
def test(args):
    assert args[-1] == Solution().maxWidthOfVerticalArea(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
