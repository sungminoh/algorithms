#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


import pytest
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = []
        idx = {}
        for n in nums:
            if n not in idx:
                idx[n] = len(cnt)
                cnt.append([n, 1])
            else:
                i = idx[n]
                cnt[i][1] += 1
                while i > 0 and cnt[i-1][1] < cnt[i][1]:
                    cnt[i-1], cnt[i] = cnt[i], cnt[i-1]
                    idx[cnt[i][0]] = i
                    i -= 1
                idx[n] = i
            print(cnt)
        return [x[0] for x in cnt[:k]]


@pytest.mark.parametrize('nums, k, expected', [
    ([1,1,1,2,2,3], 2, [1,2]),
    ([1], 1, [1]),
    ([1,2,3,4,1,2,3,1,2,1], 3, [1,2,3]),
    ([5,3,1,1,1,3,73,1], 1, [1])
])
def test(nums, k, expected):
    assert Solution().topKFrequent(nums, k) == expected
