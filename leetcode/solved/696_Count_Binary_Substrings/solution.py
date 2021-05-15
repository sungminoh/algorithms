#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

Constraints:

	1 <= s.length <= 105
	s[i] is either '0' or '1'.
"""
import sys
import pytest


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        cnt = 0
        prev_cnt = 0
        cur_cnt = 0
        cur_char = ''
        for c in s:
            if c == cur_char:
                cur_cnt += 1
            else:
                cnt += min(cur_cnt, prev_cnt)
                prev_cnt, cur_cnt = cur_cnt, 1
                cur_char = c
        cnt += min(cur_cnt, prev_cnt)
        return cnt


@pytest.mark.parametrize('s, expected', [
    ("00110011", 6),
    ("10101", 4),
])
def test(s, expected):
    assert expected == Solution().countBinarySubstrings(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
