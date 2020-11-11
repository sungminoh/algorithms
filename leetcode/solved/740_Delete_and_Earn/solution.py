#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

Example 1:

Input: nums = [3, 4, 2]
Output: 6
Explanation:
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.

Example 2:

Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation:
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.

Note:

	The length of nums is at most 20000.
	Each element nums[i] is an integer in the range [1, 10000].
"""
from functools import lru_cache
import sys
from collections import Counter
from typing import List
import pytest


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        keys = sorted(cnt.keys())

        @lru_cache(None)
        def rec(i, used=False):
            if i < 0:
                return 0
            k = keys[i]
            if k-1 not in cnt:
                ret = k*cnt[k] + rec(i-1, False)
            else:
                # not use the current key
                ret = rec(i-1, False)
                save = cnt[k-1]
                cnt[k-1] = 0
                ret = max(ret, k*cnt[k] + rec(i-1, True))
                cnt[k-1] = save
            return ret

        return rec(len(keys)-1)

    def _deleteAndEarn(self, nums: List[int]) -> int:
        """ Wrong """
        cnt = Counter(nums)
        keys = sorted(cnt.keys(), key=lambda x: x*cnt[x], reverse=True)
        for k in keys:
            print(k, cnt[k])
        ret = 0
        visited = set()
        for k in keys:
            if k in visited:
                continue
            ret += k*cnt[k]
            visited.add(k-1)
            visited.add(k+1)
        return ret


@pytest.mark.parametrize('nums, expected', [
    ([3, 4, 2], 6),
    ([2, 2, 3, 3, 3, 4], 9),
    ([8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4], 61)
])
def test(nums, expected):
    assert expected == Solution().deleteAndEarn(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
