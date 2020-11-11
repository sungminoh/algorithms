#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation:
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.

Note:

	The number of calls to MyCalendar.book per test case will be at most 1000.
	In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
"""
import sys
import pytest


class MyCalendar:
    def __init__(self):
        self.tree = None

    def book(self, start: int, end: int) -> bool:
        e = [(start, end), None, None]
        if self.tree is None:
            self.tree = e
            return True
        node = self.tree
        while node:
            if end <= node[0][0]:
                if not node[1]:
                    node[1] = e
                    return True
                else:
                    node = node[1]
            elif start >= node[0][1]:
                if not node[2]:
                    node[2] = e
                    return True
                else:
                    node = node[2]
            else:
                return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


@pytest.mark.parametrize('commands, args, expecteds', [
    (['book', 'book', 'book'], [(10, 20), (15, 25), (20, 30)], [True, False, True])
])
def test(commands, args, expecteds):
    o = MyCalendar()
    for c, a, e in zip(commands, args, expecteds):
        assert e == getattr(o, c)(*a)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
