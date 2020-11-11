
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Note:

	You may assume the interval's end point is always bigger than its start point.
	Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""
import sys
from typing import List
import pytest


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        ret = 0
        end = -float('inf')
        for s, e in intervals:
            if end <= s:
                end = e
            else:
                end = min(end, e)
                ret += 1
        return ret


@pytest.mark.parametrize('intervals, expected', [
    ([[1,2],[2,3],[3,4],[1,3]], 1),
    ([[1,2],[1,2],[1,2]], 2),
    ([[1,2],[2,3]], 0),
])
def test(intervals, expected):
    assert expected == Solution().eraseOverlapIntervals(intervals)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
