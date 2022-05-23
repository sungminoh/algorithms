#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:

	1 <= nums.length <= 8
	-10 <= nums[i] <= 10
"""
from functools import lru_cache
import sys
import copy
from collections import Counter
from typing import List
import pytest


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """05/22/2022 16:32"""
        def perm(cnt):
            if len(cnt) == 1:
                k, v = cnt.popitem()
                return [[k]*v]
            ret = []
            for k in cnt:
                sub = perm({
                    x: (c if x != k else c-1)
                    for x, c in cnt.items()
                    if (c if x != k else c-1) > 0
                })
                ret.extend([[k, *y] for y in sub])
            return ret

        return perm(Counter(nums))

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """05/22/2022 16:55
        Not to recreate counter
        """
        def perm(cnt):
            if len(cnt) == 1:
                k = next(iter(cnt))
                return [[k]*cnt[k]]
            ret = []
            keys = list(cnt.keys())
            for k in keys:
                if cnt[k] == 0:
                    continue
                cnt[k] -= 1
                if cnt[k] == 0:
                    cnt.pop(k)
                sub = perm(cnt)
                cnt.setdefault(k, 0)
                cnt[k] += 1
                ret.extend([[k, *y] for y in sub])
            return ret

        return perm(Counter(nums))

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """05/22/2022 16:41
        Cache previous result
        """

        class HashableDict(dict):
            def __hash__(self):
                return hash((frozenset(self), frozenset(self.values())))

        @lru_cache(None)
        def perm(cnt: HashableDict):
            if len(cnt) == 1:
                k, v = cnt.popitem()
                return [[k]*v]
            ret = []
            for k in cnt:
                sub = perm(HashableDict({
                    x: (c if x != k else c-1)
                    for x, c in cnt.items()
                    if (c if x != k else c-1) > 0
                }))
                ret.extend([[k, *y] for y in sub])
            return ret

        return perm(HashableDict(Counter(nums)))

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """05/22/2022 19:25
        Backtrack
        """
        nums.sort()

        def dfs(cur, remain):
            if remain == 0:
                return [cur]
            ret = []
            pv = None
            for i in range(len(nums)):
                if pv == nums[i]:
                    continue
                if remain&(1<<i) == 0:
                    continue
                pv = nums[i]
                ret.extend(dfs(cur + [nums[i]], remain^(1<<i)))
            return ret

        return dfs([], (1<<len(nums))-1)


@pytest.mark.parametrize('nums, expected', [
    ([1,1,2], [[1,1,2],[1,2,1],[2,1,1]]),
    ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
])
def test(nums, expected):
    assert sorted(expected) == sorted(Solution().permuteUnique(nums))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
