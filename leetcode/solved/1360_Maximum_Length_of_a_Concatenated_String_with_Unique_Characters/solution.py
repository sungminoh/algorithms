from functools import lru_cache
from typing import Tuple
from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.

Constraints:

	1 <= arr.length <= 16
	1 <= arr[i].length <= 26
	arr[i] contains only lowercase English letters.
"""
import pytest
import sys


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        """11/06/2022 16:05"""
        def encode(s):
            ret = 0
            for c in s:
                bit = 1<<(ord(c)-ord('a'))
                if ret & bit:
                    return None
                ret |= bit
            return ret

        encoded = [encode(s) for s in arr]

        def dfs(i, visited, used):
            ret = 0
            for j in range(i+1, len(arr)):
                if visited & (1<<j) or encoded[j] is None or used & encoded[j] != 0:
                    continue
                ret = max(ret, dfs(j, visited | (1<<j), used | encoded[j]))
            return ret + len(arr[i])

        ret = 0
        for i in range(len(arr)):
            if encoded[i] is not None:
                ret = max(ret, dfs(i, 1<<i, encoded[i]) )
        return ret

    def maxLength(self, arr: List[str]) -> int:
        """ Feb 01, 2024 19:17"""
        def encode(s):
            ret = 0
            for c in s:
                shift = ord(c)-ord('a')
                if ret & (1 << shift):
                    return 0
                ret |= (1 << shift)
            return ret

        code_length = {}
        for word in arr:
            c = encode(word)
            if c > 0:
                code_length[c] = len(word)

        codes = list(code_length.keys())

        @lru_cache(None)
        def dp(i, seen):
            if i == len(codes):
                return 0
            ret = dp(i+1, seen)
            if not codes[i] & seen:
                ret = max(ret, code_length[codes[i]] + dp(i+1, seen | codes[i]))
            return ret

        return dp(0, 0)


@pytest.mark.parametrize('args', [
    ((["un","iq","ue"], 4)),
    ((["cha","r","act","ers"], 6)),
    ((["abcdefghijklmnopqrstuvwxyz"], 26)),
    ((["aa","bb"], 0)),
])
def test(args):
    assert args[-1] == Solution().maxLength(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
