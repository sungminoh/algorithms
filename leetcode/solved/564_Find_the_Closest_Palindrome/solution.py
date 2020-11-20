#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:

Input: "123"
Output: "121"

Note:

The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
"""
import sys
import pytest


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


@pytest.mark.parametrize('n, expected', [
    ('123', '121'),
    ('99', '101'),
    ('11199', '11211'),
    ('112999', '113311'),
    ('100000', '99999'),
    ('1999999', '2000002'),
])
def test(n, expected):
    assert expected == Solution().nearestPalindromic(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
