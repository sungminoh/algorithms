#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

	0 <= i <= s.length - 2
	s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

Example 1:

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

Example 2:

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

Example 3:

Input: s = "s"
Output: "s"

Constraints:

	1 <= s.length <= 100
	s contains only lower and upper case English letters.
"""
import pytest
import sys


class Solution:
    def makeGood(self, s: str) -> str:
        """11/13/2022 18:35"""
        removed = [False]*len(s)

        def is_bad(a, b):
            return a != b and a.lower() == b.lower()

        def expand(i, j):
            if is_bad(s[i], s[j]):
                removed[i] = removed[j] = True
                while i >= 0 and removed[i]:
                    i -= 1
                while j < len(s) and removed[j]:
                    j += 1
                if i >= 0 and j < len(s):
                    return expand(i, j)
            return i, j

        i = 0
        while i < len(s)-1:
            _, i = expand(i, i+1)
        return ''.join([c for c, r in zip(s, removed) if not r])


@pytest.mark.parametrize('s, expected', [
    ("leEeetcode", "leetcode"),
    ("abBAcC", ""),
    ("s", "s"),
    ("MqWWvyRtzZTrYVwwQmUjQOoOoqJu", ""),
])
def test(s, expected):
    assert expected == Solution().makeGood(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
