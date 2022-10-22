#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a triple booking.

Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true
Explanation:
The first two events can be booked.  The third event can be double booked.
The fourth event (5, 15) can't be booked, because it would result in a triple booking.
The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.

Note:

	The number of calls to MyCalendar.book per test case will be at most 1000.
	In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
"""
import sys
import pytest


class MyCalendarTwo:
    def __init__(self):
        self.root = None

    def overlap(self, root, node):
        if not root:
            return []
        ret = [(root[0][0], root[0][1])] \
            if not (node[0][0] >= root[0][1] or node[0][1] <= root[0][0]) \
            else []
        if root[1] and root[1][0][3] > node[0][0]:
            ret.extend(self.overlap(root[1], node))
        if root[2] and root[2][0][2] < node[0][1]:
            ret.extend(self.overlap(root[2], node))
        return ret

    def insert(self, root, node):
        if not root:
            return
        root[0][2] = min(root[0][2], node[0][2])
        root[0][3] = max(root[0][3], node[0][3])
        if node[0][0] >= root[0][0]:
            if root[1] is None:
                root[1] = node
            else:
                self.insert(root[1], node)
        else:
            if root[2] is None:
                root[2] = node
            else:
                self.insert(root[2], node)

    def are_distinct(self, intervals):
        intervals.sort()
        return all(intervals[i][1] <= intervals[i+1][0] for i in range(len(intervals)-1))

    def book(self, start: int, end: int) -> bool:
        # interval tree keeping start, end, max_start, max_end
        n = [[start, end, start, end], None, None]
        if self.root is None:
            self.root = n
            return True
        overlaps = self.overlap(self.root, n)
        if not self.are_distinct(overlaps):
            return False
        self.insert(self.root, n)
        return True


@pytest.mark.parametrize('commands, args, expecteds', [
    (['book', 'book', 'book', 'book', 'book'], [(10,20),(50,60),(10,40),(5,15),(5,10),(25,55)], [True, True, True, False, True, True]),
    (["book","book","book","book","book","book"], [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]], [True,True,True,False,True,True]),
])
def test(commands, args, expecteds):
    o = MyCalendarTwo()
    for c, a, e in zip(commands, args, expecteds):
        print(a, e)
        assert e == getattr(o, c)(*a)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
