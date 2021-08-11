#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
An n-bit gray code sequence is a sequence of 2n integers where:

	Every integer is in the inclusive range [0, 2n - 1],
	The first integer is 0,
	An integer appears no more than once in the sequence,
	The binary representation of every pair of adjacent integers differs by exactly one bit, and
	The binary representation of the first and last integers differs by exactly one bit.

Given an integer n, return any valid n-bit gray code sequence.

Example 1:

Input: n = 2
Output: [0,1,3,2]
Explanation:
The binary representation of [0,1,3,2] is [00,01,11,10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- 00 and 10 differ by one bit
- 10 and 11 differ by one bit
- 11 and 01 differ by one bit
- 01 and 00 differ by one bit

Example 2:

Input: n = 1
Output: [0,1]

Constraints:

	1 <= n <= 16
"""
import sys
from typing import List
import pytest


class Solution:
    def grayCode(self, n):
        """05/04/2018 22:21

        0110011001100110
        0011110000111100
        0000111111110000
        0000000011111111
        j'th status of i'th position:
            0, where j <= 2**i or ((j - 2**i) / (2**(i+1))) % 2 == 1
            1, where ((j - 2**i) / (2**(i+1))) % 2 == 0
        """
        return [sum((2**i) * (((j+(2**i)) // (2**(i+1))) % 2) for i in range(n)) for j in range(2**n)]

    def grayCode(self, n: int) -> List[int]:
        """
        Recursion
        Time complexity: O(n * 2^n)
        Space complexity: O(2^n)
        """
        if n == 1:
            return [0,1]
        most_significant_bit = 1 << (n-1)
        sub = self.grayCode(n-1)
        return sub + [most_significant_bit + x for x in reversed(sub)]


@pytest.mark.parametrize('n, expected', [
    (2, [0,1,3,2]),
    (1, [0,1]),
])
def test(n, expected):
    assert expected == Solution().grayCode(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
