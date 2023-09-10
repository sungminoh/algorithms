#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:

	1 <= s.length <= 105
	s consists of lowercase English letters.
	1 <= k <= s.length
"""
import pytest
import sys


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """Sep 09, 2023 21:47"""
        VOWEL = set('aeiou')

        ret = cnt = 0
        j = -1
        for i, c in enumerate(s):
            if c in VOWEL:
                cnt += 1
            if i - j > k:
                j += 1
                if s[j] in VOWEL:
                    cnt -= 1
            ret = max(ret, cnt)
        return ret


@pytest.mark.parametrize('args', [
    (("abciiidef", 3, 3)),
    (("aeiou", 2, 2)),
    (("leetcode", 3, 2)),
])
def test(args):
    assert args[-1] == Solution().maxVowels(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
