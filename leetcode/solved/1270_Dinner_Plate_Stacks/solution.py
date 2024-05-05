#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

import heapq
from pathlib import Path

"""
You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has the same maximum capacity.

Implement the DinnerPlates class:

	DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks capacity.
	void push(int val) Pushes the given integer val into the leftmost stack with a size less than capacity.
	int pop() Returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns -1 if all the stacks are empty.
	int popAtStack(int index) Returns the value at the top of the stack with the given index index and removes it from that stack or returns -1 if the stack with that given index is empty.

Example 1:

Input
["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop"]
[[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []]
Output
[null, null, null, null, null, null, 2, null, null, 20, 21, 5, 4, 3, 1, -1]

Explanation:
DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5);         // The stacks are now:  2  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 2.  The stacks are now:     4
                                                       1  3  5
                                                       ﹈ ﹈ ﹈
D.push(20);        // The stacks are now: 20  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.push(21);        // The stacks are now: 20  4 21
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
                                                        1  3  5
                                                        ﹈ ﹈ ﹈
D.popAtStack(2);   // Returns 21.  The stacks are now:     4
                                                        1  3  5
                                                        ﹈ ﹈ ﹈
D.pop()            // Returns 5.  The stacks are now:      4
                                                        1  3
                                                        ﹈ ﹈
D.pop()            // Returns 4.  The stacks are now:   1  3
                                                        ﹈ ﹈
D.pop()            // Returns 3.  The stacks are now:   1
                                                        ﹈
D.pop()            // Returns 1.  There are no stacks.
D.pop()            // Returns -1.  There are still no stacks.

Constraints:

	1 <= capacity <= 2 * 104
	1 <= val <= 2 * 104
	0 <= index <= 105
	At most 2 * 105 calls will be made to push, pop, and popAtStack.
"""
import json
import pytest
import sys


class DinnerPlates:
    """TLE"""
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.i = 0

    def push(self, val: int) -> None:
        if self.i == len(self.stacks):
            self.stacks.append([])
        self.stacks[self.i].append(val)
        while self.i < len(self.stacks) and len(self.stacks[self.i]) == self.capacity:
            self.i += 1

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        if not self.stacks:
            return -1
        ret = self.stacks[-1].pop()
        if len(self.stacks)-1 < self.i:
            self.i = len(self.stacks)-1
        if not self.stacks[-1]:
            self.stacks.pop()
        return ret

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks):
            return -1
        if not self.stacks[index]:
            return -1
        ret = self.stacks[index].pop()
        if index == len(self.stacks)-1 and not self.stacks[-1]:
            self.stacks.pop()
        if index < self.i:
            self.i = index
        return ret


class DinnerPlates:
    """May 04, 2024 19:03"""
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.h = []

    def clear_heap(self):
        while self.h and (self.h[0] >= len(self.stacks) or len(self.stacks[self.h[0]]) == self.capacity):
            heapq.heappop(self.h)

    def clear_stack(self):
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

    def push(self, val: int) -> None:
        self.clear_heap()
        if not self.h:
            heapq.heappush(self.h, len(self.stacks))
            self.stacks.append([])
        self.stacks[self.h[0]].append(val)

    def pop(self) -> int:
        self.clear_stack()
        if not self.stacks:
            return -1
        ret = self.stacks[-1].pop()
        self.clear_stack()
        if self.stacks and len(self.stacks[-1]) == self.capacity-1:
            heapq.heappush(self.h, len(self.stacks)-1)
        return ret

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks):
            return -1
        if not self.stacks[index]:
            return -1
        if index == len(self.stacks) - 1:
            return self.pop()
        ret = self.stacks[index].pop()
        if len(self.stacks[index]) == self.capacity-1:
            heapq.heappush(self.h, index)
        return ret



@pytest.mark.parametrize('args', [
    ((["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop"],
      [[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []],
      [None, None, None, None, None, None, 2, None, None, 20, 21, 5, 4, 3, 1, -1])),
    ((["DinnerPlates","push","push","push","popAtStack","pop","pop"],
      [[1],[1],[2],[3],[1],[],[]],
      [None, None, None, None, 2, 3, 1])),
    ((["DinnerPlates","push","push","popAtStack","pop","push","push","pop","pop"],
      [[1],[1],[2],[1],[],[1],[2],[],[]],
      [None, None, None, 2, 1, None, None, 2, 1])),
    ((*json.load(open(Path(__file__).parent/'testcase.json')),
      )),
])
def test(args):
    commands, arguments, expecteds = args
    obj = globals()[commands[0]](*arguments[0])
    actual = [None]
    for cmd, arg in zip(commands[1:], arguments[1:]):
        actual.append(getattr(obj, cmd)(*arg))

    assert expecteds == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
