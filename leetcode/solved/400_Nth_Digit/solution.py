
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n 31).

Example 1:

Input:
3

Output:
3

Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""
import pytest


class Solution:
    def findNthDigit(self, n: int) -> int:
        # 9
        # 2 * 10 (10 - 19) * 9
        # 3 * 100 (100 - 199) * 9
        i = 0
        cnt = 0
        while cnt < n:
            cnt += (i + 1) * pow(10, i) * 9
            i += 1
        cnt -= i * pow(10, i - 1) * 9
        n -= cnt
        n -= 1
        # nth digit of seq of numbers of length i
        return self.find_nth_of_length_i(n, i)

    def find_nth_of_length_i(self, n, i):
        # 100000 100001 100002 ... 999998 999999
        first_digit = (n // (i * pow(10, i - 1))) + 1
        n = n % (i * pow(10, i - 1))
        if n % i == 0:
            return first_digit
        j = 2
        while n:
            jth_digit = (n // (i * pow(10, i - j)))
            n = n % (i * pow(10, i - j))
            if n % i == j - 1:
                return jth_digit
            j += 1


def findNthDigit(n):
    n -= 1
    for i in range(1, n + 2):
        s = str(i)
        if n < len(s):
            return int(s[n])
        n -= len(s)


@pytest.mark.parametrize('n, expected', [
    (i, findNthDigit(i))
    for i in range(1, 300)
])
def test(n, expected):
    assert expected == Solution().findNthDigit(n)
