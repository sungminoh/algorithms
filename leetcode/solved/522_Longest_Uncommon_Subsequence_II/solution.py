
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:

Input: "aba", "cdc", "eae"
Output: 3

Note:
    1. All the given strings' lengths will not exceed 10.
    2. The length of the given list will be in the range of [2, 50].
"""
from functools import lru_cache
import sys
from collections import defaultdict
from typing import List
import pytest



def is_subsequence(a, b):
    if len(a) == len(b):
        return a == b
    i = 0
    j = 0
    while i < len(b):
        if b[i] == a[j]:
            j += 1
            i += 1
        else:
            i += 1
        if j == len(a):
            break
    return j == len(a)


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        m = -1
        for i in range(len(strs)):
            for j in range(len(strs)):
                print(strs[i], strs[j])
                if i == j:
                    continue
                if is_subsequence(strs[i], strs[j]):
                    break
            else:
                m = max(m, len(strs[i]))
        return m



@pytest.mark.parametrize('strs, expected', [
    (["aba", "cdc", "eae"], 3),
    (["aaa","aaa","aa"], -1),
    (["aabbcc", "aabbcc","c"], -1),
    (["aabbcc", "aabbcc","cb"], 2)
])
def test(strs, expected):
    assert expected == Solution().findLUSlength(strs)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
