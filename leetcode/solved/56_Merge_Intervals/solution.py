#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:

	1 <= intervals.length <= 104
	intervals[i].length == 2
	0 <= starti <= endi <= 104
"""
import sys
from typing import List
import pytest


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ret = []
        cur = intervals[0]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s > cur[1]:
                ret.append(cur)
                cur = [s, e]
            else:
                cur[1] = max(cur[1], e)
        ret.append(cur)

        return ret


@pytest.mark.parametrize('intervals, expected', [
    ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    ([[1,4],[4,5]], [[1,5]]),
])
def test(intervals, expected):
    assert expected == Solution().merge(intervals)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
