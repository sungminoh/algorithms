
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

 Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:

Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example 2:

Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.

Note:

The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.
"""
from functools import lru_cache
import sys
from typing import List
import pytest


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if len(nums) < 4:
            return False
        s, r = divmod(sum(nums), 4)
        if r != 0:
            return False

        nums.sort(reverse=True)

        sides = [s] * 4
        def dfs(i):
            if i == len(nums):
                return True
            for j in range(len(sides)):
                if nums[i] > sides[j]:
                    continue
                sides[j] -= nums[i]
                if dfs(i + 1):
                    return True
                sides[j] += nums[i]
            return False

        return dfs(0)

    def _makesquare(self, nums: List[int]) -> bool:
        if len(nums) < 4:
            return False
        s, r = divmod(sum(nums), 4)
        if r != 0:
            return False

        @lru_cache(None)
        def use_to_make(used, n):
            if n == 0:
                yield from [used]
            if used == (1 << (len(nums) + 1)) - 1:
                yield from []
            for i in range(len(nums)):
                if used & 1 << i:
                    continue
                b = 1 << i
                used |= b
                yield from use_to_make(used, n - nums[i])
                used -= b

        @lru_cache(None)
        def can_devide_into_n_group(used, k):
            if k == 0:
                return True

            for u in use_to_make(used, s):
                if can_devide_into_n_group(u, k - 1):
                    return True
            return False

        return can_devide_into_n_group(1 << len(nums), 4)


@pytest.mark.parametrize('nums, expected', [
    ([1,1,2,2,2], True),
    ([3,3,3,3,4], False),
    ([5,5,5,5,4,4,4,4,3,3,3,3], True),
    ([1569462,2402351,9513693,2220521,7730020,7930469,1040519,5767807,876240,350944,4674663,4809943,8379742,3517287,8034755], False),
])
def test(nums, expected):
    assert expected == Solution().makesquare(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
