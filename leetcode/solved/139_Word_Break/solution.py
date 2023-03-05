#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:

	1 <= s.length <= 300
	1 <= wordDict.length <= 1000
	1 <= wordDict[i].length <= 20
	s and wordDict[i] consist of only lowercase English letters.
	All the strings of wordDict are unique.
"""
from functools import lru_cache
from collections import defaultdict
from typing import List
import pytest
import sys


class Solution:
    def wordBreak(self, s, wordDict):
        """Jul 26, 2018 04:31"""
        if not s:
            return True
        if not wordDict:
            return False
        s = s
        wordDict = set(wordDict)
        lengths = {len(word) for word in wordDict}
        memo = [None] * len(s)

        def solve(i):
            s = s[i:]
            if not s:
                return True
            if memo[i] is not None:
                return memo[i]
            for j in lengths:
                if s[:j] in wordDict:
                    sub_result = solve(i+j)
                    if sub_result:
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        return solve(0)

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """Mar 05, 2023 13:04
        TLE
        """
        trie = {}
        for word in wordDict:
            d = trie
            for c in word:
                d.setdefault(c, {})
                d = d[c]
            d[None] = None

        tries = [trie]
        for i, c in enumerate(s):
            new_tries = []
            for t in tries:
                if c in t:
                    new_tries.append(t[c])
                    if None in t[c]:
                        new_tries.append(trie)
                        if i == len(s)-1:
                            return True
            tries = new_tries
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict.sort(key=len, reverse=True)
        @lru_cache(None)
        def dfs(i):
            if i == len(s):
                return True
            return any([
                False,
                *[dfs(i+len(w)) for w in wordDict if s[i:].startswith(w)]
            ])
        return dfs(0)


@pytest.mark.parametrize('args', [
    (("leetcode", ["leet","code"], True)),
    (("applepenapple", ["apple","pen"], True)),
    (("catsandog", ["cats","dog","sand","and","cat"], False)),
    (("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"], False))
])
def test(args):
    assert args[-1] == Solution().wordBreak(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
