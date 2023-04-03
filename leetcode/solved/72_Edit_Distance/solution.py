#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

	Insert a character
	Delete a character
	Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:

	0 <= word1.length, word2.length <= 500
	word1 and word2 consist of lowercase English letters.
"""
from functools import lru_cache
import pytest
import sys


class Solution:
    def minDistance(self, word1, word2):
        """Aug 11, 2018 05:20
        :type word1: str
        :type word2: str
        :rtype: int
        """
        """
          _ h o r s e
        _ 0 1 2 3 4 5
        o 1 1 1 2 3 4
        r 2 2 2 1 2 3
        s 3 3 2 2 1 2

        """
        if not word1 or not word2:
            return max(len(word1), len(word2))
        memo = [j+1 for j in range(len(word2))]
        for i in range(len(word1)):
            new_memo = []
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    new_memo.append(memo[j-1] if j != 0 else i)
                else:
                    new_memo.append(1 + min(new_memo[-1] if j != 0 else i+1,
                                            memo[j-1] if j != 0 else i,
                                            memo[j]))
            memo = new_memo
        return memo[-1]

    def minDistance(self, word1: str, word2: str) -> int:
        """Apr 02, 2023 14:14"""
        @lru_cache(None)
        def dfs(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2)-j
            if j == len(word2):
                return len(word1)-i
            if word1[i] == word2[j]:
                return dfs(i+1, j+1)
            return 1 + min(dfs(i+1, j), dfs(i, j+1), dfs(i+1, j+1))
        return dfs(0, 0)


@pytest.mark.parametrize('args', [
    (("horse", "ros", 3)),
    (("intention", "execution", 5)),
])
def test(args):
    assert args[-1] == Solution().minDistance(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
