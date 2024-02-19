from collections import Counter

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

Constraints:

	1 <= s.length <= 5 * 105
	s consists of uppercase and lowercase English letters and digits.
"""
import pytest
import sys


class Solution:
    def frequencySort(self, s: str) -> str:
        """05/03/2020 18:22"""
        cnt = Counter(s)
        ret = ''
        for c, n in cnt.most_common():
            ret += c * n
        return ret

    def frequencySort(self, s: str) -> str:
        """Oct 30, 2021 00:30"""
        ret = ''
        for c, cnt in Counter(s).most_common():
            ret += c*cnt
        return ret

    def frequencySort(self, s: str) -> str:
        """Dec 04, 2022 22:33"""
        cnt = Counter(s)
        ret = ''
        for c, t in sorted(cnt.most_common(), key=lambda x: (-x[1], x[0])):
            ret += c*t
        return ret

    def frequencySort(self, s: str) -> str:
        """Feb 19, 2024 12:51"""
        return ''.join(c*cnt for c, cnt in Counter(s).most_common())


@pytest.mark.parametrize('args', [
    (("tree", "eert")),
    (("cccaaa", "aaaccc")),
    (("Aabb", "bbAa")),
])
def test(args):
    assert args[-1] == Solution().frequencySort(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
