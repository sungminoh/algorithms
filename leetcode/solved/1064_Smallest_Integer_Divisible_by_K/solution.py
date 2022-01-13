#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

Return the length of n. If there is no such n, return -1.

Note: n may not fit in a 64-bit signed integer.

Example 1:

Input: k = 1
Output: 1
Explanation: The smallest answer is n = 1, which has length 1.

Example 2:

Input: k = 2
Output: -1
Explanation: There is no such positive integer n divisible by 2.

Example 3:

Input: k = 3
Output: 3
Explanation: The smallest answer is n = 111, which has length 3.

Constraints:

	1 <= k <= 105
"""
import sys
import pytest


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        l = 1
        r = 1%k
        visited = set()
        while r > 0:
            if r in visited:
                return -1
            visited.add(r)
            l += 1
            r = 10*r + 1
            r %= k
        return l


@pytest.mark.parametrize('k, expected', [
    (1, 1),
    (2, -1),
    (3, 3),
])
def test(k, expected):
    assert expected == Solution().smallestRepunitDivByK(k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
