#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a string text. You should split it to k substrings (subtext1, subtext2, ..., subtextk) such that:

	subtexti is a non-empty string.
	The concatenation of all the substrings is equal to text (i.e., subtext1 + subtext2 + ... + subtextk == text).
	subtexti == subtextk - i + 1 for all valid values of i (i.e., 1 <= i <= k).

Return the largest possible value of k.

Example 1:

Input: text = "ghiabcdefhelloadamhelloabcdefghi"
Output: 7
Explanation: We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".

Example 2:

Input: text = "merchant"
Output: 1
Explanation: We can split the string on "(merchant)".

Example 3:

Input: text = "antaprezatepzapreanta"
Output: 11
Explanation: We can split the string on "(a)(nt)(a)(pre)(za)(tep)(za)(pre)(a)(nt)(a)".

Constraints:

	1 <= text.length <= 1000
	text consists only of lowercase English characters.
"""
from functools import lru_cache
import pytest
import sys


class Solution:
    def longestDecomposition(self, text: str) -> int:
        """May 04, 2024 17:05"""
        @lru_cache(None)
        def dp(i, j):
            ret = 1 if j >= i else 0
            for l in range(1, (j-i+1)//2 + 1):
                if text[i:i+l] == text[j+1-l:j+1]:
                    ret = max(ret, 2 + dp(i+l, j-l))
            return ret

        return dp(0, len(text)-1)


@pytest.mark.parametrize('args', [
    (("ghiabcdefhelloadamhelloabcdefghi", 7)),
    (("merchant", 1)),
    (("antaprezatepzapreanta", 11)),
    (("aaa", 3)),
    (("elvtoelvto", 2)),
])
def test(args):
    assert args[-1] == Solution().longestDecomposition(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
