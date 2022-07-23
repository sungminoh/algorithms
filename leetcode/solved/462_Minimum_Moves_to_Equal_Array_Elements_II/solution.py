#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

Example 2:

Input: nums = [1,10,2,9]
Output: 16

Constraints:

	n == nums.length
	1 <= nums.length <= 105
	-109 <= nums[i] <= 109
"""
import sys
from typing import List
import pytest


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        """06/01/2021 16:09
        Find median by quick select
        Time complexity: O(n) ~ O(n^2)
        Space complexity: O(1)
        """
        def quick_select(l, k):
            def rec(l, s, e, k):
                if s == e:
                    return l[s]
                # select pivot
                p = l[e]
                # partition, l[index] >= p for all index >= j
                i, j = s, e
                while i < j:
                    if l[i] < p:
                        i += 1
                    elif l[j] >= p:
                        j -= 1
                    else:
                        l[i], l[j] = l[j], l[i]
                l[i], l[e] = l[e], l[i]
                # recurse
                n_le = len(l)-i
                if n_le < k:
                    return rec(l, s, i-1, k)
                if n_le > k:
                    return rec(l, i+1, e, k)
                return l[i]
            return rec(l, 0, len(l)-1, k)

        mid = quick_select(nums, len(nums)//2+1)
        return sum(abs(n-mid) for n in nums)


    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = nums[len(nums)//2]
        return sum(abs(x - n) for x in nums)


@pytest.mark.parametrize('nums, expected', [
    ([1,2,3], 2),
    ([1,10,2,9], 16),
    ([1,0,0,8,6], 14)
])
def test(nums, expected):
    assert expected == Solution().minMoves2(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
