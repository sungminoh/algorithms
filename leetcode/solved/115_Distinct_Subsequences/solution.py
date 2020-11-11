#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
"""

from functools import lru_cache

class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(t) > len(s):
            return 0
        if s == t:
            return 1
        self.t = t
        chars = set(t)
        self.s = [c for c in s if c in chars]
        return self.foo(0, 0)

    @lru_cache(maxsize=None)
    def foo(self, i, j):
        if j >= len(self.t):
            return 1
        cnt = 0
        for k in range(i, len(self.s)-len(self.t)+j+1):
            if self.s[k] == self.t[j]:
                cnt += self.foo(k+1, j+1)
        return cnt


def main():
    s = input()
    t = input()
    print(Solution().numDistinct(s, t))


if __name__ == '__main__':
    main()
