
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:

Input: ")("
Output: [""]
"""
import sys
from typing import List
import pytest


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ret = set()
        m = float('inf')
        def dfs(i, n, cur, removed):
            nonlocal m, ret
            if removed > m:
                return
            if i == len(s):
                if n == 0:
                    if removed < m:
                        m = removed
                        ret = set([cur])
                    elif removed == m:
                        ret.add(cur)
                return
            if s[i] not in '()':
                return dfs(i+1, n, cur + s[i], removed)
            if s[i] == '(':
                dfs(i+1, n+1, cur + '(', removed)
            elif s[i] == ')' and n > 0:
                dfs(i+1, n-1, cur + ')', removed)
            dfs(i+1, n, cur, removed + 1)
        dfs(0, 0, '', 0)
        return list(ret)


@pytest.mark.parametrize('s, expected', [
    ("()())()", ["()()()", "(())()"]),
    ("(a)())()", ["(a)()()", "(a())()"]),
    (")(", [""]),
])
def test(s, expected):
    assert set(expected) == set(Solution().removeInvalidParentheses(s))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
