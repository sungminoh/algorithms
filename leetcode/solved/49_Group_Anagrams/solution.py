import string
from collections import defaultdict
from collections import Counter
from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:

	1 <= strs.length <= 104
	0 <= strs[i].length <= 100
	strs[i] consists of lowercase English letters.
"""
import pytest
import sys


class Solution:
    def groupAnagrams(self, strs):
        """04/22/2018 04:37"""
        d = defaultdict(list)
        for s in strs:
            d[''.join(sorted(s))].append(s)
        return list(d.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """09/22/2021 23:39"""
        d = defaultdict(set)
        for i, s in enumerate(''.join(sorted(x)) for x in strs):
            d[s].add(i)
        return [[strs[i] for i in indexes ]for indexes in d.values()]

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """11/06/2022 14:20"""
        def encode(w):
            cnt = [0]*26
            for c in w:
                cnt[ord(c)-ord('a')] += 1
            return tuple(cnt)

        grouped = defaultdict(list)
        for w in strs:
            grouped[encode(w)].append(w)
        return list(grouped.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Feb 19, 2024 12:32"""
        def encode(s):
            cnt = Counter(s)
            return tuple(cnt[c] for c in string.ascii_lowercase)

        ret = defaultdict(list)
        for s in strs:
            ret[encode(s)].append(s)
        return list(ret.values())


@pytest.mark.parametrize('args', [
    ((["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]])),
    (([""], [[""]])),
    ((["a"], [["a"]])),
])
def test(args):
    assert sorted([sorted(x) for x in args[-1]]) == sorted([sorted(x) for x in Solution().groupAnagrams(*args[:-1])])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
