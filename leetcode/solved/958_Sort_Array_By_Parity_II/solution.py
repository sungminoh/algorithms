#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

Example 1:

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Example 2:

Input: nums = [2,3]
Output: [2,3]

Constraints:

	2 <= nums.length <= 2 * 104
	nums.length is even.
	Half of the integers in nums are even.
	0 <= nums[i] <= 1000

Follow Up: Could you solve it in-place?
"""
import sys
from typing import List
import pytest


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """
        Inplace
        Time complexity: O(n)
        Space complexity: O(1)
        """
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if nums[i]%2 == 0:
                i += 2
                continue
            elif nums[j]%2 != 0:
                j += 2
                continue
            else:
                nums[i], nums[j] = nums[j], nums[i]
        return nums


@pytest.mark.parametrize('nums, expected', [
    ([4,2,5,7], [4,5,2,7]),
    ([2,3], [2,3]),
])
def test(nums, expected):
    assert expected == Solution().sortArrayByParityII(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
