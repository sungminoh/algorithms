#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

	n == height.length
	1 <= n <= 2 * 104
	0 <= height[i] <= 105
"""
import sys
from typing import List
import pytest


class Solution:
    def trap(self, height):
        """08/06/2018 02:27"""
        if not height:
            return 0
        max_right = [height[-1]]
        rheight = reversed(height)
        next(rheight)
        for i, h in enumerate(rheight):
            max_right.append(max(max_right[i], h))
        max_right.reverse()

        max_left = [height[0]]
        for i, h in enumerate(height[1:]):
            max_left.append(max(max_left[i], h))

        s = 0
        for h, l, r in zip(height, max_left, max_right):
            s += min(l, r) - h
        return s

    def trap(self, height: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        height = [0] + height + [0]
        n = len(height)
        left_highest = [0]
        for i in range(1, len(height)):
            left_highest.append(max(left_highest[i-1], height[i-1]))
        right_highest = [0]
        for i in range(1, len(height)):
            right_highest.append(max(right_highest[i-1], height[len(height)-1-i]))
        right_highest.reverse()
        ret = 0
        for h, lh, rh in zip(height, left_highest, right_highest):
            ret += max(0, min(lh, rh) - h)
        return ret

    def trap(self, height: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not height:
            return 0
        ret = 0
        # from left
        highest_idx = 0
        highest = height[highest_idx]
        water = 0
        for i in range(1, len(height)):
            h = height[i]
            if h < highest:
                water += highest - h
            else:
                highest = h
                highest_idx = i
                ret += water
                water = 0
        # from right
        highest_idx_from_left = highest_idx
        highest_idx = len(height)-1
        highest = height[highest_idx]
        water = 0
        for i in range(len(height)-2, highest_idx_from_left-1, -1):
            h = height[i]
            if h < highest:
                water += highest - h
            else:
                highest = h
                highest_idx = i
                ret += water
                water = 0
        return ret


@pytest.mark.parametrize('height, expected', [
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ([4,2,0,3,2,5], 9),
])
def test(height, expected):
    assert expected == Solution().trap(height)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
