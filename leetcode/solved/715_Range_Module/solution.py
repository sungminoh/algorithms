#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.

A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

Implement the RangeModule class:

	RangeModule() Initializes the object of the data structure.
	void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
	boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right) is currently being tracked, and false otherwise.
	void removeRange(int left, int right) Stops tracking every real number currently being tracked in the half-open interval [left, right).

Example 1:

Input
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
Output
[null, null, null, true, false, true]

Explanation
RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);
rangeModule.removeRange(14, 16);
rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)

Constraints:

	1 <= left < right <= 109
	At most 104 calls will be made to addRange, queryRange, and removeRange.
"""
import sys
import bisect
import pytest


def bisearch(arr, x, s=0, e=-1, key=lambda v, x: v >= x):
    e = e if e>=0 else (len(arr)-1)
    while s <= e:
        m = s + (e-s)//2
        if key(arr[m], x):
            e = m-1
        else:
            s = m+1
    return e+1


class RangeModule:
    def __init__(self):
        self.arr = []

    def addRange(self, left: int, right: int) -> None:
        if not self.arr:
            self.arr.append([left, right])
            return
        # bisect_left, all intervals on left side don't overlap with the new interval
        i = bisearch(self.arr, left, key=lambda v, x: v[1] >= x)
        # bisect_right, all intervals on right side don't overlap with the new interval
        j = bisearch(self.arr, right, key=lambda v, x: v[0] > x)-1
        left = min(self.arr[i][0] if 0<=i<len(self.arr) else float('inf'), left)
        right = max(self.arr[j][1] if 0<=j<len(self.arr) else -float('inf'), right)
        self.arr[i:j+1] = [[left, right]]

    def queryRange(self, left: int, right: int) -> bool:
        if not self.arr:
            return False
        i = bisearch(self.arr, left, key=lambda v, x: v[1] >= x)
        j = bisearch(self.arr, right, key=lambda v, x: v[0] > x)-1
        return i == j and self.arr[i][0] <= left and self.arr[j][1] >= right

    def removeRange(self, left: int, right: int) -> None:
        if not self.arr:
            return
        i = bisearch(self.arr, left, key=lambda v, x: v[1] >= x)
        j = bisearch(self.arr, right, key=lambda v, x: v[0] > x)-1
        remainders = []
        if i<len(self.arr) and self.arr[i][0] < left:
            remainders.append([self.arr[i][0], left])
        if j<len(self.arr) and self.arr[j][0] <= right < self.arr[j][1]:
            remainders.append([right, self.arr[j][1]])
        self.arr[i:j+1] = remainders


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"],
     [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]],
     [None, None, None, True, False, True]),
    (["RangeModule","addRange","addRange","addRange","queryRange","queryRange","queryRange","removeRange","queryRange"],
     [[],[10,180],[150,200],[250,500],[50,100],[180,300],[600,1000],[50,150],[50,100]],
     [[],None,None,None,True,False,False,None,False]),
    (["RangeModule","addRange","removeRange","removeRange","addRange","removeRange","addRange","queryRange","queryRange","queryRange"],
     [[],[6,8],[7,8],[8,9],[8,9],[1,3],[1,8],[2,4],[2,9],[4,6]],
     [[],None,None,None,None,None,None,True,True,True]),
    (["RangeModule","queryRange","queryRange","addRange","addRange","addRange","queryRange","removeRange","removeRange","removeRange"],
     [[],[1,4],[6,10],[2,6],[2,8],[4,7],[2,5],[1,10],[3,5],[1,2]],
     [[],False,False,[2,6],[2,8],[4,7],[2,5],[1,10],[3,5],[1,2]]),
])
def test(commands, arguments, expecteds):
    obj = RangeModule(*arguments[0])
    for cmd, args, exp in zip(commands[1:], arguments[1:], expecteds[1:]):
        assert exp == getattr(obj, cmd)(*args)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
