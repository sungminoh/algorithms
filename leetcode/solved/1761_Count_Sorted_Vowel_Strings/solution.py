#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

Example 3:

Input: n = 33
Output: 66045

Constraints:

	1 <= n <= 50
"""
import sys
from functools import lru_cache
import pytest


class Solution:
    def countVowelStrings(self, n: int) -> int:
        """
        Top down DP
        Time complexity: O(5*n)
        Space complexity: O(5*n)
        """
        # aeiou -> 01234
        @lru_cache(None)
        def dfs(i, n):
            if n == 0:
                return 1
            ret = 0
            for j in range(i, 5):
                ret += dfs(j, n-1)
            return ret

        return dfs(0, n)

    def countVowelStrings(self, n: int) -> int:
        """
        Bottom up DP
        Time complexity: O(5*n)
        Space complexity: O(5)
        """
        if n == 0:
            return 0
        aeiou = [1]*5
        for _ in range(n-1):
            acc = 0
            for i in range(5):
                acc += aeiou[i]
                aeiou[i] = acc
        return sum(aeiou)

    def countVowelStrings(self, n: int) -> int:
        """
        Among n+1 positions in the string of lengh n
        pick 4 places to change character.
        """
        return sum([
            (n+1)*(n)*(n-1)*(n-2)//24,  # nC4
            (n+1)*(n)*(n-1)*3//6,  # nC3 * 3(where to change char two times)
            (n+1)*(n)*3//2,  # nC2 * 3(Where to make two additional changes)
            (n+1)])  # nC1

    def countVowelStrings(self, n: int) -> int:
        """
        Multiset of size n from set of size 5 (aeiou)
        """
        # ((k, n)) the number of multiset of size n from a set of size k
        # = (k+n-1, n) the number of ways picking n from k+n-1 elements
        # ref to: https://en.wikipedia.org/wiki/Multiset#Counting_multisets
        # ((5, n)) = (n+4, n) = (n+4, 4)
        return (n+4)*(n+3)*(n+2)*(n+1)//24


@pytest.mark.parametrize('n, expected', [
    (1,5),
    (2,15),
    (33,66045),
])
def test(n, expected):
    assert expected == Solution().countVowelStrings(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))



