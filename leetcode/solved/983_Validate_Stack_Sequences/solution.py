from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

Constraints:

	1 <= pushed.length <= 1000
	0 <= pushed[i] <= 1000
	All the elements of pushed are unique.
	popped.length == pushed.length
	popped is a permutation of pushed.
"""
import pytest
import sys


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """05/28/2020 23:30"""
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

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """03/27/2022 15:35"""
        stack = []
        i = j = 0
        while i < len(pushed) or j < len(popped):
            if not i < len(pushed):
                if stack[-1] != popped[j]:
                    return False
                else:
                    stack.pop()
                    j += 1
            elif not j < len(popped):
                stack.append(pushed[i])
                i += 1
            else:
                if stack and stack[-1] == popped[j]:
                    stack.pop()
                    j += 1
                else:
                    stack.append(pushed[i])
                    i += 1
        return True

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """Sep 02, 2023 17:35"""
        stack = []
        i = j = 0
        while j < len(popped):
            if stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                if i == len(pushed):
                    return False
                stack.append(pushed[i])
                i += 1
        return True


@pytest.mark.parametrize('args', [
    (([], [], True)),
    (([], [1], False)),
    (([1,2,3,4,5], [4,5,3,2,1], True)),
    (([1,2,3,4,5], [4,3,5,2,1], True)),
    (([1,2,3,4,5], [4,3,5,1,2], False)),
])
def test(args):
    assert args[-1] == Solution().validateStackSequences(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
