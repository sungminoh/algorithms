#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input:
S = "cba"
T = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.

Note:

	S has length at most 26, and no character is repeated in S.
	T has length at most 200.
	S and T consist of lowercase letters only.
"""
import sys
from collections import Counter
import pytest


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        idx = {c: i for i, c in enumerate(S)}
        sortedidx = sorted(idx.items(), key=lambda x: x[1])
        ret = []
        t = Counter(T)
        for c, _ in sortedidx:
            if c in t:
                ret.append(c*t[c])
                t.pop(c)
        for c, n in t.items():
            ret.append(c*n)
        return ''.join(ret)


@pytest.mark.parametrize('S, T, expected', [
    ("cba", "abcd", "cbad"),
])
def test(S, T, expected):
    assert expected == Solution().customSortString(S, T)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
