#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]

Constraints:

	0 <= digits.length <= 4
	digits[i] is a digit in the range ['2', '9'].
"""
import sys
from typing import List
import pytest


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """04/28/2021 00:17
        DFS
        Time complexitiy: exponential
        Space complexitiy: exponential
        """
        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def dfs(i, cur, out):
            if i == len(digits):
                if cur:
                    out.append(cur)
                return
            for c in m[digits[i]]:
                dfs(i+1, cur+c, out)

        out = []
        dfs(0, '', out)
        return out


    def letterCombinations(self, digits: str) -> List[str]:
        """05/22/2022 12:21
        BFS
        """
        if not digits:
            return []
        m = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        queue = list(m[int(digits[0])])
        for d in digits[1:]:
            new_queue = []
            for el in queue:
                for c in m[int(d)]:
                    new_queue.append(el + c)
            queue = new_queue
        return queue


@pytest.mark.parametrize('digits, expected', [
    ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
    ("", []),
    ("2", ["a","b","c"]),
])
def test(digits, expected):
    assert expected == Solution().letterCombinations(digits)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
