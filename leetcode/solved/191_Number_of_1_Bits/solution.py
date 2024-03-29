#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

	Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
	In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.

Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:

Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:

Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

Constraints:

	The input must be a binary string of length 32.

Follow up: If this function is called many times, how would you optimize it?
"""
import pytest
import sys


class Solution:
    def hammingWeight(self, n: int) -> int:
        """Jun 12, 2022 12:14"""
        ret = 0
        for _ in range(32):
            ret += n&1
            n >>= 1
        return ret

    def hammingWeight(self, n: int) -> int:
        """Feb 04, 2024 11:31"""
        ret = 0
        while n:
            ret += n%2
            n//=2
        return ret


@pytest.mark.parametrize('args', [
    (('00000000000000000000000000001011', 3)),
    (('00000000000000000000000010000000', 1)),
    (('11111111111111111111111111111101', 31)),
])
def test(args):
    assert args[-1] == Solution().hammingWeight(int(*args[:-1], 2))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
