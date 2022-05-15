#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design an iterator that supports the peek operation on an existing iterator in addition to the hasNext and the next operations.

Implement the PeekingIterator class:

	PeekingIterator(Iterator nums) Initializes the object with the given integer iterator iterator.
	int next() Returns the next element in the array and moves the pointer to the next element.
	boolean hasNext() Returns true if there are still elements in the array.
	int peek() Returns the next element in the array without moving the pointer.

Note: Each language may have a different implementation of the constructor and Iterator, but they all support the int next() and boolean hasNext() functions.

Example 1:

Input
["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 2, 2, 3, false]

Explanation
PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
peekingIterator.next();    // return 1, the pointer moves to the next element [1,2,3].
peekingIterator.peek();    // return 2, the pointer does not move [1,2,3].
peekingIterator.next();    // return 2, the pointer moves to the next element [1,2,3]
peekingIterator.next();    // return 3, the pointer moves to the next element [1,2,3]
peekingIterator.hasNext(); // return False

Constraints:

	1 <= nums.length <= 1000
	1 <= nums[i] <= 1000
	All the calls to next and peek are valid.
	At most 1000 calls will be made to next, hasNext, and peek.

Follow up: How would you extend your design to be generic and work with all types, not just integer?
"""
import sys
import pytest


# Below is the interface for Iterator, which is already defined for you.
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return len(self.nums) > 0

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        return self.nums.pop(0)


class PeekingIterator:
    """09/10/2019 22:12"""
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.buffer = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.buffer is None:
            self.buffer = self.iterator.next()
        return self.buffer

    def next(self):
        """
        :rtype: int
        """
        if self.buffer is not None:
            ret = self.buffer
            self.buffer = None
            return ret
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.buffer is not None or self.iterator.hasNext()


# Below is the interface for Iterator, which is already defined for you.
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.cur = 0

    def __iter__(self):
        return iter(self.nums)

    def __next__(self):
        if self.cur < len(self.nums):
            ret = self.nums[self.cur]
            self.cur += 1
            return ret
        raise StopIteration()

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.cur < len(self.nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        return self.__next__()


class PeekingIterator:
    """05/14/2022 17:20"""
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self._move()

    def _move(self):
        if self.it.hasNext():
            self._next_value = self.it.next()
            self._has_next = True
        else:
            self._has_next = False
            self._next_value = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next_value

    def next(self):
        """
        :rtype: int
        """
        ret = self._next_value
        self._move()
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._has_next


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["PeekingIterator", "next", "peek", "next", "next", "hasNext"],
     [[[1, 2, 3]], [], [], [], [], []],
     [None, 1, 2, 2, 3, False]),
])
def test(commands, arguments, expecteds):
    obj = globals()[commands.pop(0)](Iterator(arguments.pop(0)[0]))
    expecteds.pop(0)
    actuals = []
    for cmd, arg, exp in zip(commands, arguments, expecteds):
        actuals.append(getattr(obj, cmd)(*arg))
    assert expecteds == actuals


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
