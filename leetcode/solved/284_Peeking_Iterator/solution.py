#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Example:

Assume that the iterator is initialized to the beginning of the list: [1,2,3].

Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.
You call next() the final time and it returns 3, the last element.
Calling hasNext() after that should return false.
Follow up: How would you extend your design to be generic and work with all types, not just integer?
"""
from itertools import chain

# Below is the interface for Iterator, which is already defined for you.
#
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


def main():
    cases = [
        [3,0,6,1,5],
        [3,3,3,3,3],
        [0]
    ]
    for case in cases:
        expected = list(chain(*zip(case, case)))
        # Your PeekingIterator object will be instantiated and called as such:
        iter = PeekingIterator(Iterator(case))
        actual = []
        while iter.hasNext():
            actual.append(iter.peek())  # Get the next element but not advance the iterator.
            actual.append(iter.next())  # Should return the same value as [val].
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')


if __name__ == '__main__':
    main()

