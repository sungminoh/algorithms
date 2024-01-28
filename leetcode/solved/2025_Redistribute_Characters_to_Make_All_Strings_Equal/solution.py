#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

Return true if you can make every string in words equal using any number of operations, and false otherwise.

Example 1:

Input: words = ["abc","aabc","bc"]
Output: true
Explanation: Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.

Example 2:

Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.

Constraints:

	1 <= words.length <= 100
	1 <= words[i].length <= 100
	words[i] consists of lowercase English letters.
"""
from collections import Counter
import itertools
from typing import List
import pytest
import sys


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        """Jan 27, 2024 18:10"""
        return all(cnt%len(words) == 0 for cnt in Counter(itertools.chain(*words)).values())


@pytest.mark.parametrize('args', [
    ((["abc","aabc","bc"], True)),
    ((["ab","a"], False)),
])
def test(args):
    assert args[-1] == Solution().makeEqual(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
