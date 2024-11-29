#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

Example 1:

Input: n = "123"
Output: "121"

Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.

Constraints:

	1 <= n.length <= 18
	n consists of only digits.
	n does not have leading zeros.
	n is representing an integer in the range [1, 1018 - 1].
"""
import pytest
import sys


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        m = (l+1)//2
        prefix = n[:m]
        candidates = [10**k + d for k in (l-1, l) for d in (-1, 1)]
        p = int(prefix)
        for pre in map(str, (p+1, p, p-1)):
            candidates.append(pre + (pre if l%2 == 0 else pre[:-1])[::-1])
        print(candidates)
        m = int(n)
        return str(min([(abs(int(c) - m), int(c)) for c in candidates if str(c) != n])[1])

    def nearestPalindromic(self, n: str) -> str:
        """Nov 13, 2024 09:08"""
        def to_palindrom(half, even=False):
            half = str(half)
            if even:
                return half + half[::-1]
            else:
                return half + half[:-1][::-1]

        if len(n) == 1:
            return "1" if n == 0 else str(int(n)-1)
        N = int(n)
        palindromes = list(map(int, filter(lambda x: x != n, [
            "9"*(len(n)-1),  # lower bound
            "1" + "0"*(len(n)-1) + "1",  # upper bound
            n[:(len(n)+1)//2] + n[:len(n)//2][::-1],  # trivial
            to_palindrom(int(n[:(len(n)+1)//2]) + 1, len(n)%2 == 0),
            to_palindrom(int(n[:(len(n)+1)//2]) - 1, len(n)%2 == 0),
        ])))
        return str(min(palindromes, key=lambda x: (abs(N-x), x)))


@pytest.mark.parametrize('args', [
    (("123", "121")),
    (("1", "0")),
    (("1213", "1221")),
    (("11", "9")),
    (("99", "101")),
    (("11911", "11811")),
    (("1283", "1331")),
    (('11199', '11211')),
    (('112999', '113311')),
    (('100000', '99999')),
    (('1999999', '2000002')),
])
def test(args):
    assert args[-1] == Solution().nearestPalindromic(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
