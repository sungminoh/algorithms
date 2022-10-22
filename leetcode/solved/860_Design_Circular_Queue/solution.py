#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

	MyCircularQueue(k) Initializes the object with the size of the queue to be k.
	int Front() Gets the front item from the queue. If the queue is empty, return -1.
	int Rear() Gets the last item from the queue. If the queue is empty, return -1.
	boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
	boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
	boolean isEmpty() Checks whether the circular queue is empty or not.
	boolean isFull() Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in your programming language. 

Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4

Constraints:

	1 <= k <= 1000
	0 <= value <= 1000
	At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
"""
import pytest
import sys


class MyCircularQueue:
    """06/20/2020 15:32
    Using an Array
    """
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = k
        self.queue = [None] * (k + 1)
        self.head = self.tail = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail += 1
        self.tail %= self.size+1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.head += 1
        self.head %= self.size+1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.tail - 1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.tail == self.head

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.tail+1) % (self.size+1) == self.head


class MyCircularQueue:
    """04/21/2021 09:45
    Using a CircularLikedList
    """
    class Node:
        def __init__(self, val, nxt=None):
            self.val = val
            self.nxt = nxt

    def __init__(self, k: int):
        self.k = k
        self.n = 0
        self.h = self.t = self.Node(None)
        for i in range(k):
            nn = self.Node(None)
            self.t.nxt = nn
            self.t = self.t.nxt
        self.t.nxt = self.h
        self.t = self.h

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.t.nxt.val = value
        self.t = self.t.nxt
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.h = self.h.nxt
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.h.nxt.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.t.val

    def isEmpty(self) -> bool:
        return self.h == self.t

    def isFull(self) -> bool:
        return self.t.nxt == self.h


class MyCircularQueue:
    """10/21/2022 17:15"""
    def __init__(self, k: int):
        self.store = [None] * (k+1)
        self.h = 0
        self.t = 0

    def _idx(self, i, d) -> int:
        return (i+d)%len(self.store)

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.store[self.t] = value
        self.t = self._idx(self.t, 1)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.h = self._idx(self.h, 1)
        return True

    def Front(self) -> int:
        return self.store[self.h] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.store[self._idx(self.t, -1)] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.h == self.t

    def isFull(self) -> bool:
        return self._idx(self.t, 1) == self.h


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"],
     [[3], [1], [2], [3], [4], [], [], [], [4], []],
     [None, True, True, True, False, 3, True, True, True, 4]),
    (["MyCircularQueue","enQueue","Rear","Rear","deQueue","enQueue","Rear","deQueue","Front","deQueue","deQueue","deQueue"],
     [[6],[6],[],[],[],[5],[],[],[],[],[],[]],
     [None,True,6,6,True,True,5,True,-1,False,False,False]),
])
def test(commands, arguments, expecteds):
    obj = globals()[commands.pop(0)](*arguments.pop(0))
    actuals = []
    for cmd, arg in zip(commands, arguments):
        actuals.append(getattr(obj, cmd)(*arg))
    assert expecteds[1:] == actuals


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
