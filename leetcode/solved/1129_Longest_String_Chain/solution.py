#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

	For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".

A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.

Constraints:

	1 <= words.length <= 1000
	1 <= words[i].length <= 16
	words[i] only consists of lowercase English letters.
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        DFS DP
        Time complexity: O(n^2*l)
        Space complexity: O(n)
        """
        if not words:
            return 0

        # O(nlogn)
        words.sort(key=len)
        indexes = {}
        # O(n)
        for i, w in enumerate(words):
            indexes.setdefault(len(w), i)

        # O(l)
        def is_predecesor(parent, child):
            if len(parent) != len(child)+1:
                return False
            i, j = 0, 0
            while i < len(parent) and j < len(child):
                if parent[i] != child[j]:
                    if i > j:
                        return False
                    else:
                        i += 1
                else:
                    i += 1
                    j += 1
            return True

        @lru_cache(None)
        def dfs(i):
            """
            Time complexity: O(n)
            Space complexity: O(1)
            """
            if i == 0:
                return 1
            ret = 1
            for j in range(
                indexes.get(len(words[i])-1, len(words)),
                indexes[len(words[i])]):
                if is_predecesor(words[i], words[j]):
                    ret = max(ret, 1+dfs(j))
            return ret

        # O(n^2)
        return max(dfs(i) for i in range(len(words)))

    def longestStrChain(self, words: List[str]) -> int:
        """
        DP
        Time complexity: O(n*l*l)
        Space complexity: O(n*l)
        """
        # O(nlogn)
        words.sort(key=len)
        dp = {}
        for word in words:  # O(n)
            dp[word] = 1
            for i in range(len(word)):  # O(l)
                child = word[:i] + word[i+1:]  # O(l)
                dp[word] = max(dp[word], dp.get(child, 0)+ 1)
        return max(dp.values())


@pytest.mark.parametrize('words, expected', [
    (["a","b","ba","bca","bda","bdca"], 4),
    (["xbc","pcxbcf","xb","cxbc","pcxbc"], 5),
    (["abcd","dbqca"], 1),
    (["a","b","ab","bac"], 2)
])
def test(words, expected):
    assert expected == Solution().longestStrChain(words)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
