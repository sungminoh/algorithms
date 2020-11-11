#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
56. Merge Intervals
DescriptionHintsSubmissionsDiscussSolution
DiscussPick One
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '(%s, %s)' % (self.start, self.end)


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals = list(sorted(intervals, key=lambda x: x.start))
        ret = []
        interval = intervals[0]
        for i in range(1, len(intervals)):
            x = intervals[i]
            if x.start <= interval.end:
                interval.end = max(interval.end, x.end)
            else:
                ret.append(interval)
                interval = x
        ret.append(interval)
        return ret


def main():
    intervals = []
    s = list(map(int, input().split()))
    while s:
        intervals.append(Interval(*s))
        s = list(map(int, input().split()))
    print(Solution().merge(intervals))


if __name__ == '__main__':
    main()
