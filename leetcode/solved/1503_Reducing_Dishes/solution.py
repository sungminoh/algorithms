#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.

Example 1:

Input: satisfaction = [-1,-8,0,5,-9]
Output: 14
Explanation: After Removing the second and last dish, the maximum total like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
Each dish is prepared in one unit of time.

Example 2:

Input: satisfaction = [4,3,2]
Output: 20
Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)

Example 3:

Input: satisfaction = [-1,-4,-5]
Output: 0
Explanation: People do not like the dishes. No dish is prepared.

Constraints:

	n == satisfaction.length
	1 <= n <= 500
	-1000 <= satisfaction[i] <= 1000
"""
from functools import lru_cache
from typing import List
import pytest
import sys


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """Apr 23, 2023 21:48"""
        satisfaction.sort()

        @lru_cache(None)
        def dfs(i, t):
            if i == len(satisfaction):
                return 0
            return max(
                satisfaction[i]*t + dfs(i+1, t+1),
                dfs(i+1, t))

        return dfs(0, 1)

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """Apr 23, 2023 21:51"""
        satisfaction.sort()
        i = len(satisfaction)-1

        ret = 0
        cur = 0
        while i >= 0:
            cur += satisfaction[i]
            if cur > 0:
                ret += cur
            else:
                return ret
            i -= 1
        return ret


@pytest.mark.parametrize('args', [
    (([-1,-8,0,5,-9], 14)),
    (([4,3,2], 20)),
    (([-1,-4,-5], 0)),
])
def test(args):
    assert args[-1] == Solution().maxSatisfaction(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
