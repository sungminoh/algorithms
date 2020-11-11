#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
69. Sqrt(x)(https://leetcode.com/problems/sqrtx/description/)
DescriptionHintsSubmissionsDiscussSolution
DiscussPick One
Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.


Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.
"""


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        l, h = 0, x
        r = (h+l)//2
        while h-l > 1:
            if r**2 == x:
                break
            if r**2 > x:
                h = r
            else:
                l = r
            r = (h+l)//2
        return r



def main():
    print(Solution().mySqrt(int(input())))


if __name__ == '__main__':
    main()
