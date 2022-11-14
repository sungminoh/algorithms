#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".

Constraints:

	1 <= words.length <= 105
	words[i].length == 2
	words[i] consists of lowercase English letters.
"""
from collections import Counter
from typing import List
import pytest
import sys


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        ret = 0
        for w in counter:
            r = w[::-1]
            if r in counter:
                n = min(counter[w], counter[r]) if w != r else counter[w]//2
                ret += 4*n
                counter[w] -= n
                counter[r] -= n
        if any(w == w[::-1] and counter[w] > 0 for w in counter):
            ret += 2
        return ret


@pytest.mark.parametrize('words, expected', [
    (["lc","cl","gg"], 6),
    (["ab","ty","yt","lc","cl","ab"], 8),
    (["cc","ll","xx"], 2),
])
def test(words, expected):
    assert expected == Solution().longestPalindrome(words)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
