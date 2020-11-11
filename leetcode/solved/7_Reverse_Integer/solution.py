#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output:  321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed
integer range. For the purpose of this problem, assume that your function returns 0 when the
reversed integer overflows.
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        neg = 1
        if x < 0:
            neg = -1
            x *= -1
        lst = list(str(x))
        lst.reverse()
        x = int(''.join(lst))
        if x > 2147483648:
            return 0
        return neg * x


def main():
    print(Solution().reverse(int(input())))


if __name__ == '__main__':
    main()
