#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:

	1 <= s.length <= 1000
	s consists of lowercase English letters.
"""
from functools import lru_cache
import pytest
import sys


class Solution:
    def countSubstrings(self, s: str) -> int:
        """06/27/2020 12:50"""
        @lru_cache(None)
        def is_palindrome(i, j):
            if i == j:
                return True
            if i+1 == j and s[i] == s[j]:
                return True
            return s[i] == s[j] and is_palindrome(i+1,j-1)
        return sum(1 if is_palindrome(i, j) else 0 for j in range(len(s)) for i in range(j+1))

    def countSubstrings(self, s: str) -> int:
        """06/27/2020 14:07
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        def expand(i, j):
            cnt = 0
            while 0 <= i and j < len(s) and s[i] == s[j]:
                cnt += 1
                i -= 1
                j += 1
            return cnt

        return sum(expand(i, i) for i in range(len(s))) + sum(expand(i, i+1) for i in range(len(s)-1))

    def countSubstrings(self, s: str) -> int:
        """06/12/2022 11:47
        Manacher's algorithm
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        def manacher(s: str) -> int:
            """
            s = abcdefg
            s` = #a#b#c#d#e#f#g#
            """
            if not s:
                return 0

            def char_at(i):
                if i%2 == 0:
                    return None
                return s[(i-1)//2]

            n = len(s)*2 + 1

            def expand(i, k):
                ret = k
                for j in range(k+1, min(i+1, n-i)):
                    if char_at(i-j) != char_at(i+j):
                        break
                    ret += 1
                return ret

            l = c = r = 0
            p = [0]*n
            i = 1
            while i < n:
                if i > r:
                    p[i] = expand(i, 0)
                else:
                    j = c-(i-c)
                    if i + p[j] >= r:
                        p[i] = expand(i, r-i)
                        if i + p[i] > r:
                            l = i-p[i]
                            c = i
                            r = i+p[i]
                    else:
                        p[i] = p[j]
                i += 1
            return p

        lps = manacher(s)
        # 2k -> 2k, 2k-2, 2k-4, ... 2 -> k*(2k+2)//2 = k*(k+1)
        # 2k-1 -> 2k-1, 2k-3, ... 1 -> k*(2k-1+1)//2 = k*k
        return sum((x+1)//2 for x in lps)

    def countSubstrings(self, s: str) -> int:
        """Feb 19, 2024 14:04"""
        @lru_cache(None)
        def is_palindrom(i, j):
            if i >= j:
                return True
            return s[i] == s[j] and is_palindrom(i+1, j-1)

        ret = 0
        for j in range(len(s)):
            for i in range(j+1):
                if is_palindrom(i, j):
                    ret += 1
        return ret


@pytest.mark.parametrize('args', [
    (("abc", 3)),
    (("aaa", 6)),
    (("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 500500)),
])
def test(args):
    assert args[-1] == Solution().countSubstrings(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
