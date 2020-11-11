#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

Example 1:

Input: nums = [1,3], n = 6
Output: 1
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].

Example 3:

Input: nums = [1,2,2], n = 5
Output: 0
"""
import sys
from typing import List
import pytest


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        cnt = 0
        m = 0
        i = 1
        j = 0
        while i <= n:
            while j < len(nums) and nums[j] <= i:
                m = max(m, m + nums[j])
                j += 1
                i = m+1
            if m >= n:
                return cnt
            m = 2*m + 1
            cnt += 1
            i = m+1
        return cnt


@pytest.mark.parametrize('nums, n, expected', [
    ([1,3], 6, 1),
    ([1,5,10], 20, 2),
    ([1,2,2], 5, 0),
    ([], 7, 3),
    ([], 8, 4),
])
def test(nums, n, expected):
    assert expected == Solution().minPatches(nums, n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
