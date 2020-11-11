#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        self.nums = nums
        self.memo = {}
        rob_first = nums[0] + self.max_striding(2, len(nums) - 1)
        leave_first = self.max_striding(1, len(nums))
        return max(rob_first, leave_first)

    def max_striding(self, i, j):
        if i >= j:
            return 0
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        rob_first = self.nums[i] + self.max_striding(i + 2, j)
        leave_first = self.max_striding(i + 1, j)
        ret = max(rob_first, leave_first)
        self.memo[(i, j)] = ret
        return ret


if __name__ == '__main__':
    cases = [
        [2,3,2],
        [1,2,3,1],
        [],
        [1]
    ]
    expecteds = [
        3,
        4,
        0,
        1
    ]
    for nums, expected in zip(cases, expecteds):
        actual = Solution().rob(nums)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
