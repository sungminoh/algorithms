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
import sys
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def groupAnagrams(self, strs):
        """04/22/2018 04:37"""
        d = defaultdict(list)
        for s in strs:
            d[''.join(sorted(s))].append(s)
        return list(d.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(set)
        for i, s in enumerate(''.join(sorted(x)) for x in strs):
            d[s].add(i)
        return [[strs[i] for i in indexes ]for indexes in d.values()]


@pytest.mark.parametrize('strs, expected', [
    (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
    ([""], [[""]]),
    (["a"], [["a"]]),
])
def test(strs, expected):
    assert sorted(sorted(x) for x in expected) == sorted(sorted(x) for x in Solution().groupAnagrams(strs))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))

