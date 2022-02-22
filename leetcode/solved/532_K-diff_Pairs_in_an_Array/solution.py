#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

	0 <= i, j < nums.length
	i != j
	nums[i] - nums[j] == k

Notice that |val| denotes the absolute value of val.

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:

Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Constraints:

	1 <= nums.length <= 104
	-107 <= nums[i] <= 107
	0 <= k <= 107
"""
from itertools import chain
import sys
from collections import defaultdict
from collections import Counter
from typing import List
import pytest


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """12/15/2020 18:12"""
        ret = set()
        s = set()
        for n in nums:
            if n-k in s:
                ret.add((n-k, n))
            if n+k in s:
                ret.add((n, n+k))
            s.add(n)
        return len(ret)

    def findPairs(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(set)
        visited = set()
        ret = 0
        for i, n in enumerate(nums):
            for j in chain(cnt[n+k], cnt[n-k]):
                pair = tuple(sorted([nums[j], nums[i]]))
                if j != i and pair not in visited:
                    visited.add(pair)
                    ret += 1
            cnt[n].add(i)

        return ret


@pytest.mark.parametrize('nums, k, expected', [
    ([3,1,4,1,5], 2, 2),
    ([1,2,3,4,5], 1, 4),
    ([1,3,1,5,4], 0, 1),
    ([1,2,4,4,3,3,0,9,2,3], 3, 2),
])
def test(nums, k, expected):
    assert expected == Solution().findPairs(nums, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
