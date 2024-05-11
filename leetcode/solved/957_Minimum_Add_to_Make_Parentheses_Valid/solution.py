#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A parentheses string is valid if and only if:

	It is the empty string,
	It can be written as AB (A concatenated with B), where A and B are valid strings, or
	It can be written as (A), where A is a valid string.

You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

	For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".

Return the minimum number of moves required to make s valid.

Example 1:

Input: s = "())"
Output: 1

Example 2:

Input: s = "((("
Output: 3

Constraints:

	1 <= s.length <= 1000
	s[i] is either '(' or ')'.
"""
import pytest
import sys


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """May 05, 2024 14:11"""
        ret = 0
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                if cnt == 0:
                    ret += 1
                else:
                    cnt -= 1
        return ret + cnt


@pytest.mark.parametrize('args', [
    (("())", 1)),
    (("(((", 3)),
])
def test(args):
    assert args[-1] == Solution().minAddToMakeValid(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
