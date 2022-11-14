#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

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

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:

	1 <= nums.length <= 3 * 104
	-100 <= nums[i] <= 100
	nums is sorted in non-decreasing order.
"""
import random
from typing import List
import pytest
import sys


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """03/31/2020 13:48"""
        if not nums:
            return 0
        prev = nums[0]
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] == prev:
                cnt += 1
            else:
                prev = nums[i]
                nums[i - cnt], nums[i] = nums[i], nums[i - cnt]
        return len(nums) - cnt

    def removeDuplicates(self, nums: List[int]) -> int:
        """11/13/2022 20:15"""
        i = j = 1
        n = nums[0]
        while i < len(nums):
            m = nums[i]
            if nums[i] != n:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            n = m
            i += 1
        return j


def gen_case():
    ret = []
    for i in range(random.randint(0, 10)):
        for _ in range(random.randint(1, 3)):
            ret.append(i)
    return ret, len(sorted(list(set(ret))))


@pytest.mark.parametrize('nums, k, expected', [
    ([1,1,2], 2, [1,2,None]),
    ([0,0,1,1,1,2,2,3,3,4], 5, [0,1,2,3,4,None,None,None,None,None]),
])
def test(nums, k, expected):
    actual = Solution().removeDuplicates(nums)
    assert k == actual
    assert expected[:k] == nums[:actual]


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
