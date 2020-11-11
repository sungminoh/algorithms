#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
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
"""

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '[%s, %s]' % (self.start, self.end)


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        s = bisearch(intervals, newInterval, key=lambda a, b: a.end < b.start)
        e = bisearch(intervals, newInterval, key=lambda a, b: a.start <= b.end)
        if s >= len(intervals):
            return intervals + [newInterval]
        elif e <= 0:
            return [newInterval] + intervals
        else:
            n = Interval(min(intervals[s].start, newInterval.start), max(intervals[e-1].end, newInterval.end))
            return intervals[:s] + [n] + intervals[e:]

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


def main():
    intervals = []
    line = input()
    while line:
        intervals.append(Interval(*(int(x) for x in line.split())))
        line = input()

    print(Solution().insert(intervals[:-1], intervals[-1]))


if __name__ == '__main__':
    main()
