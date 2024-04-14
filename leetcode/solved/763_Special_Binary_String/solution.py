#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Special binary strings are binary strings with the following two properties:

	The number of 0's is equal to the number of 1's.
	Every prefix of the binary string has at least as many 1's as 0's.

You are given a special binary string s.

A move consists of choosing two consecutive, non-empty, special substrings of s, and swapping them. Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.

Return the lexicographically largest resulting string possible after applying the mentioned operations on the string.

Example 1:

Input: s = "11011000"
Output: "11100100"
Explanation: The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.

Example 2:

Input: s = "10"
Output: "10"

Constraints:

	1 <= s.length <= 50
	s[i] is either '0' or '1'.
	s is a special binary string.
"""
from collections import defaultdict
import itertools
import pytest
import sys


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        """Apr 13, 2024 18:21"""

        N = len(s)

        visited = set()
        def rec(s):
            visited.add(s)
            specials = defaultdict(list)
            acc = 0
            for i in range(N):
                acc = 0
                for j in range(i, N):
                    acc += 1 if s[j] == '1' else -1
                    if acc == 0:
                        specials[i].append(j+1)
                        break
                    elif acc < 0:
                        break
            ret = s
            for i in specials:
                for j in specials.get(i, []):
                    for k in specials.get(j, []):
                        if not s[j:k].startswith(s[i:j]) and s[i:j] < s[j:k]:
                            _s = s[:i] + s[j:k] + s[i:j] + s[k:]
                            if _s not in visited:
                                ret = max(ret, rec(_s))
            return ret

        return rec(s)

    def makeLargestSpecial(self, s: str) -> str:
        acc = 0
        i = 0
        subs = []
        for j, c in enumerate(s):
            acc += 1 if c == '1' else -1
            if acc == 0:
                subs.append('1' + self.makeLargestSpecial(s[i+1:j]) + '0')
                i = j+1
        return ''.join(sorted(subs, reverse=True))


@pytest.mark.parametrize('args', [
    (("11011000", "11100100")),
    (("10", "10")),
    (("1010101100", '1100101010')),
    (("101100101100", "110011001010")),
    (("1010101101010101001100", '1101010101001100101010')),
    (("10101101001011100011010110001011001110011000101100", '11100110001110010100111000110100110011001010101010')),
])
def test(args):
    assert args[-1] == Solution().makeLargestSpecial(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
