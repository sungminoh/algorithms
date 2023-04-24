#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We can scramble a string s to get a string t using the following algorithm:

	If the length of the string is 1, stop.
	If the length of the string is > 1, do the following:

		Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
		Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
		Apply step 1 recursively on each of the two substrings x and y.

Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on s1 is:
"great" --> "gr/eat" // divide at random index.
"gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
"gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
"g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
"r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
"r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
The algorithm stops now, and the result string is "rgeat" which is s2.
As one possible scenario led s1 to be scrambled to s2, we return true.

Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false

Example 3:

Input: s1 = "a", s2 = "a"
Output: true

Constraints:

	s1.length == s2.length
	1 <= s1.length <= 30
	s1 and s2 consist of lowercase English letters.
"""
from functools import lru_cache
from collections import defaultdict
from collections import Counter
import pytest
import sys


class Solution:
    def isScramble(self, s1, s2):
        """Aug 14, 2018 23:16"""
        if s1 == s2:
            return True
        elif sorted(s1) != sorted(s2):
            return False
        for i in range(1, len(s1)):
            if (self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:]))\
                    or (self.isScramble(s1[0:i], s2[-i:]) and self.isScramble(s1[i:], s2[:len(s2)-i])):
                return True
        return False

    def isScramble(self, s1: str, s2: str) -> bool:
        """Apr 23, 2023 22:09"""

        @lru_cache(None)
        def comp(a, b):
            if len(a) == 1:
                return a == b

            cnt = defaultdict(int)
            for i, (x, y) in enumerate(zip(a, b)):
                cnt[x] += 1
                cnt[y] -= 1
                if cnt[x] == 0:
                    cnt.pop(x)
                if cnt[y] == 0:
                    cnt.pop(y)
                if not cnt and i < len(a)-1:
                    if (comp(a[:i+1], b[:i+1]) and comp(a[i+1:], b[i+1:])) \
                            or (comp(a[:i+1], b[:i+1][::-1]) and comp(a[i+1:], b[i+1:])) \
                            or (comp(a[:i+1], b[:i+1]) and comp(a[i+1:], b[i+1:][::-1])) \
                            or (comp(a[:i+1], b[:i+1][::-1]) and comp(a[i+1:], b[i+1:][::-1])):
                        return True
            return False

        return comp(s1, s2) or comp(s1, s2[::-1])


@pytest.mark.parametrize('args', [
    (("great", "rgeat", True)),
    (("abcde", "caebd", False)),
    (("a", "a", True)),
    (("ab", "ba", True)),
    (("great", "rgeta", True)),
])
def test(args):
    assert args[-1] == Solution().isScramble(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
