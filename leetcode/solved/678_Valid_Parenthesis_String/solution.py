#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:

Input: "()"
Output: True

Example 2:

Input: "(*)"
Output: True

Example 3:

Input: "(*))"
Output: True

Note:

The string size will be in the range [1, 100].
"""
import sys
import pytest


class Solution:
    def checkValidString(self, s: str) -> bool:
        n, m = 0, 0
        for c in s:
            if c == '(':
                n += 1
                m += 1
            elif c == ')':
                m -= 1
                if m < 0:
                    return False
                n = max(0, n-1)
            else:
                m += 1
                n = max(0, n-1)
        return n == 0

    def _checkValidString(self, s: str) -> bool:
        def rec(i):
            if i == -1:
                return {0}
            possibles = rec(i-1)
            current_possibles = []
            if s[i] == ')':
                current_possibles.append(-1)
            elif s[i] == '(':
                current_possibles.append(1)
            else:
                current_possibles.extend([-1,0,1])
            ret = set()
            for v in possibles:
                for u in current_possibles:
                    if v + u >= 0:
                        ret.add(v + u)
            return ret

        return 0 in rec(len(s)-1)


@pytest.mark.parametrize('s, expected', [
    ("()", True),
    ("(*)", True),
    ("(*))", True),
])
def test(s, expected):
    assert expected == Solution().checkValidString(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
