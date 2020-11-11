#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Define S = [s,n] as the string S which consists of n connected strings s. For example, ["abc", 3] ="abcabcabc".
On the other hand, we define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1. For example, “abc”  can be obtained from “abdbec” based on our definition, but it can not be obtained from “acbbe”.
You are given two non-empty strings s1 and s2 (each at most 100 characters long) and two integers 0 ≤ n1 ≤ 106 and 1 ≤ n2 ≤ 106. Now consider the strings S1 and S2, where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] can be obtained from S1.

Example:

Input:
s1="acb", n1=4
s2="ab", n2=2

Return:
2
"""
import sys
import pytest


class Solution:
    def _getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        ret = 0
        i = 0
        j = 0
        while i < len(s1)*n1:
            while i < len(s1)*n1 and s1[i%len(s1)] != s2[j%len(s2)]:
                i += 1
            if i == len(s1)*n1:
                return ret
            i += 1
            j += 1
            if j % (len(s2)*n2) == 0:
                ret += 1
        return ret

    def _getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        memo = {}
        j = 0
        m = 0
        for n in range(1, n1+1):
            for i, c in enumerate(s1):
                if s1[i] == s2[j]:
                    j += 1
                    if j % len(s2) == 0:
                        j = 0
                        m += 1
            if j in memo:
                prev_n, prev_m = memo[j]
                repeat_per_cycle = m - prev_m
                used_per_cycle = n - prev_n
                repeat = ((n1 - prev_n) // used_per_cycle) * repeat_per_cycle
                remainder = (n1 - prev_n) % used_per_cycle + prev_n
                for k, (_n, _m) in memo.items():
                    if _n == remainder:
                        repeat += _m
                        break
                return repeat // n2
            else:
                memo[j] = (n, m)
        return m // n2

    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        memo = {}
        n, m = 1, 0
        i, j = 0, 0
        while n <= n1:
            if s1[i] == s2[j]:
                j += 1
            if j == len(s2):
                m += 1
                j = 0
                if i not in memo:
                    memo[i] = (n, m)
                else:
                    prev_n, prev_m = memo[i]
                    used_s1, used_s2 = n-prev_n, m-prev_m
                    repeat = ((n1-prev_n)//used_s1) * used_s2
                    remainder = (n1-prev_n) % used_s1
                    n = n1-remainder
                    m = prev_m + repeat
            i += 1
            if i == len(s1):
                n += 1
                i = 0
        return m//n2


@pytest.mark.parametrize('s1, n1, s2, n2, expected', [
    ("acb", 4, "ab", 2, 2),
    ("phqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjpre", 1000000, "pggxr", 100, 10000),
    ("aaa", 3, "aa", 1, 4),
    ("aaa", 4, "aa", 1, 6),
    # aaa    aaa   aaa
    # aa a  a aa   aa
])
def test(s1, n1, s2, n2, expected):
    print()
    assert expected == Solution().getMaxRepetitions(s1, n1, s2, n2)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
