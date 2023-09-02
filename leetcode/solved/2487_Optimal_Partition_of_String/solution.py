#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.

Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.

Example 2:

Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").

Constraints:

	1 <= s.length <= 105
	s consists of only English lowercase letters.
"""
import pytest
import sys


class Solution:
    def partitionString(self, s: str) -> int:
        """Aug 26, 2023 12:36"""
        used = set()
        ret = 0
        for c in s:
            if c in used:
                used.clear()
                ret += 1
            used.add(c)
        if used:
            ret += 1
        return ret


@pytest.mark.parametrize('args', [
    (("abacaba", 4)),
    (("ssssss", 6)),
])
def test(args):
    assert args[-1] == Solution().partitionString(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
