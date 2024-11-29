#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is a strange printer with the following two special properties:

	The printer can only print a sequence of the same character each time.
	At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.

Given a string s, return the minimum number of turns the printer needed to print it.

Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".

Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.

Constraints:

	1 <= s.length <= 100
	s consists of lowercase English letters.
"""
from functools import lru_cache
import pytest
import sys


class Solution:
    def strangePrinter(self, s: str) -> int:
        """TLE"""
        def dfs(i, stack):
            if i == len(s):
                return 0
            j = i
            while j < len(s) and s[i] == s[j]:
                j += 1
            ret = 1 + dfs(j, stack + [s[i]])
            while stack and stack[-1] != s[i]:
                stack.pop()
            if stack:
                ret = min(ret, dfs(j, stack))
            return ret

        return dfs(0, [])

    def strangePrinter(self, s: str) -> int:
        """Early termination, TLE"""
        ret = float('inf')
        def dfs(i, stack, cur):
            nonlocal ret
            if cur >= ret:
                return
            if i == len(s):
                ret = min(ret, cur)
                return
            j = i
            while j < len(s) and s[i] == s[j]:
                j += 1
            dfs(j, stack + [s[i]], cur+1)
            while stack and stack[-1] != s[i]:
                stack.pop()
            if stack:
                dfs(j, stack, cur)

        dfs(0, [], 0)
        return ret

    def strangePrinter(self, s: str) -> int:
        """Memoization, TLE"""
        @lru_cache(None)
        def dfs(i, stack):
            if i == len(s):
                return 0
            j = i
            while j < len(s) and s[i] == s[j]:
                j += 1
            ret = 1 + dfs(j, stack + (s[i], ))
            stack = list(stack)
            while stack and stack[-1] != s[i]:
                stack.pop()
            if stack:
                ret = min(ret, dfs(j, tuple(stack)))
            return ret

        return dfs(0, tuple())

    @lru_cache(None)
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0
        ret = 1 + self.strangePrinter(s[1:])
        j = 1
        while j < len(s):
            if s[j] == s[0]:
                ret = min(ret, self.strangePrinter(s[:j]) + self.strangePrinter(s[j+1:]))
            j += 1
        return ret

    @lru_cache(None)
    def strangePrinter(self, s: str) -> int:
        N = len(s)
        ret = N
        i = 0
        while i < N:
            j = i
            while j < N and s[j] == s[i]:
                j += 1
            ret = min(ret, 1 + self.strangePrinter(s[:i] + s[j:]))
            i = j
        return ret


@pytest.mark.parametrize('args', [
    (("aaabbb", 2)),
    (("aba", 2)),
    (("abcdefedcbabcdefedcba", 11)),
    (("abcdefafedcba", 7)),
    (("baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa", 19)),
    (("ccdaccacbbdbacdccdbadacbbcbbaadacbadadbbcbdbaacdb", 25)),
    (("zuvckrvtmihlhnbbgycnxthqtskcjgakbypnrkhduqqcdsfksjzscjivbtzmbzxezosrabwurnywhdizmktqtcnuxmjyoidpwxg", 74)),
])
def test(args):
    assert args[-1] == Solution().strangePrinter(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
