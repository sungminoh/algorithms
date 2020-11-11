#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""


class Solution(object):
    def ternary_positionwise_add(self, a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        a1, a2 = divmod(a, 3)
        b1, b2 = divmod(b, 3)
        c = (a2 + b2) % 3
        return c + 3 * self.ternary_positionwise_add(a1, b1)

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sign = 0
        ret = 0
        for n in nums:
            if n < 0:
                sign += 1
                sign %= 3
                n *= -1
            ret = self.ternary_positionwise_add(ret, n)
        return ret * (-1 if sign != 0 else 1)


def main():
    print(Solution().singleNumber([int(x) for x in input().split()]))


if __name__ == '__main__':
    main()
