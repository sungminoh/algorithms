#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

Constraints:

	1 <= words.length <= 1000
	1 <= words[i].length, chars.length <= 100
	words[i] and chars consist of lowercase English letters.
"""
from collections import Counter
from typing import List
import pytest
import sys


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        """Feb 04, 2024 12:39"""
        cnt = Counter(chars)
        ret = 0
        for w in words:
            if all(cnt.get(k, 0) >= v for k, v in Counter(w).items()):
                ret += len(w)
        return ret


@pytest.mark.parametrize('args', [
    ((["cat","bt","hat","tree"], "atach", 6)),
    ((["hello","world","leetcode"], "welldonehoneyr", 10)),
])
def test(args):
    assert args[-1] == Solution().countCharacters(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
