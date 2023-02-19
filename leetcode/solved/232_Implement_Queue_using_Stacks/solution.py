#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

	void push(int x) Pushes element x to the back of the queue.
	int pop() Removes the element from the front of the queue and returns it.
	int peek() Returns the element at the front of the queue.
	boolean empty() Returns true if the queue is empty, false otherwise.

Notes:

	You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
	Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

Example 1:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

Constraints:

	1 <= x <= 9
	At most 100 calls will be made to push, pop, peek, and empty.
	All the calls to pop and peek are valid.

Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
"""
import pytest
import sys


class MyQueue:
    """Feb 19, 2023 15:28"""
    def __init__(self):
        self.instack = []
        self.outstack = []

    def _move(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

    def push(self, x: int) -> None:
        self.instack.append(x)

    def pop(self) -> int:
        self._move()
        return self.outstack.pop()

    def peek(self) -> int:
        self._move()
        return self.outstack[-1]

    def empty(self) -> bool:
        return len(self.instack) + len(self.outstack) == 0


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["MyQueue", "push", "push", "peek", "pop", "empty"],
     [[], [1], [2], [], [], []],
     [None, None, None, 1, 1, False])
])
def test(commands, arguments, expecteds):
    obj = globals()[commands.pop(0)](*arguments.pop(0))
    expecteds.pop(0)
    actuals = []
    for cmd, arg in zip(commands, arguments):
        actuals.append(getattr(obj, cmd)(*arg))
    assert expecteds == actuals



if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
