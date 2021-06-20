#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of strings words, return the smallest string that contains each string in words as a substring. If there are multiple valid strings of the smallest length, return any of them.

You may assume that no string in words is a substring of another string in words.

Example 1:

Input: words = ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.

Example 2:

Input: words = ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"

Constraints:

	1 <= words.length <= 12
	1 <= words[i].length <= 20
	words[i] consists of lowercase English letters.
	All the strings of words are unique.
"""
from prompt_toolkit.filters import app
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        """
        Time complexity: O(2^n * n)
        Space complexity: O(2^n * n)
        """
        if not words:
            return ''

        @lru_cache(None)
        def overlap(s, p):
            for i in range(len(p)):
                if s.endswith(p[:len(p)-i]):
                    return len(p)-i
            return 0

        @lru_cache(None)
        def dp(available, i):
            s = available
            available = available^(1<<i)
            max_indexes = [i]
            max_overlap = -1
            for j in range(len(words)):
                if (1<<j) & available:
                    cnt_overlap, indexes = dp(available, j)
                    cnt_overlap += overlap(words[j], words[i])
                    if cnt_overlap > max_overlap:
                        max_overlap = cnt_overlap
                        max_indexes = indexes + [i]
            return max(0, max_overlap), max_indexes

        available = (1<<len(words)) - 1
        max_indexes = []
        max_overlap = -1
        for i in range(len(words)):
            cnt_overlap, indexes = dp(available, i)
            if cnt_overlap > max_overlap:
                max_overlap = cnt_overlap
                max_indexes = indexes
        ret = words[max_indexes[0]]
        for i, idx in enumerate(max_indexes[1:], 1):
            prev_word = words[max_indexes[i-1]]
            ret += words[idx][overlap(prev_word, words[idx]):]
        return ret


@pytest.mark.parametrize('words, expected', [
(["alex","loves","leetcode"], "alexlovesleetcode"),
(["catg","ctaagt","gcta","ttca","atgcatc"], "gctaagttcatgcatc"),
])
def test(words, expected):
    actual = Solution().shortestSuperstring(words)
    print(actual)
    assert len(expected) == len(actual)
    for word in words:
        assert word in actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
