#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.

Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".

Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".

Constraints:

	1 <= s.length <= 500
	s consists of lowercase English letters.
"""
from functools import lru_cache
import pytest
import sys


class Solution:
    def minInsertions(self, s: str) -> int:
        """Sep 03, 2023 22:26"""
        @lru_cache(None)
        def dp(i, j):
            if i >= j:
                return 0
            cases = [dp(i+1, j) + 1, dp(i, j-1) + 1]
            if s[i] == s[j]:
                cases.append(dp(i+1, j-1))
            return min(cases)

        return dp(0, len(s)-1)


@pytest.mark.parametrize('args', [
    (("zzazz", 0)),
    (("mbadm", 2)),
    (("leetcode", 5)),
])
def test(args):
    assert args[-1] == Solution().minInsertions(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
