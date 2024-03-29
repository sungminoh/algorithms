#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.

Example 1:

Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.

Example 2:

Input: colors = "abc", neededTime = [1,2,3]
Output: 0
Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.

Example 3:

Input: colors = "aabaa", neededTime = [1,2,3,4,1]
Output: 2
Explanation: Bob will remove the balloons at indices 0 and 4. Each balloons takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.

Constraints:

	n == colors.length == neededTime.length
	1 <= n <= 105
	1 <= neededTime[i] <= 104
	colors contains only lowercase English letters.
"""
from functools import lru_cache
from typing import List
import pytest
import sys


class Solution:
     def minCost(self, colors: str, neededTime: List[int]) -> int:
        """10/21/2022 21:42"""
        if not colors:
            return 0
        ret = 0
        cur = None
        timesum = 0
        maxtime = 0
        for t, c in zip(neededTime, colors):
            if c != cur:
                if maxtime != timesum:  # redundant
                    ret += timesum-maxtime
                cur = c
                maxtime = timesum = t
            else:
                maxtime = max(maxtime, t)
                timesum += t
        if maxtime != timesum:  # redundant
            ret += timesum-maxtime
        return ret

   def minCost(self, colors: str, neededTime: List[int]) -> int:
       """Jan 27, 2024 15:00"""
        ret = 0
        i = 0
        while i < len(colors):
            max_cost = 0
            j = i
            while j < len(colors) and colors[j] == colors[i]:
                ret += neededTime[j]
                max_cost = max(max_cost, neededTime[j])
                j += 1
            ret -= max_cost
            i = j
        return ret


@pytest.mark.parametrize('args', [
    (("abaac", [1,2,3,4,5], 3)),
    (("abc", [1,2,3], 0)),
    (("aabaa", [1,2,3,4,1], 2)),
    (("bbbaaa", [4,9,3,8,8,9], 23)),
])
def test(args):
    assert args[-1] == Solution().minCost(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
