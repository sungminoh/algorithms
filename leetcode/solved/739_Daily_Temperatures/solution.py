#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature.  If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note:
The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].
"""
import sys
from typing import List
import pytest


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ret = [0]*len(T)
        stack = []
        for j, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                i = stack.pop()
                ret[i] = j-i
            stack.append(j)
        return ret


@pytest.mark.parametrize('T, expected', [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
])
def test(T, expected):
    assert expected == Solution().dailyTemperatures(T)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
