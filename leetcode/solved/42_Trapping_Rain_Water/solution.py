#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

"""

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
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


def main():
    height = [int(x) for x in input().split()]
    print(Solution().trap(height))


if __name__ == '__main__':
    main()
