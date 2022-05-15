#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"

Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"

Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination:
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"

Constraints:

	1 <= s.length <= 10^5
	0 <= pairs.length <= 10^5
	0 <= pairs[i][0], pairs[i][1] < s.length
	s only contains lower case English letters.
"""
import sys
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UnionFind:
            def __init__(self):
                self.rep = {}

            def find(self, a):
                if a not in self.rep:
                    self.rep[a] = a
                if self.rep[a] != a:
                    self.rep[a] = self.find(self.rep[a])
                return self.rep[a]

            def union(self, a, b):
                pa = self.find(a)
                pb = self.find(b)
                self.rep[pa] = self.rep[pb] = min(pa, pb)

            def all_groups(self):
                ret = {}
                for k in self.rep:
                    ret.setdefault(self.find(k), []).append(k)
                return list(ret.values())

        uf = UnionFind()
        for a, b in pairs:
            if a > b:
                a, b = b, a
            uf.union(a, b)

        ret = list(s)
        groups = uf.all_groups()
        for indexes in groups:
            chars = [s[i] for i in indexes]
            for i, c in zip(sorted(indexes), sorted(chars)):
                ret[i] = c
        return ''.join(ret)


@pytest.mark.parametrize('s, pairs, expected', [
    ("dcab", [[0,3],[1,2]], "bacd"),
    ("dcab", [[0,3],[1,2],[0,2]], "abcd"),
    ("cba", [[0,1],[1,2]], "abc"),
    ("dcab", [], "dcab"),
    ("pwqlmqm", [[5,3],[3,0],[5,1],[1,1],[1,5],[3,0],[0,2]], "lpqqmwm"),
])
def test(s, pairs, expected):
    assert expected == Solution().smallestStringWithSwaps(s, pairs)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
