#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

	Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
	Each vowel 'a' may only be followed by an 'e'.
	Each vowel 'e' may only be followed by an 'a' or an 'i'.
	Each vowel 'i' may not be followed by another 'i'.
	Each vowel 'o' may only be followed by an 'i' or a 'u'.
	Each vowel 'u' may only be followed by an 'a'.

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".

Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".

Example 3: 

Input: n = 5
Output: 68

Constraints:

	1 <= n <= 2 * 10^4
"""
from functools import lru_cache
import sys
import pytest


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """08/11/2021 13:39 TLE"""
        m = {'a': 'e', 'e': 'ai', 'i': 'aeou', 'o': 'iu', 'u': 'a'}
        visited = set()

        @lru_cache(None)
        def dfs(n, cur):
            if n == 0:
                visited.add(cur)
            else:
                for c in (m[cur[-1]] if cur else m.keys()):
                    dfs(n-1, cur + c)

        dfs(n, '')
        return len(visited) % int(1e9+7)

    def countVowelPermutation(self, n: int) -> int:
        """08/11/2021 14:06
              a  e  i  o  u
        a -> [0, 1, 0, 0, 0]
        e -> [1, 0, 1, 0, 0]
        i -> [1, 1, 0, 1, 1]
        o -> [0, 0, 1, 0, 1]
        u -> [1, 0, 0, 0, 0]
        Time complexity: O(logn)
        Space complexity: O(1)
        """
        mod = int(1e9+7)
        mat = [
            [0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0]
        ]

        def matplus(a, b):
            if not a:
                return b
            if not b:
                return a
            return [[(ea+eb)%mod for ea, eb in zip(ra, rb)] for ra, rb in zip(a, b)]

        def matmul(a, b):
            if not a:
                return b
            if not b:
                return a
            ret = [[0]*len(b[0]) for _ in range(len(a))]
            for i in range(len(ret)):
                for k in range(len(a[0])):
                    for j in range(len(ret[0])):
                        ret[i][j] += a[i][k] * b[k][j]
            return ret

        def element_mat(n):
            ret = []
            for i in range(n):
                row = [0]*n
                row[i] = 1
                ret.append(row)
            return ret

        def matpow(m, p):
            ret = element_mat(len(m))
            while p:
                if p%2:
                    ret = matmul(ret, m)
                m = matmul(m, m)
                p = p >> 1
            return ret

        return sum(matmul([[1,1,1,1,1]], matpow(mat, n-1))[0])%mod

    def countVowelPermutation(self, n: int) -> int:
        """08/11/2021 14:13
        Time complexity: O(n)
        Space complexity: O(1)
        """
        mod = int(1e9+7)
        a=e=i=o=u=1
        for _ in range(n-1):
            a,e,i,o,u = (x%mod for x in [(e+i+u), (a+i), (e+o), i, (i+o)])
        return (a+e+i+o+u)%mod

    def countVowelPermutation(self, n: int) -> int:
        """08/21/2022 16:11
        Top-down
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        MOD = int(1e9+7)
        def dfs(n):
            assert n>=1
            if n == 1:
                return 1,1,1,1,1
            a,e,i,o,u = dfs(n-1)
            return (x%MOD for x in [e+u+i,a+i,e+o,i,o+i])

        return sum(dfs(n))%MOD

    def countVowelPermutation(self, n: int) -> int:
        """08/21/2022 16:13
        Bottom-up
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if n == 0:
            return 0
        MOD = int(1e9+7)
        a,e,i,o,u = 1,1,1,1,1
        for _ in range(n-1):
            a,e,i,o,u = (x%MOD for x in [e+u+i,a+i,e+o,i,o+i])
        return (a+e+i+o+u) % MOD

    def countVowelPermutation(self, n: int) -> int:
        """08/21/2022 17:01
        Time Complexity: O(logn)
        Space Complexity: O(1)
        """
        if n == 0:
            return 0

        MOD = int(1e9+7)

        def mul(m1, m2):
            ret = [[0]*len(m2[0]) for _ in range(len(m1))]
            for i in range(len(m1)):
                for k in range(len(m2)):
                    for j in range(len(m2[0])):
                        ret[i][j] += m1[i][k] * m2[k][j]
            return ret

        mat = [[0,1,0,0,0],  # a -> e
               [1,0,1,0,0],  # e -> a, i
               [1,1,0,1,1],  # i -> !i
               [0,0,1,0,1],  # o -> i, u
               [1,0,0,0,0]]  # u -> a

        # [1,1,1,1,1] * mat^(n-1)
        # mat^(n-1) = mat^p0 * mat^p1 * ... mat^pk
        #  where pi = 2^i and sum(pi) = n-1
        cur = [[1,0,0,0,0],
               [0,1,0,0,0],
               [0,0,1,0,0],
               [0,0,0,1,0],
               [0,0,0,0,1]]
        n -= 1
        while n:
            if n%2 == 1:
                cur = mul(cur, mat)
            mat = mul(mat, mat)
            n >>= 1
        return sum(mul([[1,1,1,1,1]], cur)[0])%MOD


@pytest.mark.parametrize('n, expected', [
    (1, 5),
    (2, 10),
    (5, 68),
    (144, 18208803),
])
def test(n, expected):
    assert expected == Solution().countVowelPermutation(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
