#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

	FreqStack() constructs an empty frequency stack.
	void push(int val) pushes an integer val onto the top of the stack.
	int pop() removes and returns the most frequent element in the stack.

		If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

Example 1:

Input
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output
[null, null, null, null, null, null, null, 5, 7, 5, 4]

Explanation
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].

Constraints:

	0 <= val <= 109
	At most 2 * 104 calls will be made to push and pop.
	It is guaranteed that there will be at least one element in the stack before calling pop.
"""
from collections import defaultdict
import sys
import pytest


class FreqStack:
    """
    Use heap to get the most frequent one
    Counter has a pointer to the corresponding element in the heap
    Every push and pop, change counter and heapify
    Heap is sorted by (freq, last index) in descending order
    """
    def __init__(self):
        self.cnt = 0
        self.counter = {}
        self.index = {}
        self.heap = []

    def push(self, val: int) -> None:
        """
        Time complexity: O(logn)
        """
        if val not in self.counter:
            self.counter[val] = [-1, -self.cnt, [self.cnt], val]
            self.index[val] = len(self.heap)
            self.heap.append(self.counter[val])
        else:
            self.counter[val][0] -= 1
            self.counter[val][1] = -self.cnt
            self.counter[val][2].append(self.cnt)
        self._heapup(self.index[val])
        self.cnt += 1

    def _heapup(self, i):
        p = (i-1)//2
        while p >= 0 and self.heap[p] > self.heap[i]:
            self._heapswap(p, i)
            i = p
            p = (i-1)//2

    def _heapswap(self, i, j):
        self.heap[j], self.heap[i] = self.heap[i], self.heap[j]
        self.index[self.heap[j][-1]] = j
        self.index[self.heap[i][-1]] = i

    def _heapdown(self, i):
        l = 2*i+1
        r = 2*i+2
        if l < len(self.heap) \
                and (r >= len(self.heap) or self.heap[l] < self.heap[r]) \
                and self.heap[l] < self.heap[i]:
            self._heapswap(l, i)
            self._heapdown(l)
        elif r < len(self.heap) \
                and (l >= len(self.heap) or self.heap[r] < self.heap[l]) \
                and self.heap[r] < self.heap[i]:
            self._heapswap(r, i)
            self._heapdown(r)

    def _heapclean(self):
        while self.heap and self.heap[-1][0] == 0:
            _, _, _, val = self.heap.pop()
            self.index.pop(val)
            self.counter.pop(val)

    def pop(self) -> int:
        """
        Time complexity: O(logn)
        """
        ret = self.heap[0][-1]
        self.heap[0][0] += 1
        self.heap[0][2].pop()
        self.heap[0][1] = -self.heap[0][2][-1] if self.heap[0][2] else 1
        if self.heap[0][0] == 0:
            self._heapswap(0, len(self.heap)-1)
        self._heapdown(0)
        self._heapclean()
        return ret


class FreqStack:
    """cheat"""
    def __init__(self):
        self.counter = defaultdict(int)
        self.freq_stack = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        """
        Time complexity: O(1)
        """
        self.counter[val] += 1
        self.freq_stack[self.counter[val]].append(val)
        self.max_freq = max(self.max_freq, self.counter[val])

    def pop(self) -> int:
        """
        Time complexity: O(1)
        """
        ret = self.freq_stack[self.max_freq].pop()
        if not self.freq_stack[self.max_freq]:
            self.max_freq -= 1
        self.counter[ret] -= 1
        return ret


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"],
     [[], [5], [7], [5], [7], [4], [5], [], [], [], []],
     [None, None, None, None, None, None, None, 5, 7, 5, 4]),
    (["FreqStack","push","push","push","push","push","push","pop","push","pop","push","pop","push","pop","push","pop","pop","pop","pop","pop","pop"],
     [[],[4],[0],[9],[3],[4],[2],[],[6],[],[1],[],[1],[],[4],[],[],[],[],[],[]],
     [None, None, None, None, None, None, None, 4,None,6,None,1,None,1,None,4,2,3,9,0,4]),
    (["FreqStack","push","push","push","push","push","push","push","push","push","push","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop"],
     [[],[1],[0],[0],[1],[5],[4],[1],[5],[1],[6],[],[],[],[],[],[],[],[],[],[]],
     [None,None,None,None,None,None,None,None,None,None,None,1,1,5,1,0,6,4,5,0,1]),
])
def test(commands, arguments, expecteds):
    obj = FreqStack(*arguments[0])
    for cmd, args, exp in zip(commands[1:], arguments[1:], expecteds[1:]):
        assert exp == getattr(obj, cmd)(*args)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
