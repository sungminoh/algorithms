#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

	For example, for arr = [2,3,4], the median is 3.
	For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

	MedianFinder() initializes the MedianFinder object.
	void addNum(int num) adds the integer num from the data stream to the data structure.
	double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:

	-105 <= num <= 105
	There will be at least one element in the data structure before calling findMedian.
	At most 5 * 104 calls will be made to addNum and findMedian.

Follow up:

	If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
	If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""
from pathlib import Path
import json
from heapq import heappushpop
from heapq import heappop
from heapq import heappush
from collections import defaultdict
import sys
import pytest


class MedianFinder:
    """06/16/2020 22:55
    Binary search
    Time complexity:
        addNum: O(logn + n) (insertion is O(n))
        findMedian: O(1)
    Space complexity: O(n)
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.cnt = list()

    def addNum(self, num: int) -> None:
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

    def findMedian(self) -> float:
        return (self.cnt[self.i] + self.cnt[self.j]) / 2


class MedianFinder:
    """06/16/2020 23:13
    Two heaps
    Time complexity:
        addNum: O(logn)
        findMedian: O(1)
    Space complexity: O(n)
    """
    def __init__(self):
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


class MedianFinder:
    """
    Segment tree
    Time complexity:
        addNum: O(logn) on average. (worst case O(n))
        findMedian: O(logn)
    Space complexity: O(distinct n)
    """
    def __init__(self):
        self.tree = None

    def addNum(self, num: int) -> None:
        if not self.tree:
            self.tree = [[num, 1], None, None]
            return

        def _add(tree, v):
            tree[0][1] += 1
            if v < tree[0][0]:
                if not tree[1]:
                    tree[1] = [[v, 1], None, None]
                else:
                    _add(tree[1], v)
            elif v > tree[0][0]:
                if not tree[2]:
                    tree[2] = [[v, 1], None, None]
                else:
                    _add(tree[2], v)

        _add(self.tree, num)

    def findKth(self, k) -> float:
        assert self.tree is not None

        def find(tree, k):
            left = tree[1][0][1] if tree[1] else 0
            total = tree[0][1]
            right = tree[2][0][1] if tree[2] else 0
            if k <= left:
                return find(tree[1], k)
            if k <= total - right:
                return tree[0][0]
            else:
                return find(tree[2], k-(total-right))

        return find(self.tree, k)

    def findMedian(self) -> float:
        assert self.tree is not None
        total = self.tree[0][1]
        if total % 2 == 0:
            return (self.findKth(total//2) + self.findKth(total//2+1)) / 2
        return self.findKth(total//2 + 1)


class MedianFinder:
    """
    Two heaps without duplicates
    Time complexity:
        addNum: O(logn)
        findMedian: O(1)
    Space complexity: O(distinct n)
    """
    def __init__(self):
        self.cnt = defaultdict(int)
        self.l = []
        self.l_cnt = 0
        self.r = []
        self.r_cnt = 0

    def addNum(self, num: int) -> None:
        if not self.l:
            self.l.append(-num)
            self.l_cnt += 1
            self.cnt[num] += 1
            return
        if num <= -self.l[0]:
            self.l_cnt += 1
            if num not in self.cnt:
                heappush(self.l, -num)
        else:
            self.r_cnt += 1
            if num not in self.cnt:
                heappush(self.r, num)
        self.cnt[num] += 1
        while self.l_cnt - self.cnt[self.l[0]] > self.r_cnt:
            n = -heappop(self.l)
            self.l_cnt -= self.cnt[n]
            self.r_cnt += self.cnt[n]
            heappush(self.r, n)
        while self.r_cnt > 0 and self.r_cnt - self.cnt[self.r[0]] > self.l_cnt:
            n = heappop(self.r)
            self.r_cnt -= self.cnt[n]
            self.l_cnt += self.cnt[n]
            heappush(self.l, -n)


    def findMedian(self) -> float:
        if not self.r:
            return -self.l[0]
        if self.l_cnt < self.r_cnt:
            return self.r[0]
        if self.l_cnt > self.r_cnt:
            return -self.l[0]
        else:
            return (-self.l[0] + self.r[0]) / 2


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
     [[], [1], [2], [], [3], []],
     [None, None, None, 1.5, None, 2.0]),
    (["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"],
     [[],[6],[],[10],[],[2],[],[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]],
     [None,None,6.00000,None,8.00000,None,6.00000,None,6.00000,None,6.00000,None,5.50000,None,6.00000,None,5.50000,None,5.00000,None,4.00000,None,3.00000]),
    (["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"],
     [[],[12],[],[10],[],[13],[],[11],[],[5],[],[15],[],[1],[],[11],[],[6],[],[17],[],[14],[],[8],[],[17],[],[6],[],[4],[],[16],[],[8],[],[10],[],[2],[],[12],[],[0],[]],
     [None,None,12.00000,None,11.00000,None,12.00000,None,11.50000,None,11.00000,None,11.50000,None,11.00000,None,11.00000,None,11.00000,None,11.00000,None,11.00000,None,11.00000,None,11.00000,None,11.00000,None,11.00000,None,11.00000,None,11.00000,None,10.50000,None,10.00000,None,10.50000,None,10.00000]),
])
def test(commands, arguments, expecteds):
    print()
    obj = globals()[commands[0]](*arguments[0])
    for cmd, args, exp in zip(commands[1:], arguments[1:], expecteds[1:]):
        assert exp == getattr(obj, cmd)(*args)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
