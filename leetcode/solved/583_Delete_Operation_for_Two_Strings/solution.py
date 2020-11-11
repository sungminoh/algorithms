
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:

Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Note:

The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
"""
import sys
from functools import lru_cache
import pytest




class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def lcs(i, j):
            if i == -1 or j == -1:
                return 0
            if word1[i] == word2[j]:
                m = max([m, lcs(i-1, j-1) + 1])
            else:
                m = max([lcs(i-1, j), lcs(i, j-1)])
            return m
        lcs_length = lcs(len(word1)-1, len(word2)-1)
        return len(word1) + len(word2) - (2 * lcs_length)


@pytest.mark.parametrize('word1, word2, expected', [
    ('sea', 'eat', 2)
])
def test(word1, word2, expected):
    assert expected == Solution().minDistance(word1, word2)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
