
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
For example,

[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

	void addNum(int num) - Add a integer number from the data stream to the data structure.
	double findMedian() - Return the median of all elements so far.

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2

Follow up:

	If all integer numbers from the stream are between 0 and 100, how would you optimize it?
	If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""
from heapq import heappushpop
from heapq import heappop
from heapq import heappush
import sys
import pytest



class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.cnt = list()
        self.l = []
        self.r = []

    def addNum(self, num: int) -> None:
        heappush(self.r, -heappushpop(self.l, -float(num)))
        if len(self.r) > len(self.l):
            heappush(self.l, -heappop(self.r))

    def findMedian(self) -> float:
        if len(self.l) > len(self.r):
            return -self.l[0]
        else:
            return (-self.l[0] + self.r[0]) / 2

    def _addNum(self, num: int) -> None:
        if len(self.cnt) == 0:
            self.cnt.append(num)
            self.i = 0
            self.j = 0
            return

        def binsearch(n):
            cnt = self.cnt
            i, j = 0, len(cnt)-1
            while i <= j:
                m = i + (j-i)//2
                if n < cnt[m]:
                    j = m - 1
                elif n > cnt[m]:
                    i = m + 1
                else:
                    return m
            return i
        idx = binsearch(num)
        self.cnt.insert(idx, num)
        if self.i == self.j:
            self.j += 1
        else:
            self.i += 1

    def _findMedian(self) -> float:
        return (self.cnt[self.i] + self.cnt[self.j]) / 2


@pytest.mark.parametrize('command, args, expected', [
    (["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"], [[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]], [None,None,-1.00000,None,-1.50000,None,-2.00000,None,-2.50000,None,-3.00000]),
    (["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"], [[],[6],[],[10],[],[2],[],[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]], [None,None,6.00000,None,8.00000,None,6.00000,None,6.00000,None,6.00000,None,5.50000,None,6.00000,None,5.50000,None,5.00000,None,4.00000,None,3.00000])
])
def test(command, args, expected):
    obj = globals()[command[0]](*args[0])
    actual = [getattr(obj, cmd)(*arg) for cmd, arg in zip(command[1:], args[1:])]
    assert expected[1:] == actual



if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
