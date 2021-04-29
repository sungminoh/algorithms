#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

	NestedIterator(List nestedList) Initializes the iterator with the nested list nestedList.
	int next() Returns the next integer in the nested list.
	boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

Example 1:

Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:

Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

Constraints:

	1 <= nestedList.length <= 500
	The values of the integers in the nested list is in the range [-106, 106].
"""
import sys
from typing import List
import pytest


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, val):
        self.val = val

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return isinstance(self.val, int)

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self.val if self.isInteger() else None

    def getList(self) -> List['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self.val if not self.isInteger() else None

    def __repr__(self) -> str:
        if self.isInteger():
            return str(self.getInteger())
        return f"[{', '.join(repr(x) for x in self.val)}]"


def build(v):
    if isinstance(v, int):
        return NestedInteger(v)
    return NestedInteger([build(x) for x in v])


class NestedIterator:
    """Recusive
    assuming the input is NestedInteger not a list of NestedInteger"""
    def __init__(self, nestedList: NestedInteger):
        self.x = nestedList if nestedList.isInteger() else [NestedIterator(x) for x in nestedList.getList()]
        self.i = 0

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration
        if isinstance(self.x, NestedInteger):
            ret = self.x.getInteger()
            self.x = None
            return ret
        return self.x[self.i].next()

    def hasNext(self) -> bool:
        if self.x is None:
            return False
        if isinstance(self.x, NestedInteger):
            return True
        while self.i < len(self.x) and not self.x[self.i].hasNext():
            self.i += 1
        if self.i < len(self.x):
            return True
        self.x = None
        self.i = 0
        return False


class NestedIterator:
    """Recusive"""
    def __init__(self, nestedList: List[NestedInteger]):
        self.l = nestedList
        self.i = 0
        self.sub = None
        self.nxt = None

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration
        ret = self.nxt
        self.nxt = None
        return ret

    def hasNext(self) -> bool:
        if self.nxt is not None:
            return True
        if self.sub:
            if self.sub.hasNext():
                self.nxt = self.sub.next()
                return True
            self.sub = None
        if self.i == len(self.l):
            return False
        n = self.l[self.i]
        self.i += 1
        if n.isInteger():
            self.nxt = n.getInteger()
            return True
        self.sub = NestedIterator(n.getList())
        return self.hasNext()


class NestedIterator:
    """Recusive"""
    def __init__(self, nestedList: List[NestedInteger]):
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


class NestedIterator:
    """Use stack"""
    def __init__(self, nestedList: List[NestedInteger]):
        self.stack = list(reversed(nestedList))

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration()
        return  self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack and not self.stack[-1].isInteger():
            self.stack.extend(reversed(self.stack.pop().getList()))
        return len(self.stack) > 0


@pytest.mark.parametrize('nestedList, expected', [
    ([[1,1],2,[1,1]], [1,1,2,1,1]),
    ([1,[4,[6]]], [1,4,6]),
    ([0,1,2,3,4,5,6,7,8,9], [0,1,2,3,4,5,6,7,8,9]),
    ([[0,0,0], [0,1,2,], [0,2,4]], [0, 0, 0, 0, 1, 2, 0, 2, 4]),
    ([], []),
    ([[],[],[]], []),
])
def test(nestedList, expected):
    i, actual = NestedIterator([build(x) for x in nestedList]), []
    while i.hasNext(): actual.append(i.next())
    assert expected == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
