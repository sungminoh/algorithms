#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
 'P' : Present.

A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:

Input: n = 2
Output: 8
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times.

Note:
The value of n won't exceed 100,000.
"""
import sys
import pytest


MOD = 10**9 + 7


def matmul(m, n):
    if not m:
        return n
    if not n:
        return m
    a, b, c = len(m), len(n), len(n[0])
    ret = [[0]*c for _ in range(a)]
    for i in range(a):
        for j in range(b):
            for k in range(c):
                ret[i][k] += (m[i][j]%MOD) * (n[j][k]%MOD)
    return ret


def matadd(m, n):
    if m is None:
        return n
    if not n:
        return m
    a, b = len(m), len(m[0])
    ret = [[0]*b for _ in range(a)]
    for i in range(a):
        for j in range(b):
            ret[i][j] = (m[i][j] + n[i][j])%MOD
    return ret


class Solution:
    def checkRecord(self, n: int) -> int:
        mat = [[0, 1, 1, 0, 0, 1],
               [0, 0, 1, 0, 0 ,1],
               [1, 0, 1, 0, 0, 1],
               [0, 0, 0, 0, 1, 1],
               [0, 0, 0, 0, 0, 1],
               [0, 0, 0, 1, 0, 1]]
        v = [1, 0, 1, 0, 0, 1]
        ret = None
        for i, k in enumerate(reversed(bin(n-1)[2:])):
            if k == '1':
                ret = matmul(ret, mat)
            mat = matmul(mat, mat)
        return int(sum(matmul([v], ret)[0]) % MOD)

    def _checkRecord(self, n: int) -> int:
        m = 10**9 + 7
        l, ll, p, al, al2, ap = 1, 0, 1, 0, 0, 1
        for _ in range(n-1):
            l, ll, p, al, al2, ap \
                = p, l, (p+l+ll)%m, ap, al, (l+ll+p+ap+al+al2)%m
        return int((l + ll + p + al + al2 + ap) % m)

    def _checkRecord(self, n: int) -> int:
        def l_ll_p_a_al_all_ap(n):
            if n == 1:
                return 1, 0, 1, 1, 0, 0, 0
            l, ll, p, a, al, al2, ap = l_ll_p_a_al_all_ap(n-1)
            # p  # l
            # l  # ll
            # p + l + ll  # p
            # l + ll + p  # a
            # a + ap  # al
            # al  # all
            # a + al + al2  # ap
            return p, l, p+l+ll, l+ll+p, a+ap, al, a+ap+al+al2

        return int(sum(l_ll_p_a_al_all_ap(n)) % (pow(10,9)+7))


@pytest.mark.parametrize('n, expected', [
    (2, 8),
    (3, 19),
    (4, 43),
    (100, 985598218),
    (44444, 551678027),
    (55555, 179758661),
])
def test(n, expected):
    assert expected == Solution().checkRecord(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
