
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Example 1:

Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.

Example 2:

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Example 3:

Input: [1,2,3,4,5,6,7,8,9]
Output: 2

Follow up:
Can you do it in O(n) time?
"""
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        def wiggle(sign):
            arr = []
            for n in nums:
                if not arr:
                    arr.append(n)
                    continue
                if sign * (n - arr[-1]) > 0:
                    arr.append(n)
                    sign *= -1
                else:
                    assert False
            return arr

        pos = wiggle(1)
        neg = wiggle(-1)
        return max(len(pos), len(neg))

    def _wiggleMaxLength(self, nums: List[int]) -> int:
        @lru_cache(None)
        def _rec(i, sign):
            if i == 0:
                return [nums[i]]
            max_arr = []
            for j in range(i-1, -1, -1):  # i-1 ... 0
                if j + 2 <= len(max_arr):
                    break
                arr = _rec(j, -sign)
                if sign * (nums[i] - arr[-1]) > 0:
                    arr = arr + [nums[i]]
                else:
                    arr = [nums[i]]
                max_arr = max(max_arr, arr, key=len)
            return max_arr

        m = []
        for i in range(len(nums)):
            pos = _rec(i, 1)
            neg = _rec(i, -1)
            # print(pos, neg)
            m = max(m, pos, neg, key=len)
        return len(m)


@pytest.mark.parametrize('nums, expected', [
    ([1,7,4,9,2,5], 6),
    ([1,17,5,10,13,15,10,5,16,8], 7),
    ([1,2,3,4,5,6,7,8,9], 2),
    ([102,224,201,150,79,14,242,235,65,25,224,268,21,295,210,74,199,216,40,93,152,117,235,186,22,204,266,55,170,163], 19)
])
def test(nums, expected):
    print('\n')
    assert expected == Solution().wiggleMaxLength(nums)
