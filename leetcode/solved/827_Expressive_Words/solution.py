#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy. 

Example:
Input:
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation:
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.

Constraints:

	0 <= len(S) <= 100.
	0 <= len(words) <= 100.
	0 <= len(words[i]) <= 100.
	S and all words in words consist only of lowercase letters
"""
import sys
from typing import List
import pytest


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def stretchy(s, w):
            i = j = 0
            while i < len(s) and j < len(w):
                if s[i] != w[j]:
                    return False
                _i = i
                while _i < len(s) and s[_i] == s[i]:
                    _i += 1
                _j = j
                while _j < len(w) and w[_j] == w[j]:
                    _j += 1
                cnti = _i-i
                cntj = _j-j
                if (cnti >= 3 and cnti >= cntj) or cnti == cntj:
                    i = _i
                    j = _j
                else:
                    return False
            return i >= len(s) and j >= len(w)

        return sum(1 for w in words if stretchy(S, w))


@pytest.mark.parametrize('S, words, expected', [
    ("heeellooo", ["hello", "hi", "helo"], 1),
    ("aaa", ["aaaa"], 0),
])
def test(S, words, expected):
    assert expected == Solution().expressiveWords(S, words)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
