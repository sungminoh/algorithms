#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

Example 1:

Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3  (3 + 5  (3 + 6  (3 + 6 <= 9)

Example 2:

Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]

Example 3:

Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).

Constraints:

	1 <= nums.length <= 105
	1 <= nums[i] <= 106
	1 <= target <= 106
"""
import bisect
from typing import List
import pytest
import sys


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """Sep 09, 2023 22:02"""
        MOD = int(1e9+7)
        nums.sort()

        ret = 0
        for i, n in enumerate(nums):
            if 2*n > target:
                break
            j = bisect.bisect_left(nums, target-n+1, lo=i, hi=len(nums))
            ret += pow(2, max(0, j-i-1))
            ret %= MOD

        return ret

    def numSubseq(self, nums: List[int], target: int) -> int:
        """Sep 09, 2023 22:06"""
        MOD = int(1e9+7)
        nums.sort()

        i, j = 0, len(nums)-1
        ret = 0
        while i <= j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            else:
                ret += pow(2, j-i, MOD)
                i += 1
        return ret%MOD


@pytest.mark.parametrize('args', [
    (([3,5,6,7], 9, 4)),
    (([3,3,6,8], 10, 6)),
    (([2,3,3,4,6,7], 12, 61)),
    (([14,4,6,6,20,8,5,6,8,12,6,10,14,9,17,16,9,7,14,11,14,15,13,11,10,18,13,17,17,14,17,7,9,5,10,13,8,5,18,20,7,5,5,15,19,14], 22, 272187084)),
])
def test(args):
    assert args[-1] == Solution().numSubseq(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
