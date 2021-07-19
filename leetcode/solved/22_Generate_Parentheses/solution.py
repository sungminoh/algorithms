#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1
Output: ["()"]

Constraints:

	1 <= n <= 8
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Time complexity: O(n^3)
        Space complexity: O(n^3)
        """
        @lru_cache(None)
        def gen_surrounded(n):
            if n == 0:
                return ['']
            return [f'({s})' for s in gen_all(n-1)]

        @lru_cache(None)
        def gen_all(n):
            if n == 0:
                return ['']
            ret = []
            for i in range(1, n+1):
                for pre in gen_surrounded(i):
                    for post in gen_all(n-i):
                        ret.append(pre + post)
            return ret

        return gen_all(n)

    @lru_cache(None)
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Time complexity: O(n^3)
        Space complexity: O(n^3)
        """
        if n == 0:
            return ['']
        ret = []
        for i in range(n):
            for pre in self.generateParenthesis(i):
                for post in self.generateParenthesis(n-i-1):
                    ret.append(f'{pre}({post})')
        return ret


@pytest.mark.parametrize('n, expected', [
(3, ["((()))","(()())","(())()","()(())","()()()"]),
(1, ["()"]),
])
def test(n, expected):
    actual = Solution().generateParenthesis(n)
    print()
    print(actual)
    assert len(expected) == len(actual)
    assert sorted(expected) == sorted(actual)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
