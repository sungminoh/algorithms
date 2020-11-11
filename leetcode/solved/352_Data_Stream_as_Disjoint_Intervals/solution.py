#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]

Follow up:

What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
"""
import bisect
import sys
from typing import List
import pytest


class SummaryRanges:
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


class _SummaryRanges:
    def __init__(self):
        """
        Initialize your data structure here.
        """
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


@pytest.mark.parametrize('commands, args, exepcteds', [
    (['SummaryRanges','addNum','getIntervals','addNum','getIntervals','addNum','getIntervals','addNum','getIntervals','addNum','getIntervals'],
     [[None],[1],[],[3],[],[7],[],[2],[],[6],[]],
     [None,None,[[1,1]],None,[[1,1],[3,3]],None,[[1,1],[3,3],[7,7]],None,[[1,3],[7,7]],None,[[1,3],[6,7]]]),
    (["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"],
     [[],[6],[],[6],[],[0],[],[4],[],[8],[],[7],[],[6],[],[4],[],[7],[],[5],[]],
     [None,None,[[6,6]],None,[[6,6]],None,[[0,0],[6,6]],None,[[0,0],[4,4],[6,6]],None,[[0,0],[4,4],[6,6],[8,8]],None,[[0,0],[4,4],[6,8]],None,[[0,0],[4,4],[6,8]],None,[[0,0],[4,4],[6,8]],None,[[0,0],[4,4],[6,8]],None,[[0,0],[4,8]]]),
])
def test(commands, args, exepcteds):
    o = SummaryRanges()
    for c, a, e in zip(commands[1:], args[1:], exepcteds[1:]):
        actual = getattr(o, c)(*a)
        print(actual)
        assert e == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
