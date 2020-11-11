#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

	MyCircularDeque(k): Constructor, set the size of the deque to be k.
	insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
	insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
	deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
	deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
	getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
	getRear(): Gets the last item from Deque. If the deque is empty, return -1.
	isEmpty(): Checks whether Deque is empty or not. 
	isFull(): Checks whether Deque is full or not.

Example:

MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
circularDeque.insertLast(1);			// return true
circularDeque.insertLast(2);			// return true
circularDeque.insertFront(3);			// return true
circularDeque.insertFront(4);			// return false, the queue is full
circularDeque.getRear();  			// return 2
circularDeque.isFull();				// return true
circularDeque.deleteLast();			// return true
circularDeque.insertFront(4);			// return true
circularDeque.getFront();			// return 4

Note:

	All values will be in the range of [0, 1000].
	The number of operations will be in the range of [1, 1000].
	Please do not use the built-in Deque library.
"""
import sys
import pytest


class MyCircularDeque:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.q = [None] * (k+1)
        self.k = k
        self.h = 0
        self.t = 0

    def prev_idx(self, i):
        return self.k if i == 0 else i-1

    def next_idx(self, i):
        return 0 if i == self.k else i+1

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.h = self.prev_idx(self.h)
        self.q[self.h] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.q[self.t] = value
        self.t = self.next_idx(self.t)
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.h = self.next_idx(self.h)
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.t = self.prev_idx(self.t)
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return -1 if self.isEmpty() else self.q[self.h]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return -1 if self.isEmpty() else self.q[self.prev_idx(self.t)]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.t == self.h

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.next_idx(self.t) == self.h


@pytest.mark.parametrize('commands, args, expected', [
    (['MyCircularDeque', 'insertLast', 'insertLast', 'insertFront', 'insertFront', 'getRear', 'isFull', 'deleteLast', 'insertFront', 'getFront'],
     [[3],[1],[2],[3],[4],[],[],[],[4],[]],
     [None,True,True,True,False,2,True,True,True,4]),
    (["MyCircularDeque","insertFront","deleteLast","getRear","getFront","getFront","deleteFront","insertFront","insertLast","insertFront","getFront","insertFront"],
     [[4],[9],[],[],[],[],[],[6],[5],[9],[],[6]],
     [None,True,True,-1,-1,-1,False,True,True,True,9,True])
])
def test(commands, args, expected):
    obj = globals()[commands[0]](*args[0])
    actual = [getattr(obj, c)(*a) for c, a in zip(commands[1:], args[1:])]
    assert expected[1:] == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
