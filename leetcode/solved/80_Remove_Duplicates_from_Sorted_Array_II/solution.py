#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:

	1 <= nums.length <= 3 * 104
	-104 <= nums[i] <= 104
	nums is sorted in non-decreasing order.
"""
import sys
from typing import List
import pytest


class Solution:
    def removeDuplicates(self, nums):
        """05/01/2018 05:33"""
        from collections import defaultdict
        counter = defaultdict(int)
        ret = len(nums)-1
        i = 0
        while i <= ret:
            counter[nums[i]] += 1
            if counter[nums[i]] > 2:
                while ret > i and nums[ret] == nums[i]:
                    ret -= 1
                nums[i], nums[ret] = nums[ret], nums[i]
                ret -= 1
                continue
            i += 1
        nums[:ret+1] = sorted(nums[:ret+1])
        return ret+1

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j, n in enumerate(nums):
            if 0<j<len(nums)-1 and nums[i-1] == n == nums[j+1]:
                continue
            nums[i] = nums[j]
            i += 1
        return i


@pytest.mark.parametrize('nums, k, expected', [
    ([1,1,1,2,2,3], 5, [1,1,2,2,3,None]),
    ([0,0,1,1,1,1,2,3,3], 7, [0,0,1,1,2,3,3,None,None]),
])
def test(nums, k, expected):
    assert k == Solution().removeDuplicates(nums)
    for i in range(k):
        assert nums[i] == expected[i]


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))

