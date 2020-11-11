#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.

Example 1:

┌───┐
│   │
└───┼──>
    │

Input: [2,1,1,2]
Output: true

Example 2:

┌──────┐
│      │
│
│
└────────────>

Input: [1,2,3,4]
Output: false

Example 3:

┌───┐
│   │
└───┼>

Input: [1,1,1,1]
Output: true
"""
import sys
from typing import List
import pytest


class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        # look back up to 6
        for i in range(3, len(x)):
            if x[i] >= x[i-2] and x[i-1] <= x[i-3]:
                # print(0, i)
                return True
            if i == 4:
                if x[i] >= x[i-2]-x[i-4] and x[i-1] == x[i-3]:
                    # print(1, i)
                    return True
            if i >= 5:
                if x[i-2] >= x[i] >= x[i-2]-x[i-4] >= 0 and x[i-3] >= x[i-1] >= x[i-3]-x[i-5] >= 0:
                    # print(2, i)
                    return True
        return False


@pytest.mark.parametrize('x, expected', [
    ([2,1,1,2], True),
    ([1,2,3,4], False),
    ([1,1,1,1], True),
    ([1,1,2,1,1], True),
    ([1,2,2,3,4], False),
    ([3,3,3,2,1,1], False),
    ([1,1,2,2,3,3,4,4,10,4,4,3,3,2,2,1,1], False)
])
def test(x, expected):
    assert expected == Solution().isSelfCrossing(x)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
