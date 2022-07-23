#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

	horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
	verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.

Example 1:

Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.

Example 2:

Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.

Example 3:

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9

Constraints:

	2 <= h, w <= 109
	1 <= horizontalCuts.length <= min(h - 1, 105)
	1 <= verticalCuts.length <= min(w - 1, 105)
	1 <= horizontalCuts[i] < h
	1 <= verticalCuts[i] < w
	All the elements in horizontalCuts are distinct.
	All the elements in verticalCuts are distinct.
"""
import sys
from typing import List
import pytest


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        """06/22/2021 06:07"""
        MOD = 1e9+7
        hs = sorted(horizontalCuts + [h]) + [0]
        ws = sorted(verticalCuts + [w]) + [0]

        height = max(hs[i] - hs[i-1] for i in range(len(hs)-1)) % MOD
        width = max(ws[j] - ws[j-1] for j in range(len(ws)-1)) % MOD
        if height > MOD/2:
            height -= MOD
        if width > MOD/2:
            width -= MOD
        return int((height*width) % MOD)

    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()
        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()
        MOD = int(1e9)+7
        height = max(horizontalCuts[i+1]-horizontalCuts[i] for i in range(len(horizontalCuts)-1)) % MOD
        width = max(verticalCuts[i+1]-verticalCuts[i] for i in range(len(verticalCuts)-1)) % MOD
        return (height * width) % MOD


@pytest.mark.parametrize('h, w, horizontalCuts, verticalCuts, expected', [
    (5, 4, [1,2,4], [1,3], 4),
    (5, 4, [3,1], [1], 6),
    (5, 4, [3], [3], 9),
    (1000000000, 1000000000, [2], [2], 81),
])
def test(h, w, horizontalCuts, verticalCuts, expected):
    assert expected == Solution().maxArea(h, w, horizontalCuts, verticalCuts)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
