#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given two strings order and s. All the words of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

Example 1:

Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

Example 2:

Input: order = "cbafg", s = "abcd"
Output: "cbad"

Constraints:

	1 <= order.length <= 26
	1 <= s.length <= 200
	order and s consist of lowercase English letters.
	All the characters of order are unique.
"""
import sys
from collections import Counter
from collections import defaultdict
import pytest


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        """09/12/2020 14:03"""
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

    def customSortString(self, order: str, s: str) -> str:
        """
        Sort
        Time complexity: O(nlogn)
        Space complexity: O(n)
        """
        priority = {c: i for i, c in enumerate(order)}
        return ''.join(sorted(s, key=lambda x: priority.get(x, 0)))

    def customSortString(self, order: str, s: str) -> str:
        """
        Without using sort
        Time complexity: O(n)
        Space complexity: O(n)
        """
        cnt = Counter(s)
        ret = ''
        for c in order:
            if c in cnt:
                ret += c*cnt[c]
                cnt.pop(c)
        for c, n in cnt.items():
            ret += c*n
        return ret


@pytest.mark.parametrize('order, s, expected', [
    ("cba", "abcd", "cbad"),
    ("cbafg", "abcd", "cbad"),
])
def test(order, s, expected):
    assert expected == Solution().customSortString(order, s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
