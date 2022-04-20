#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

Constraints:

	n == height.length
	2 <= n <= 105
	0 <= height[i] <= 104
"""
import sys
from typing import List
import pytest


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """TLE"""
        stack = [0]
        ret = 0
        for i, h in enumerate(height[1:], 1):
            for j in stack:
                ret = max(ret, (i-j)*min(h, height[j]))
            if h > height[stack[-1]]:
                stack.append(i)
        return ret

    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        ret = 0
        while l < r:
            h = min(height[l], height[r])
            w = r-l
            ret = max(ret, w*h)
            while l < r and height[l] <= h:
                l += 1
            while l < r and height[r] <= h:
                r -= 1
        return ret


@pytest.mark.parametrize('height, expected', [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1,1], 1),
    ([1,0,0,0,0,0,0,2,2], 8),
])
def test(height, expected):
    assert expected == Solution().maxArea(height)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
