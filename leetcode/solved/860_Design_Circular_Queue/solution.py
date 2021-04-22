#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

	MyCircularQueue(k): Constructor, set the size of the queue to be k.
	Front: Get the front item from the queue. If the queue is empty, return -1.
	Rear: Get the last item from the queue. If the queue is empty, return -1.
	enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
	deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
	isEmpty(): Checks whether the circular queue is empty or not.
	isFull(): Checks whether the circular queue is full or not.

Example:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
circularQueue.enQueue(1);  // return true
circularQueue.enQueue(2);  // return true
circularQueue.enQueue(3);  // return true
circularQueue.enQueue(4);  // return false, the queue is full
circularQueue.Rear();  // return 3
circularQueue.isFull();  // return true
circularQueue.deQueue();  // return true
circularQueue.enQueue(4);  // return true
circularQueue.Rear();  // return 4

Constraints:

	1 <= k <= 1000
	0 <= value <= 1000
	At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.

Follow up: Could you solve the problem without using the built-in queue?
"""
import sys
import pytest


class MyCircularQueue:
    """Using an Array"""

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
    """Using a CircularLikedList"""
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


@pytest.mark.parametrize('commands, args, expected', [
    (['MyCircularQueue', 'enQueue', 'enQueue', 'enQueue', 'enQueue', 'Rear', 'isFull', 'deQueue', 'enQueue', 'Rear'],
     [[3],[1],[2],[3],[4],[],[],[],[4],[]],
     [None, True, True, True, False, 3, True, True, True, 4]),
    (["MyCircularQueue","enQueue","Rear","Rear","deQueue","enQueue","Rear","deQueue","Front","deQueue","deQueue","deQueue"],
     [[6],[6],[],[],[],[5],[],[],[],[],[],[]],
     [None,True,6,6,True,True,5,True,-1,False,False,False]),
])
def test(commands, args, expected):
    obj = globals()[commands[0]](*args[0])
    actual = [getattr(obj, cmd)(*arg) for cmd, arg in zip(commands[1:], args[1:])]
    assert expected[1:] == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
