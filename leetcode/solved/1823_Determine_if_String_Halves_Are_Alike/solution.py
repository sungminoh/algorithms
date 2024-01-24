#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.

Constraints:

	2 <= s.length <= 1000
	s.length is even.
	s consists of uppercase and lowercase letters.
"""
import pytest
import sys


class Solution:
    VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    def halvesAreAlike(self, s: str) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        def count_vowels(s, i, j):
            cnt = 0
            while i < j:
                cnt += 1 if s[i] in self.VOWELS else 0
                i += 1
            return cnt

        return count_vowels(s, 0, len(s)//2) == count_vowels(s, len(s)//2, len(s))

    def halvesAreAlike(self, s: str) -> bool:
        counters = [0, 0]
        cur = 0
        for i, c in enumerate(s):
            if c in 'aeiouAEIOU':
                counters[i//(len(s)//2)] += 1
        return counters[0] == counters[1]


    def halvesAreAlike(self, s: str) -> bool:
        """"
        When all vowels need to be counted separately"
        """
        vowels = 'aeiouAEIOU'
        idx = {c: i for i, c in enumerate(vowels)}
        cnt = [0]*len(vowels)
        remain = 0
        for c in s:
            if c in idx:
                if cnt[idx[c]] == 0:
                    remain += 1
                cnt[idx[c]] += 1
        for i in range(len(cnt)):
            if cnt[i] % 2 == 1:
                return False
            cnt[i] //= 2
        for c in s:
            if c in idx:
                cnt[idx[c]] -= 1
                if cnt[idx[c]] == 0:
                    remain -= 1
        return remain == 0

    def halvesAreAlike(self, s: str) -> bool:
        """Jan 23, 2024 21:16"""
        vowels = set('aeiouAEIOU')
        counters = [0, 0]
        for i, c in enumerate(s):
            if c in vowels:
                counters[i//(len(s)//2)] += 1
        return counters[0] == counters[1]


@pytest.mark.parametrize('args', [
    (("book", True)),
    (("textbook", False)),
    (("MerryChristmas", False)),
    (("AbCdEfGh", True)),
    (('Uo', True)),
])
def test(args):
    assert args[-1] == Solution().halvesAreAlike(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
