#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1

Constraints:

	1 <= intervals.length <= 1000
	intervals[i].length == 2
	0 <= li < ri <= 105
	All the given intervals are unique.
"""
import sys
from typing import List
import pytest


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        covered_cnt = 0
        boundary = -float('inf')
        for s, e in intervals:
            if e <= boundary:
                covered_cnt += 1
            else:
                boundary = e
        return len(intervals)-covered_cnt


@pytest.mark.parametrize('intervals, expected', [
    ([[1,4],[3,6],[2,8]], 2),
    ([[1,4],[2,3]], 1),
    ([[1,2],[1,4],[3,4]], 1)
])
def test(intervals, expected):
    assert expected == Solution().removeCoveredIntervals(intervals)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
