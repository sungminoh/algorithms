#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

	void push(int x) Pushes element x to the top of the stack.
	int pop() Removes the element on the top of the stack and returns it.
	int top() Returns the element on the top of the stack.
	boolean empty() Returns true if the stack is empty, false otherwise.

Notes:

	You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
	Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

Constraints:

	1 <= x <= 9
	At most 100 calls will be made to push, pop, top, and empty.
	All the calls to pop and top are valid.

Follow-up: Can you implement the stack using only one queue?
"""
import sys
from collections import deque
import pytest


class MyStack:
    def __init__(self):
        self.queues = [deque(), deque()]
        self.idx = 0

    def push(self, x: int) -> None:
        self.queues[self.idx].append(x)

    def pop(self) -> int:
        while len(self.queues[self.idx])>1:
            self.queues[(self.idx+1)%2].append(self.queues[self.idx].popleft())
        ret = self.queues[self.idx].popleft()
        self.idx = (self.idx+1)%2
        return ret

    def top(self) -> int:
        ret = self.pop()
        self.queues[self.idx].append(ret)
        return ret

    def empty(self) -> bool:
        return all(len(q) == 0 for q in self.queues)


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["MyStack", "push", "push", "top", "pop", "empty"],
     [[], [1], [2], [], [], []],
     [None, None, None, 2, 2, False]),
])
def test(commands, arguments, expecteds):
    obj = globals()[commands.pop(0)](*arguments.pop(0))
    actuals = []
    for cmd, arg in zip(commands, arguments):
        actuals.append(getattr(obj, cmd)(*arg))
    assert expecteds[1:] == actuals


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
