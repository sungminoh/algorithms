#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer n represented as a string, return the smallest good base of n.

We call k >= 2 a good base of n, if all digits of n base k are 1's.

Example 1:

Input: n = "13"
Output: "3"
Explanation: 13 base 3 is 111.

Example 2:

Input: n = "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.

Example 3:

Input: n = "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.

Constraints:

	n is an integer in the range [3, 1018].
	n does not contain any leading zeros.
"""
import math
import pytest
import sys


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        cache = set()

        def is_goodbase(n: int, b: int):
            i = 1
            while n:
                if n%b != 1:
                    cache.add(b**i)
                    return False
                n //= b
                i += 1
            return True

        n = int(n)
        for i in range(2, n):
            if i not in cache and is_goodbase(n, i):
                return str(i)
        return str(n-1)

    def smallestGoodBase(self, n: str) -> str:
        """
        n = 1 + p + p^2 + ... + p^q < (p+1)^q
            -> n > p^q
            -> n < (p+1)^q
        (p-1)n = p^(q+1)-1
            -> n < p^(q+1) where p >= 2
        1. q < logp(n) < q+1
        2. p < n^(1/q) < p+1
        since p >= 2, q < log2(n)
        """
        n = int(n)
        for q in range(int(math.log2(n)), 1, -1):
            p = int(n**(1/q))
            if (p-1)*n == (p**(q+1))-1:
                return str(p)
        return str(n-1)


@pytest.mark.parametrize('n, expected', [
    ("13", "3"),
    ("4681", "8"),
    ("1000000000000000000", "999999999999999999"),
])
def test(n, expected):
    assert expected == Solution().smallestGoodBase(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
