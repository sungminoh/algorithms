#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:

	0 <= intervals.length <= 104
	intervals[i].length == 2
	0 <= starti <= endi <= 105
	intervals is sorted by starti in ascending order.
	newInterval.length == 2
	0 <= start <= end <= 105
"""
import bisect
from typing import List
import pytest
import sys


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
    def insert(self, intervals, newInterval):
        """Aug 10, 2018 21:41"""
        def bisearch(lst, x, key=None):
            compare = key or (lambda a, b: a < b)
            l, r = 0, len(lst)
            while l < r:
                i = (l+r)//2
                if compare(lst[i], x):
                    l = i+1
                else:
                    r = i
            return l

        s = bisearch(intervals, newInterval, key=lambda a, b: a[1] < b[0])
        e = bisearch(intervals, newInterval, key=lambda a, b: a[0] <= b[1])
        if s >= len(intervals):
            return intervals + [newInterval]
        elif e <= 0:
            return [newInterval] + intervals
        else:
            n = [min(intervals[s].start, newInterval.start), max(intervals[e-1].end, newInterval.end)]
            return intervals[:s] + [n] + intervals[e:]

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """Aug 20, 2020 23:45"""
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

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """Aug 21, 2020 00:03"""
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

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """Mar 05, 2023 20:13"""
        if not intervals:
            return [newInterval]
        i = bisect.bisect_right(intervals, newInterval)
        intervals.insert(i, newInterval)
        if i > 0 and intervals[i-1][1] >= newInterval[0]:
            i -= 1
        while i+1<len(intervals) and intervals[i][1] >= intervals[i+1][0]:
            intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
            intervals.pop(i+1)
        return intervals


@pytest.mark.parametrize('args', [
    (([[1,3],[6,9]], [2,5], [[1,5],[6,9]])),
    (([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], [[1,2],[3,10],[12,16]])),
    (([[0,5],[9,12]], [7,16], [[0,5],[7,16]]))
])
def test(args):
    assert args[-1] == Solution().insert(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
