#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i = -1
        agg = 0
        ret = 0
        for j, n in enumerate(nums):
            agg += n
            while agg >= s:
                ret = min(ret, j - i) if ret else j - i
                i += 1
                agg -= nums[i]
        return ret


def main():
    inputs = [
        (7, [2, 3, 1, 2, 4, 3])
    ]
    exptecteds = [
        2
    ]
    for (s, nums), expected in zip(inputs, exptecteds):
        actual = Solution().minSubArrayLen(s, nums)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')


if __name__ == '__main__':
    main()
