#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k events.)

You are given some events [startTime, endTime), after each given event, return an integer k representing the maximum k-booking between all the previous events.

Implement the MyCalendarThree class:

	MyCalendarThree() Initializes the object.
	int book(int startTime, int endTime) Returns an integer k representing the largest integer such that there exists a k-booking in the calendar.

Example 1:

Input
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, 1, 1, 2, 3, 3, 3]

Explanation
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // return 1
myCalendarThree.book(50, 60); // return 1
myCalendarThree.book(10, 40); // return 2
myCalendarThree.book(5, 15); // return 3
myCalendarThree.book(5, 10); // return 3
myCalendarThree.book(25, 55); // return 3

Constraints:

	0 <= startTime < endTime <= 109
	At most 400 calls will be made to book.
"""
import bisect
import heapq
from collections import deque
from typing import List
import pytest
import sys


def easy_find(node, start, end):
    def iter_nodes(node):
        if node:
            yield node.val[:2]
            yield from iter_nodes(node.left)
            yield from iter_nodes(node.right)
    return sorted([[s, e] for s, e in iter_nodes(node) if not (e<=start or end<=s)])


class MyCalendarThree:
    """
    Interval tree. Find all overlapping intervals and count maximum overlaps
    """
    class TreeNode:
        def __init__(self, val, left=None, right=None, ):
            self.val = val
            self.left = left
            self.right = right

    def __init__(self):
        self.tree = None
        self.max_overlaps = 0

    def find_overlaps(self, startTime, endTime):
        def find(node, start, end):
            if not node or start == end:
                return []
            ret = [node.val[:2]] if not (end<=node.val[0] or node.val[1]<=start) else []
            if node.left and node.left.val[2] > start:
                ret.extend(find(node.left, start, end))
            if node.right:
                ret.extend(find(node.right , max(start, node.val[0]), end))

            return ret

        return find(self.tree, startTime, endTime)

    def count_overlaps(self, intervals):
        ret = 0
        heap = []
        for s, e in sorted(intervals):
            while heap and heap[0] <= s:
                heapq.heappop(heap)
            heapq.heappush(heap, e)
            ret = max(ret, len(heap))
        return ret

    def book(self, startTime: int, endTime: int) -> int:
        def insert(node, start, end):
            if not node:
                return self.TreeNode([start, end, end])
            else:
                node.val[2] = max(node.val[2], end)
                if start < node.val[0]:
                    node.left = insert(node.left, start, end)
                else:
                    node.right = insert(node.right, start, end)
                return node

        self.tree = insert(self.tree, startTime, endTime)
        overlapping_intervals = self.find_overlaps(startTime, endTime)
        self.max_overlaps = max(self.max_overlaps, self.count_overlaps(overlapping_intervals))
        return self.max_overlaps


class MyCalendarThree:
    """10/22/2022 00:16
    Only need to consider the start time and the end time
    """
    def __init__(self):
        # list of (time, the number of overlapping schedules at the time)
        self.sorted_list = [[0, 0]]  # dummy
        self.max_overlaps = 0

    def insert_event(self, t):
        i = bisect.bisect_left(self.sorted_list, t, key=lambda x: x[0])
        if not (i < len(self.sorted_list) and self.sorted_list[i][0] == t):
            self.sorted_list.insert(i, [t, self.sorted_list[i-1][1]])
        return i

    def book(self, startTime: int, endTime: int) -> int:
        s = self.insert_event(startTime)
        e = self.insert_event(endTime)
        for i in range(s, e):
            self.sorted_list[i][1] += 1
            self.max_overlaps = max(self.max_overlaps, self.sorted_list[i][1])
        return self.max_overlaps


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["MyCalendarThree", "book", "book", "book", "book", "book", "book"],
     [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]],
     [None, 1, 1, 2, 3, 3, 3]),
    (["MyCalendarThree","book","book","book","book","book","book","book","book","book","book"],
     [[],[26,35],[26,32],[25,32],[18,26],[40,45],[19,26],[48,50],[1,6],[46,50],[11,18]],
     [None,1,2,3,3,3,3,3,3,3,3]),
    (["MyCalendarThree","book","book","book","book","book","book","book","book","book","book"],
     [[],[24,40],[43,50],[27,43],[5,21],[30,40],[14,29],[3,19],[3,14],[25,39],[6,19]],
     [None,1,1,2,2,3,3,3,3,4,4]),
    (["MyCalendarThree","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book"],
     [[],[47,50],[1,10],[27,36],[40,47],[20,27],[15,23],[10,18],[27,36],[17,25],[8,17],[24,33],[23,28],[21,27],[47,50],[14,21],[26,32],[16,21],[2,7],[24,33],[6,13],[44,50],[33,39],[30,36],[6,15],[21,27],[49,50],[38,45],[4,12],[46,50],[13,21]],
     [None,1,1,1,1,1,2,2,2,3,3,3,4,5,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7]),
    (["MyCalendarThree","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book"],
     [[],[97,100],[51,65],[27,46],[90,100],[20,32],[15,28],[60,73],[77,91],[67,85],[58,72],[74,93],[73,83],[71,87],[97,100],[14,31],[26,37],[66,76],[52,67],[24,43],[6,23],[94,100],[33,44],[30,46],[6,20],[71,87],[49,59],[38,55],[4,17],[46,61],[13,31],[94,100],[47,65],[9,25],[4,20],[2,17],[28,42],[26,38],[72,83],[43,61],[18,35]],
     [None,1,1,1,2,2,3,3,3,3,3,3,4,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,8,9,9,9,9,9,10]),
    (["MyCalendarThree","book"], [[],[0,1000000000]], [None, 1]),
    (["MyCalendarThree","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book"],
     [[],[5,12],[42,50],[4,9],[33,41],[2,7],[16,25],[7,16],[6,11],[13,18],[38,43],[49,50],[6,15],[5,13],[35,42],[19,24],[46,50],[39,44],[28,36],[28,37],[20,29],[41,49],[11,19],[41,46],[28,37],[17,23],[22,31],[4,10],[31,40],[4,12],[19,26]],
     [None,1,1,2,2,3,3,3,4,4,4,4,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,8,8]),
])
def test(commands, arguments, expecteds):
    obj = globals()[commands.pop(0)](*arguments.pop(0))
    actual = []
    for cmd, arg in zip(commands, arguments):
        actual.append(getattr(obj, cmd)(*arg))
    print()
    print(actual)
    assert expecteds[1:] == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
