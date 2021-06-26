#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

	s = s1 + s2 + ... + sn
	t = t1 + t2 + ... + tm
	|n - m| <= 1
	The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true

Constraints:

	0 <= s1.length, s2.length <= 100
	0 <= s3.length <= 200
	s1, s2, and s3 consist of lowercase English letters.

Follow up: Could you solve it using only O(s2.length) additional memory space?
"""
from functools import lru_cache
import sys
import pytest


class Solution:
    def isInterleave(self, s1, s2, s3):
        """08/15/2018 15:43	"""
        if len(s1) + len(s2) != len(s3):
            return False
        if not s3:
            return True

        @lru_cache(maxsize=None)
        def dp(i, j):
            k = i + j
            if k == len(s3):
                return True
            return (i < len(s1) and s1[i] == s3[k] and dp(i+1, j))\
                or (j < len(s2) and s2[j] == s3[k] and dp(i, j+1))

        return dp(0, 0)

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """Bottom up
        Time complexity: O(n*m)
        Space complexity: O(min(n, m))
        """
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s2) > len(s1):
            return self.isInterleave(s2, s1, s3)
        dp = [True]
        for i, c in enumerate(s2):
            dp.append(dp[-1] and c == s3[i])
        for i in range(1, len(s1)+1):
            for j in range(len(s2)+1):
                cnt = i+j
                dp[j] = dp[j] and s1[i-1] == s3[cnt-1]
                if j > 0 and s2[j-1] == s3[cnt-1]:
                    dp[j] |= dp[j-1]
        return dp[-1]


@pytest.mark.parametrize('s1, s2, s3, expected', [
    ("aabcc", "dbbca", "aadbbcbcac", True),
    ("aabcc", "dbbca", "aadbbbaccc", False),
    ("", "", "", True),
    ("", "", "a", False)
])
def test(s1, s2, s3, expected):
    assert expected == Solution().isInterleave(s1, s2, s3)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
