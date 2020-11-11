#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
"""
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ''
        if all(n == 0 for n in nums):
            return '0'

        from math import log10
        import re
        def helper(x):
            search = re.search(r'[^%s]' % str(x)[0], str(x))
            if search:
                return len(str(x)) if int(search.group()) < int(str(x)[0]) else -len(str(x));
            else:
                return 0
        ml = max(int(log10(n))+1 for n in nums if n > 0)
        # Sort after pad first digit.
        # When two numbers are same,
        #   if the first number which is diffent from first digit is lager than first digit,
        #     longer shoud be ahead.
        #   else
        #     shorter should be ahead.
        nums.sort(key=lambda x: (('{:%s<%s}' % (int(str(x)[0]), ml)).format(x),
                                 helper(x)))
        return ''.join(str(n) for n in reversed(nums))


def main():
    nums = [int(x) for x in input().split()]
    # nums = [824,938,1399,5607,6973,5703,9609,4398,8247]
    print(Solution().largestNumber(nums))


if __name__ == '__main__':
    main()
