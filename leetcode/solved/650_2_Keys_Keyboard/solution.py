#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

	Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
	Paste: You can paste the characters which are copied last time.

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:

Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

Note:

	The n will be in the range [1, 1000].
"""
import sys
from functools import lru_cache
import pytest


class Solution:
    def minSteps(self, n: int) -> int:
        @lru_cache(None)
        def rec(n):
            if n == 1:
                return 0
            m = float('inf')
            for i in range(1, n):
                if n % i == 0:
                    m =min(m, rec(i) + (n//i))
            return m
        return rec(n)


@pytest.mark.parametrize('n, expected', [
    (3, 3),
])
def test(n, expected):
    assert expected == Solution().minSteps(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
