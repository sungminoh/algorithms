#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
import sys
from typing import List
import pytest


def bs(arr, v, key=lambda x, y: x < y):
    s, e = 0, len(arr)-1
    while s <= e:
        m = (s+e)//2
        if key(arr[m], v):
            s = m + 1
        else:
            e = m - 1
    return e + 1


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        s = bs(intervals, newInterval, key=lambda x, y: x[1] < y[0])
        ret.extend(intervals[:s])
        e = bs(intervals, newInterval, key=lambda x, y: x[0] <= y[1])
        if s < e:
            ret.append([min(newInterval[0], intervals[s][0]), max(newInterval[1], intervals[e-1][1])])
        else:
            ret.append(newInterval)
        ret.extend(intervals[e:])
        return ret

    def _insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            ret.append(intervals[i])
            i += 1
        merged = newInterval[:]
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            merged[0] = min(merged[0], intervals[i][0])
            merged[1] = max(merged[1], intervals[i][1])
            i += 1
        ret.append(merged)
        while i < len(intervals):
            ret.append(intervals[i])
            i += 1
        return ret


@pytest.mark.parametrize('intervals, newInterval, expected', [
    ([[1,3],[6,9]], [2,5], [[1,5],[6,9]]),
    ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], [[1,2],[3,10],[12,16]]),
    ([], [5,7], [[5,7]]),
])
def test(intervals, newInterval, expected):
    assert expected == Solution().insert(intervals, newInterval)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
