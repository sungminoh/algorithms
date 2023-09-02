import math
from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a 0-indexed array nums comprising of n non-negative integers.

In one operation, you must:

	Choose an integer i such that 1 <= i < n and nums[i] > 0.
	Decrease nums[i] by 1.
	Increase nums[i - 1] by 1.

Return the minimum possible value of the maximum integer of nums after performing any number of operations.

Example 1:

Input: nums = [3,7,1,6]
Output: 5
Explanation:
One set of optimal operations is as follows:
1. Choose i = 1, and nums becomes [4,6,1,6].
2. Choose i = 3, and nums becomes [4,6,2,5].
3. Choose i = 1, and nums becomes [5,5,2,5].
The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
Therefore, we return 5.

Example 2:

Input: nums = [10,1]
Output: 10
Explanation:
It is optimal to leave nums as is, and since 10 is the maximum value, we return 10.

Constraints:

	n == nums.length
	2 <= n <= 105
	0 <= nums[i] <= 109
"""
import pytest
import sys


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        """Aug 26, 2023 14:30"""
        def flatten(stack):
            acr = stack.pop()
            while stack and stack[-1][0] <= acr[0]:
                _acr = stack.pop()
                cnt = (_acr[0]*_acr[1]) + _acr[2] + (acr[0]*acr[1])+acr[2]
                a, r = divmod(cnt, acr[1]+_acr[1])
                acr = [a, acr[1]+_acr[1], r]
            stack.append(acr)


        ret = 0
        stack = [[nums[0], 1, 0]]  # avg, cnt, remain
        for i in range(1, len(nums)):
            acr = stack[-1]
            if nums[i] >= acr[0]:
                over = nums[i]-acr[0]+acr[2]
                acr[1] += 1
                n, r = divmod(over, acr[1])
                acr[0] += n
                acr[2] = r
                flatten(stack)
            else:
                stack.append([nums[i], 1, 0])
            print(i, stack)

        return max([acr[0] + min(1, acr[2]) for acr in stack])

    def minimizeArrayValue(self, nums: List[int]) -> int:
        """Aug 26, 2023 14:33"""
        ret = 0
        acc = 0
        for i, n in enumerate(nums, 1):
            acc += n
            ret = max(ret, math.ceil(acc/i))
        return ret


@pytest.mark.parametrize('args', [
    (([3,7,1,6], 5)),
    (([10,1], 10)),
    (([13,13,20,0,8,9,9], 16)),
])
def test(args):
    assert args[-1] == Solution().minimizeArrayValue(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
