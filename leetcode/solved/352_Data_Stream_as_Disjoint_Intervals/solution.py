#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

Implement the SummaryRanges class:

	SummaryRanges() Initializes the object with an empty stream.
	void addNum(int value) Adds the integer value to the stream.
	int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.

Example 1:

Input
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
Output
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

Explanation
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]

Constraints:

	0 <= value <= 104
	At most 3 * 104 calls will be made to addNum and getIntervals.
	At most 102 calls will be made to getIntervals.

Follow up: What if there are lots of merges and the number of disjoint intervals is small compared to the size of the data stream?
"""
import bisect
from typing import List
import pytest
import sys


class SummaryRanges:
    """Oct 11, 2020 19:35"""
    def __init__(self):
        self.d = dict()

    def addNum(self, val: int) -> None:
        if val in self.d:
            return
        if val+1 in self.d and val-1 in self.d:
            self.d[val] = self.d[val-1]
            v = val+1
            while v in self.d and v != self.d[v]:
                v = self.d[v]
            self.d[v] = self.d[val-1]
        elif val+1 in self.d:
            self.d[val] = self.d[val+1]
        elif val-1 in self.d:
            self.d[val] = self.d[val-1]
        else:
            self.d[val] = val

    def find_root(self, v):
        if self.d[v] == v:
            return v
        self.d[v] = self.find_root(self.d[v])
        return self.d[v]

    def getIntervals(self) -> List[List[int]]:
        intervals = dict()
        keys = self.d.keys()
        for k in keys:
            r = self.find_root(k)
            if r not in intervals:
                intervals[r] = [k,k]
            else:
                intervals[r][0] = min(intervals[r][0], k)
                intervals[r][1] = max(intervals[r][1], k)
        return sorted(intervals.values())


class SummaryRanges:
    """Oct 11, 2020 19:53"""
    def __init__(self):
        self.keys = list()
        self.d = dict()

    def addNum(self, val: int) -> None:
        i = bisect.bisect_left(self.keys, val)
        if i-1 >= 0 and self.d[self.keys[i-1]] >= val-1:
            if i < len(self.keys) and self.keys[i] == val+1:
                self.d[self.keys[i-1]] = self.d.pop(self.keys.pop(i))
            else:
                self.d[self.keys[i-1]] = max(self.d[self.keys[i-1]], val)
        else:
            if i < len(self.keys) and self.keys[i] <= val+1:
                self.d[val] = self.d.pop(self.keys[i])
                self.keys[i] = val
            else:
                self.keys.insert(i, val)
                self.d[val] = val

    def getIntervals(self) -> List[List[int]]:
        return [[k, self.d[k]] for k in self.keys]


class SummaryRanges:
    """Mar 12, 2023 18:33"""
    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        def bisearch(arr, v, key=lambda x: x):
            l, r = 0, len(arr)-1
            while l <= r:
                m = l+(r-l)//2
                if key(arr[m]) < v:
                    l = m+1
                else:
                    r = m-1
            return r+1

        i = bisearch(self.intervals, value, lambda x: x[1])
        self.intervals.insert(i, [value, value])

        if i < len(self.intervals)-1:
            if self.intervals[i+1][0] - 1 <= self.intervals[i][1]:
                self.intervals[i+1][0] = min(self.intervals[i+1][0], self.intervals[i][0])
                self.intervals.pop(i)
        if i > 0:
            if self.intervals[i-1][1] + 1 >= self.intervals[i][0]:
                self.intervals[i-1][1] = max(self.intervals[i-1][1], self.intervals[i][1])
                self.intervals.pop(i)

    def getIntervals(self) -> List[List[int]]:
        return self.intervals
        # return [x[:] for x in self.intervals]


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"],
     [[], [1], [], [3], [], [7], [], [2], [], [6], []],
     [None, None, [[1, 1]], None, [[1, 1], [3, 3]], None, [[1, 1], [3, 3], [7, 7]], None, [[1, 3], [7, 7]], None, [[1, 3], [6, 7]]]),
    (["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"],
     [[],[6],[],[6],[],[0],[],[4],[],[8],[],[7],[],[6],[],[4],[],[7],[],[5],[]],
     [None,None,[[6,6]],None,[[6,6]],None,[[0,0],[6,6]],None,[[0,0],[4,4],[6,6]],None,[[0,0],[4,4],[6,6],[8,8]],None,[[0,0],[4,4],[6,8]],None,[[0,0],[4,4],[6,8]],None,[[0,0],[4,4],[6,8]],None,[[0,0],[4,4],[6,8]],None,[[0,0],[4,8]]]),
])
def test(commands, arguments, expecteds):
    obj = globals()[commands.pop(0)](*arguments.pop(0))
    # actuals = []
    for i, (cmd, arg, exp) in enumerate(zip(commands, arguments, expecteds[1:]), 1):
        act = getattr(obj, cmd)(*arg)
        assert exp == act, i
        # actuals.append(act)
    # assert expecteds[1:] == actuals


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
