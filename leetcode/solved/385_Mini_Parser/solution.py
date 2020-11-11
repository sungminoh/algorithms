
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note:
    You may assume that the string is well-formed:

String is non-empty.
String does not contain white spaces.
String contains only digits 0-9, [, - ,, ].

Example 1:

Given s = "324",

You should return a NestedInteger object which contains a single integer 324.

Example 2:

Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
        a. An integer containing value 789.
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
import math
import pytest
from typing import Iterable

class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        if isinstance(value, Iterable):
            self.value = [NestedInteger(v) for v in value]
        elif isinstance(value, NestedInteger):
            self.value = value.value
        else:
            self.value = value

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.isInteger():
            return str(self.getInteger())
        else:
            return str(self.getList())

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return isinstance(self.value, int)

    def add(self, elem: 'NestedInteger'):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        if self.value is None:
            self.value = [elem]
        elif self.isInteger():
            self.value = [NestedInteger(self.value), elem]
        else:
            self.value = [*self.value, elem]

    def setInteger(self, value: int):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        self.value = value

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return self.value if self.isInteger() else None

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return self.value if not self.isInteger() else None


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit() or s[i] == '-':
                j = i if s[i].isdigit() else i + 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                stack[-1].add(NestedInteger(int(s[i:j])))
                i = j
                continue
            elif s[i] == ']':
                last = stack.pop()
                if stack:
                    stack[-1].add(last)
                else:
                    return last
            elif s[i] == '[':
                stack.append(NestedInteger())
            i += 1
        # return stack[-1].getList()[0]


    def deserialize_list(self, s: str) -> NestedInteger:
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit() or s[i] == '-':
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                stack.append(int(s[i:j]))
                i = j
                continue
            elif s[i] == ']':
                e = stack.pop()
                cur = []
                while e != '[':
                    cur.append(e)
                    e = stack.pop()
                stack.append(cur[::-1])
            elif s[i] == '[':
                stack.append('[')
            i += 1
        return stack[-1]


@pytest.mark.parametrize('s', [
    "[123,[456,[789]]]",
    "324",
    "[[]]",
    "-3",
    "[-1,-2]"
])
def test(s):
    ret = Solution().deserialize(s)
    assert str(ret) == str(eval(s))
