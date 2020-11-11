#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].




The largest rectangle is shown in the shaded area, which has area = 10 unit.



Example:

Input: [2,1,5,6,2,3]
Output: 10
"""

class Solution:
    def largestRectangleArea(self, heights):
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

    def __largestRectangleArea(self, heights):
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

    def _largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        self.heights = heights
        return self.get_largest_area_bewteen(0, len(heights)-1)

    def get_largest_area_bewteen(self, s, e):
        if s > e:
            return 0
        elif s == e:
            return self.heights[s]
        m = (s+e)//2
        i, j = m, m+1
        h = min(self.heights[i], self.heights[j])
        center = h * 2
        while s < i and j < e:
            if self.heights[i-1] > self.heights[j+1]:
                i -= 1
            else:
                j += 1
            h = min(h, self.heights[i], self.heights[j])
            center = max(center, h * (j-i+1))
        while s < i:
            i -= 1
            h = min(h, self.heights[i])
            center = max(center, h * (j-i+1))
        while j < e:
            j += 1
            h = min(h, self.heights[j])
            center = max(center, h * (j-i+1))
        print(s, e, center)
        return max(self.get_largest_area_bewteen(s, m), self.get_largest_area_bewteen(m+1, e), center)


def main():
    heights = [int(x) for x in input().split()]
    print(Solution().largestRectangleArea(heights))


if __name__ == '__main__':
    main()
