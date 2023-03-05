#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

Constraints:

	1 <= s.length <= 20
	1 <= wordDict.length <= 1000
	1 <= wordDict[i].length <= 10
	s and wordDict[i] consist of only lowercase English letters.
	All the strings of wordDict are unique.
"""
from functools import lru_cache
from typing import List
import pytest
import sys


class Solution:
    def wordBreak(self, s, wordDict):
        """Oct 23, 2018 06:43"""
        @lru_cache(None)
        def word_break(i):
            if i == len(s):
                return [[]]
            ret = []
            for j in range(i+1, len(s)+1):
                if s[i:j] in words:
                    ret.extend([[s[i:j]] + l for l in word_break(j)])
            return ret

        words = set(wordDict)
        s = s
        return [' '.join(x) for x in word_break(0)]

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """Mar 05, 2023 13:22"""
        ret = []
        def dfs(i, words):
            if i == len(s):
                ret.append(' '.join(words))
            for word in wordDict:
                if s[i:].startswith(word):
                    words.append(word)
                    dfs(i+len(word), words)
                    words.pop()
        dfs(0, [])
        return ret

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """Mar 05, 2023 13:27"""
        @lru_cache(None)
        def dfs(i):
            if i == len(s):
                return ['']
            ret = []
            for word in wordDict:
                if s[i:].startswith(word):
                    ret.extend([word + ' ' + x for x in dfs(i+len(word))])
            return ret
        return [x.strip() for x in dfs(0)]


@pytest.mark.parametrize('args', [
    (("catsanddog", ["cat","cats","and","sand","dog"], ["cats and dog","cat sand dog"])),
    (("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"], ["pine apple pen apple","pineapple pen apple","pine applepen apple"])),
    (("catsandog", ["cats","dog","sand","and","cat"], [])),
])
def test(args):
    assert sorted(args[-1]) == sorted(Solution().wordBreak(*args[:-1]))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
