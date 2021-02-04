#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:

	0 <= nums.length <= 100
	0 <= nums[i] <= 400
"""
import sys
from typing import List
import pytest


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        yes = nums[0]
        no = 0
        for n in nums[1:]:
            _yes = no + n
            no = max(yes, no)
            yes = _yes
        return max(yes, no)


@pytest.mark.parametrize('nums, expected', [
    ([1,2,3,1], 4),
    ([2,7,9,3,1], 12),
])
def test(nums, expected):
    assert expected == Solution().rob(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
