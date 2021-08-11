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
import copy
import sys
from functools import lru_cache
import pytest


class Solution:
    """
    a (e)
    e (a,i)
    i (a,e,o,u)
    o (i,u)
    u (a)
    """
    def countVowelPermutation(self, n: int) -> int:
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
        """
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
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        mod = int(1e9+7)
        a=e=i=o=u=1
        for _ in range(n-1):
            a,e,i,o,u = (x%mod for x in [(e+i+u), (a+i), (e+o), i, (i+o)])
        return (a+e+i+o+u)%mod


@pytest.mark.parametrize('n, expected', [
    (1, 5),
    (2, 10),
    (5, 68),
    (144, 18208803)
])
def test(n, expected):
    assert expected == Solution().countVowelPermutation(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
