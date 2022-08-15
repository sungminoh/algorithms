#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

	MyCalendar() Initializes the calendar object.
	boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.

Constraints:

	0 <= start < end <= 109
	At most 1000 calls will be made to book.
"""
import sys
import pytest


class MyCalendar:
    """09/05/2020 01:20"""
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

class MyCalendar:
    """07/25/2021 07:52"""
    class Node:
        def __init__(self, s, e):
            self.s = s
            self.e = e
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        node = self.Node(start, end)
        if not self.root:
            self.root = node
            return True

        def insert(root, node):
            ret = False
            if node.e <= root.s :
                if root.left is None:
                    root.left = node
                    ret = True
                else:
                    ret = insert(root.left, node)
            elif root.e <= node.s:
                if root.right is None:
                    root.right = node
                    ret = True
                else:
                    ret = insert(root.right, node)
            return ret

        return insert(self.root, node)

class MyCalendar:
    """08/14/2022 18:49"""
    def __init__(self):
        self.tree = []

    def book(self, start: int, end: int) -> bool:
        if not self.tree:
            self.tree = [(start, end), None, None]
            return True

        def insert(tree, node):
            if node[1] <= tree[0][0]:
                if tree[1] is None:
                    tree[1] = [node, None, None]
                    return True
                return insert(tree[1], node)
            elif tree[0][1] <= node[0]:
                if tree[2] is None:
                    tree[2] = [node, None, None]
                    return True
                return insert(tree[2], node)
            return False

        return insert(self.tree, (start, end))


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["MyCalendar", "book", "book", "book"],
     [[], [10, 20], [15, 25], [20, 30]],
     [None, True, False, True]),

])
def test(commands, arguments, expecteds):
    obj = globals()[commands.pop(0)](*arguments.pop(0))
    actual = []
    for cmd, arg in zip(commands, arguments):
        actual.append(getattr(obj, cmd)(*arg))
    assert expecteds[1:] == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
