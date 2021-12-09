#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:

	1 <= nums.length <= 2 * 104
	-10 <= nums[i] <= 10
	The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
import sys
from typing import List
import pytest


class Solution:
    def maxProduct(self, nums):
        """07/27/2018 22:42"""
        if not nums:
            return 0
        m = -float('inf')
        # Set starting point
        i = 0;
        while i < len(nums) and nums[i] == 0:
            i += 1
        # Was there zero?
        if i > 0:
            m = 0
        # Get max product of each chunk
        while i < len(nums):
            p = 1
            # If there is zero in the middle of the list
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    for k in range(i, j-1):
                        p //= nums[k]
                        m = max(m, p)
                    m = max(m, 0)
                    i = j+1
                    break
                p *= nums[j]
                m = max(m, p)
            # else there is no zero in the list
            else:
                for k in range(i, len(nums)-1):
                    p //= nums[k]
                    m = max(m, p)
                break
        return m

    def maxProduct(self, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not nums:
            return 0
        ret = nums[0]
        acc = 1
        neg = 1
        neg_cnt = 0
        for n in nums:
            # reset
            if n == 0:
                acc = 1
                neg = 1
                neg_cnt = 0
                ret = max(ret, 0)
            else:
                acc *= abs(n)
                if n < 0:
                    if neg_cnt == 0:
                        neg = acc
                    neg_cnt += 1
                if neg_cnt%2 == 0:
                    # when there were even number of negative values so far,
                    #  multipying all numbers is the max product
                    ret = max(ret, acc)
                elif not (n < 0 and neg_cnt == 1):
                    # when there were odd number of negative values so far,
                    #  and also when the current n is not the first negative
                    #  multiplying all numbers after the first negative value
                    #  and the currnet number is the max product
                    ret = max(ret, acc//neg)
        return ret



@pytest.mark.parametrize('nums, expected', [
    ([2,3,-2,4], 6),
    ([-2,0,-1], 0),
    ([-2], -2)
])
def test(nums, expected):
    assert expected == Solution().maxProduct(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
