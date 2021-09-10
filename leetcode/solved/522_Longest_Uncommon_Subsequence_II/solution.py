#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.

An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.

A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

	For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).

Example 1:
Input: strs = ["aba","cdc","eae"]
Output: 3
Example 2:
Input: strs = ["aaa","aaa","aa"]
Output: -1

Constraints:

	2 <= strs.length <= 50
	1 <= strs[i].length <= 10
	strs[i] consists of lowercase English letters.
"""
import sys
from collections import Counter
from typing import List
import pytest


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        """05/31/2020 20:15"""
        def is_subsequence(a, b):
            if len(a) == len(b):
                return a == b
            i = 0
            j = 0
            while i < len(b):
                if b[i] == a[j]:
                    j += 1
                    i += 1
                else:
                    i += 1
                if j == len(a):
                    break
            return j == len(a)

        m = -1
        for i in range(len(strs)):
            for j in range(len(strs)):
                if i == j:
                    continue
                if is_subsequence(strs[i], strs[j]):
                    break
            else:
                m = max(m, len(strs[i]))
        return m

    def findLUSlength(self, strs: List[str]) -> int:
        def is_subseq(s, arr):
            # print(s, arr)
            pointers = {x: 0 for x in arr}
            for c in s:
                exhausted = []
                for x in pointers:
                    while pointers[x] < len(x) and x[pointers[x]] != c:
                        pointers[x] += 1
                    if pointers[x] == len(x):
                        exhausted.append(x)
                    pointers[x] += 1
                for x in exhausted:
                    pointers.pop(x)
                # print(pointers)
                if not pointers:
                    return False
            return True

        longers = []
        for s, c in sorted(Counter(strs).most_common(len(strs)), key=lambda x: -len(x[0])):
            if c == 1 and not is_subseq(s, longers):
                return len(s)
            longers.append(s)
        return -1


@pytest.mark.parametrize('strs, expected', [
    (["aba","cdc","eae"], 3),
    (["aaa","aaa","aa"], -1),
    (["aabbcc", "aabbcc","cb"], 2),
    (["abcabc","abcabc","abcabc","abc","abc","cca"], 3),
])
def test(strs, expected):
    assert expected == Solution().findLUSlength(strs)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
