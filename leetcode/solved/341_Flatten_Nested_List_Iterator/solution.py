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

Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res

If res matches the expected flattened list, then your code will be judged as correct.

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
from collections import deque
import sys
from typing import Iterable
from typing import Any
from typing import Union
from typing import List
import pytest


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value: Union[int, List]):
        self.value: Union[int, List['NestedInteger']]
        if isinstance(value, Iterable):
            self.value = [
                x if isinstance(x, NestedInteger)
                else NestedInteger(x)
                for x in value
            ]
        else:
            self.value = value

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return isinstance(self.value, int)

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self.value if self.isInteger() else None

    def getList(self) -> List['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self.value if not self.isInteger() else None

    def __repr__(self):
        return repr(self.value)


class NestedIterator:
    """04/09/2020 00:22
    Recusive"""
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
    """04/28/2021 09:46
    Recusive"""
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
    """04/28/2021 10:00
    Use stack"""
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


class NestedIterator:
    """05/22/2022 12:09"""
    def __init__(self, nestedList: List[NestedInteger]):
        self.stack = []
        self.stack.extend(reversed(nestedList))

    def next(self) -> int:
        if self.hasNext():
            return self.stack.pop().getInteger()
        raise StopIteration

    def hasNext(self) -> bool:
        while self.stack:
            if self.stack[-1].isInteger():
                return True
            self.stack.extend(reversed(self.stack.pop().getList()))
        return False


@pytest.mark.parametrize('nestedList, expected', [
    ([[1,1],2,[1,1]], [1,1,2,1,1]),
    ([1,[4,[6]]], [1,4,6]),
    ([0,1,2,3,4,5,6,7,8,9], [0,1,2,3,4,5,6,7,8,9]),
    ([[0,0,0], [0,1,2,], [0,2,4]], [0, 0, 0, 0, 1, 2, 0, 2, 4]),
    ([], []),
    ([[],[],[]], []),
])
def test(nestedList, expected):
    actual = []
    it = NestedIterator(NestedInteger(nestedList).getList())
    while it.hasNext():
        actual.append(it.next())
    assert expected == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))

