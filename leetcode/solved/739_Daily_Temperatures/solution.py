#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:

	1 <= temperatures.length <= 105
	30 <= temperatures[i] <= 100
"""
from typing import List
import pytest
import sys


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """09/05/2020 12:23"""
        ret = [0]*len(T)
        stack = []
        for j, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                i = stack.pop()
                ret[i] = j-i
            stack.append(j)
        return ret

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """Nov 20, 2021 11:02
        Time complexity: O(n)
        Space complexity: O(n)
        """
        ret = [0]*len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                ret[j] = i-j
            stack.append(i)
        return ret

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """Feb 19, 2023 16:49"""
        stack = []
        ret = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                ret[j] = i-j
            ret.append(0)
            stack.append(i)
        return ret


@pytest.mark.parametrize('temperatures, expected', [
    ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
    ([30,40,50,60], [1,1,1,0]),
    ([30,60,90], [1,1,0]),
])
def test(temperatures, expected):
    assert expected == Solution().dailyTemperatures(temperatures)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
