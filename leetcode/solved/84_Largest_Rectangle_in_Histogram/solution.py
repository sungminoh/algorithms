#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:

Input: heights = [2,4]
Output: 4

Constraints:

	1 <= heights.length <= 105
	0 <= heights[i] <= 104
"""
import sys
from typing import List
import pytest


class Solution:
    def largestRectangleArea(self, heights):
        """08/13/2018 05:57"""
        def get_largest_area_bewteen(s, e):
            if s > e:
                return 0
            elif s == e:
                return heights[s]
            m = (s+e)//2
            i, j = m, m+1
            h = min(heights[i], heights[j])
            center = h * 2
            while s < i and j < e:
                if heights[i-1] > heights[j+1]:
                    i -= 1
                else:
                    j += 1
                h = min(h, heights[i], heights[j])
                center = max(center, h * (j-i+1))
            while s < i:
                i -= 1
                h = min(h, heights[i])
                center = max(center, h * (j-i+1))
            while j < e:
                j += 1
                h = min(h, heights[j])
                center = max(center, h * (j-i+1))
            return max(get_largest_area_bewteen(s, m), get_largest_area_bewteen(m+1, e), center)

        return get_largest_area_bewteen(0, len(heights)-1)

    def largestRectangleArea(self, heights):
        """08/14/2018 19:41"""
        ret = 0
        stack = []
        for i, h in enumerate(heights):
            idx = ph = -1
            while stack and stack[-1][1] >= h:
                idx, ph = stack.pop()
                ret = max(ret, ph * (i - idx))
            if idx < 0:
                idx = i
            stack.append((idx, h))
        while stack:
            idx, ph = stack.pop()
            ret = max(ret, ph * (len(heights) - idx))
        return ret

    def largestRectangleArea(self, heights):
        """08/14/2018 23:00"""
        ret = 0
        stack = []
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                ph = heights[stack.pop()]
                w = i - (stack[-1] if stack else -1) - 1
                ret = max(ret, ph * w)
            stack.append(i)
        return ret

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(0)
        ret = 0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                j = stack.pop()
                ret = max(ret, (i-stack[-1]-1) * heights[j])
            stack.append(i)
        return ret


@pytest.mark.parametrize('heights, expected', [
    ([2,1,5,6,2,3], 10),
    ([2,4], 4),
    ([2,1,2], 3),
])
def test(heights, expected):
    assert expected == Solution().largestRectangleArea(heights)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
