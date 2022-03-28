#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

	It is the empty string, contains only lowercase characters, or
	It can be written as AB (A concatenated with B), where A and B are valid strings, or
	It can be written as (A), where A is a valid string.

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Constraints:

	1 <= s.length <= 105
	s[i] is either'(' , ')', or lowercase English letter.
"""
import itertools
import sys
import pytest


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ret = ''
        num_closes = reversed(list(itertools.accumulate(
            reversed([1 if c == ')' else 0 for c in s]))))
        cnt = 0
        for c, n in zip(s, num_closes):
            if c == '(':
                if n > cnt:
                    ret += c
                    cnt += 1
            elif c == ')':
                if cnt != 0:
                    ret += c
                    cnt -= 1
            else:
                ret += c
        return ret


@pytest.mark.parametrize('s, expected', [
    ("lee(t(c)o)de)", "lee(t(c)o)de"),
    ("a)b(c)d", "ab(c)d"),
    ("))((", ""),
])
def test(s, expected):
    assert expected == Solution().minRemoveToMakeValid(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
