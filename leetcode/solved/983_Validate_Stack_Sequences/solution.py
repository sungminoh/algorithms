
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

Note:
    1. 0 <= pushed.length == popped.length <= 1000
    2. 0 <= pushed[i], popped[i] < 1000
    3. pushed is a permutation of popped.
    4. pushed and popped have distinct values.
"""
import sys
from typing import List
import pytest


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed:
            return len(popped) == 0
        stack = []
        i = 0
        j = 0
        while i < len(pushed):
            stack.append(pushed[i])
            i += 1
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            if j == len(popped):
                return True
        return False


@pytest.mark.parametrize('pushed, popped, expected', [
    ([], [], True),
    ([], [1], False),
    ([1,2,3,4,5], [4,5,3,2,1], True),
    ([1,2,3,4,5], [4,3,5,2,1], True),
    ([1,2,3,4,5], [4,3,5,1,2], False),
])
def test(pushed, popped, expected):
    assert expected == Solution().validateStackSequences(pushed, popped)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
