#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

Constraints:

	1 <= nums.length <= 105
	1 <= nums[i] <= 104
	1 <= x <= 109
"""
import itertools
from pathlib import Path
import json
import sys
from typing import List
import pytest


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        visited = set()
        ret = len(nums)+1
        def dfs(i, j, t, cnt):
            if t == 0:
                nonlocal ret
                ret = min(ret, cnt)
            if (i, j) in visited or t < 0 or i > j:
                return
            dfs(i+1, j, t-nums[i], cnt+1)
            dfs(i, j-1, t-nums[j], cnt+1)

        dfs(0, len(nums)-1, x, 0)
        return -1 if ret > len(nums) else ret

    def minOperations(self, nums: List[int], x: int) -> int:
        acc = [0] + list(itertools.accumulate(nums))
        total = acc[-1]
        if x > total:
            return -1
        if x == total:
            return len(nums)
        index = {v: i for i, v in enumerate(acc)}
        ret = len(nums)+1
        for i, a in enumerate(acc):
            b = x-a
            if total-b in index:
                operations_from_left = i
                operations_from_right = len(acc)-1 - index[total-b]
                ret = min(ret, operations_from_left + operations_from_right)
        return ret if ret <= len(nums) else -1


@pytest.mark.parametrize('nums, x, expected', [
    ([1,1,4,2,3], 5, 2),
    ([5,6,7,8,9], 4, -1),
    ([3,2,20,1,1,3], 10, 5),
    ([8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], 134365, 16),
    (*json.load(open(Path(__file__).parent/'testcase.json')), -1),
])
def test(nums, x, expected):
    assert expected == Solution().minOperations(nums, x)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
