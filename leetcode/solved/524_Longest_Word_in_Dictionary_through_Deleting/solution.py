
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:

Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"

Example 2:

Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"

Note:
    1. All the strings in the input will only contain lower-case letters.
    2. The size of the dictionary won't exceed 1,000.
    3. The length of all the strings in the input won't exceed 1,000.
"""
import sys
from typing import List
import pytest


def is_subseq(a, b):
    if len(a) == len(b):
        return a == b
    i, j = 0, 0
    while i < len(b):
        if b[i] == a[j]:
            i += 1
            j += 1
        else:
            i += 1
        if j == len(a):
            break
    return j == len(a)


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d = sorted(d, key=lambda x: (-len(x), x))
        return next((x for x in d if is_subseq(x, s)), '')


@pytest.mark.parametrize('s, d, expected', [
    ("abpcplea", ["ale","apple","monkey","plea"], "apple"),
    ("abpcplea", ["a","b","c"], "a"),
    ("apple", ["zxc","vbn"], "")
])
def test(s, d, expected):
    assert expected == Solution().findLongestWord(s, d)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
