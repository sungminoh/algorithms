#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

Example 1:

Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.

Example 2:

Input: s = "10"
Output: 0
Explanation: s is already alternating.

Example 3:

Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".

Constraints:

	1 <= s.length <= 104
	s[i] is either '0' or '1'.
"""
import pytest
import sys


class Solution:
    def minOperations(self, s: str) -> int:
        """Jan 27, 2024 14:27"""
        dp = [0, 1]  # keep or swap
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                dp = [dp[0], dp[1]+1]
            else:
                dp = [dp[1], dp[0]+1]

        return min(dp)


@pytest.mark.parametrize('args', [
    (("0100", 1)),
    (("10", 0)),
    (("1111", 2)),
])
def test(args):
    assert args[-1] == Solution().minOperations(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
