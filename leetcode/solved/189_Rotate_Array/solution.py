#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:

	1 <= nums.length <= 105
	-231 <= nums[i] <= 231 - 1
	0 <= k <= 105

Follow up:

	Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
	Could you do it in-place with O(1) extra space?
"""
import random
import sys
from typing import List
import pytest


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """03/31/2020 18:47"""
        if not nums or k == len(nums):
            return nums

        def swap_circle(nums, i, k):
            m = 0
            tmp = None
            while nums[i] is not None:
                if m == 0 or i < m:
                    m = i
                tmp, nums[i] = nums[i], tmp
                i = (i + k) % len(nums)
            else:
                nums[i] = tmp
            return m

        k = k % len(nums)
        times = swap_circle(nums, 0, k)
        for i in range(1, times):
            swap_circle(nums, i, k)


    def rotate(self, nums: List[int], k: int) -> None:
        if not nums:
            return

        k = k%len(nums)
        def rot(i, k):
            j = i
            tmp = nums[j]
            new_j = (j+k) % len(nums)
            ret = k
            while new_j != i:
                nums[new_j], tmp = tmp, nums[new_j]
                j = new_j
                new_j = (j+k) % len(nums)
                if new_j > i:
                    ret = min(ret, new_j-i)
            else:
                nums[i] = tmp
            return ret

        d = rot(0, k)
        for i in range(1, d):
            rot(i, k)


def gen_case():
    size = random.randint(0, 20)
    nums = list(range(size))
    random.shuffle(nums)
    k = random.randint(0, 20)
    fivot = k % len(nums)
    answer = nums[-fivot:] + nums[:-fivot]
    return nums, k, answer


@pytest.mark.parametrize('nums, k, expected', [
    ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
    ([-1,-100,3,99], 2, [3,99,-1,-100]),
    (gen_case()),
    (gen_case()),
    (gen_case()),
    (gen_case()),
])
def test(nums, k, expected):
    Solution().rotate(nums, k)
    assert expected == nums


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
