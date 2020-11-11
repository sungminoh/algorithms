
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.

Example 1:

Input: ["23:59","00:00"]
Output: 1

Note:

The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
"""
import sys
from typing import List
import pytest


def convert(s):
    h, m = map(int, s.split(':'))
    return 60*h + m


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePointsSet = set(timePoints)
        if len(timePoints) != len(timePointsSet):
            return 0
        ts = sorted(convert(t) for t in set(timePointsSet))
        ts.append(ts[0] + 1440)
        return min(ts[i+1] - ts[i] for i in range(len(ts)-1))


@pytest.mark.parametrize('timePoints, expected', [
    (["23:59","00:00"], 1),
    (["00:00","23:59","00:00"], 0),
    (["05:31","22:08","00:35"], 147),
])
def test(timePoints, expected):
    assert expected == Solution().findMinDifference(timePoints)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
