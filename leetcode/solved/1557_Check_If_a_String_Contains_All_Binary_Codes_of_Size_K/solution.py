#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.

Example 2:

Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring.

Example 3:

Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and does not exist in the array.

Constraints:

	1 <= s.length <= 5 * 105
	s[i] is either '0' or '1'.
	1 <= k <= 20
"""
import sys
import pytest


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        lenk = set()
        for i in range(len(s)-(k-1)):
            j = i+k
            lenk.add(s[i:j])
        return len(lenk) == 2**k


@pytest.mark.parametrize('s, k, expected', [
    ("00110110", 2, True),
    ("0110", 1, True),
    ("0110", 2, False),
])
def test(s, k, expected):
    assert expected == Solution().hasAllCodes(s, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
