#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
341. Flatten Nested List Iterator
Medium

1462

598

Add to List

Share
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,4,6].
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
import pytest

class NestedInteger:
    def __init__(self, v):
        self.v = v

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return isinstance(self.v, int)

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self.v

    def getList(self) -> ['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self.v


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.lst = nestedList
        self.nxt = None
        self.update()

    def update(self):
        if self.nxt and isinstance(self.nxt, NestedIterator):
            if self.nxt.hasNext():
                return
        if not self.lst:
            self.nxt = None
        else:
            nestedInterger = self.lst.pop(0)
            if nestedInterger.isInteger():
                self.nxt = nestedInterger
            else:
                nestedIterator = NestedIterator(nestedInterger.getList())
                if not nestedIterator.hasNext():
                    self.update()
                else:
                    self.nxt = nestedIterator

    def next(self) -> int:
        if isinstance(self.nxt, NestedInteger):
            v = self.nxt.getInteger()
        elif self.nxt.hasNext():
            v = self.nxt.next()
        self.update()
        return v

    def hasNext(self) -> bool:
        return self.nxt and (isinstance(self.nxt, NestedInteger) or self.nxt.hasNext())


@pytest.mark.parametrize('nestedList, expected', [
    ([NestedInteger(i) for i in range(10)],
     [0,1,2,3,4,5,6,7,8,9]),
    ([NestedInteger([NestedInteger(i*j) for j in range(3)]) for i in range(3)],
     [0, 0, 0, 0, 1, 2, 0, 2, 4]),
    ([NestedInteger([NestedInteger(i*j) for j in range(3)]
                    if i % 2 != 0
                    else i)
      for i in range(8)],
     [0,0,1,2,2,0,3,6,4,0,5,10,6,0,7,14]),
    ([NestedInteger([])], []),
    ([NestedInteger([]),NestedInteger([NestedInteger(3)])], [3])
])
def test(nestedList, expected):
    actual = []
    it = NestedIterator(nestedList)
    while it.hasNext():
        actual.append(it.next())
    print(actual)
    assert expected == actual


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
