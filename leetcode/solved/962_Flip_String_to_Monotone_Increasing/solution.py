#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.

Example 1:

Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.

Example 2:

Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.

Example 3:

Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.

Constraints:

	1 <= s.length <= 105
	s[i] is either '0' or '1'.
"""
import pytest
import sys


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """Sep 23, 2021 00:08"""
        m0 = 0  # to ends with 0
        m1 = 0  # to ends with 1
        for c in s:
            if c == '0':
                m1 += 1
            else:
                m1 = min(m1, m0)
                m0 += 1
        return min(m0, m1)

    def minFlipsMonoIncr(self, s: str) -> int:
        """Mar 05, 2023 20:32"""
        num_ones_on_left = []
        num_zeros_on_right = []
        ones = 0
        for c in s:
            num_ones_on_left.append(ones)
            if c == '1':
                ones += 1
        zeros = 0
        for c in reversed(s):
            num_zeros_on_right.append(zeros)
            if c == '0':
                zeros += 1
        num_zeros_on_right.reverse()
        return min(o + z for o, z in zip(num_ones_on_left, num_zeros_on_right))


@pytest.mark.parametrize('args', [
    (("00110", 1)),
    (("010110", 2)),
    (("00011000", 2)),
])
def test(args):
    assert args[-1] == Solution().minFlipsMonoIncr(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
