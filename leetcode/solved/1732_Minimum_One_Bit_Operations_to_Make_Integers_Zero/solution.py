#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer n, you must transform it into 0 using the following operations any number of times:

	Change the rightmost (0th) bit in the binary representation of n.
	Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.

Return the minimum number of operations to transform n into 0.

Example 1:

Input: n = 3
Output: 2
Explanation: The binary representation of 3 is "11".
"11" -> "01" with the 2nd operation since the 0th bit is 1.
"01" -> "00" with the 1st operation.

Example 2:

Input: n = 6
Output: 4
Explanation: The binary representation of 6 is "110".
"110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
"010" -> "011" with the 1st operation.
"011" -> "001" with the 2nd operation since the 0th bit is 1.
"001" -> "000" with the 1st operation.

Constraints:

	0 <= n <= 109
"""
import pytest
import sys


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        """Feb 04, 2024 12:24"""
        b = '0' + bin(n)[2:]
        first = 0
        ret = 0
        for i in range(1, len(b)):
            d = len(b)-1-i
            if first == 0:
                if b[i] == '1':
                    ret += 2**d
                    first = 1
                else:
                    first = 0
            else:
                if b[i] == '0':
                    ret += 2**d
                    first = 1
                else:
                    first = 0
        return ret


@pytest.mark.parametrize('args', [
    ((3, 2)),
    ((6, 4)),
    ((9, 14)),
])
def test(args):
    assert args[-1] == Solution().minimumOneBitOperations(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
