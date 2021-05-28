#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.

Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right].

Example 1:

Input: left = "4", right = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.

Example 2:

Input: left = "1", right = "2"
Output: 1

Constraints:

	1 <= left.length, right.length <= 18
	left and right consist of only digits.
	left and right cannot have leading zeros.
	left and right represent integers in the range [1, 1018 - 1].
	left is less than or equal to right.
"""
import bisect
from functools import lru_cache
import sys
import math
import pytest


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        """
        Bruteforce
        Time complexity: O(n^0.5 * logn)  # num iteration, palindrome check
        Space complexity: O(n^0.5)  # memo palindrome check
        """
        @lru_cache(None)
        def is_palindrome(s):
            s = str(s)
            return s == s[::-1]

        left, right = int(left), int(right)
        cnt = 0
        for i in range(math.ceil(left**0.5), math.floor(right**0.5)+1):
            if is_palindrome(i) and is_palindrome(i**2):
                cnt +=1
        return cnt

    def superpalindromesInRange(self, left: str, right: str) -> int:
        """
        Constructs all palindromes that has a length in a certain range
        and check if square is also a palindrome
        Time complexity: O(logn * log(logn) + a)
            build: log(n)
            sort: log(n)*log(log(n))
            bisearch: log(a) where a is the number of all palindromes
            check: a
        Space complexity: O(a)
        a is unknown?
        """
        def is_palindrome(s):
            s = str(s)
            return s == s[::-1]

        def all_palindromes(n, m):
            ret = []
            if n == 1:
                ret.extend(range(10))
            for i in range(10**((n-1)//2), 10**(m//2)):
                pre = str(i)
                post = pre[::-1]
                if len(pre)*2 >= n:
                    ret.append(int(pre + post))
                if n-1 <= len(pre)*2 < m:
                    for d in '0123456789':
                        ret.append(int(pre + d + post))
            return ret

        left, right = int(left), int(right)
        # min_length = len(str(math.floor((left/10)**0.5)))
        min_length = 1
        max_length = len(str(math.floor(right**0.5)))
        palindromes = all_palindromes(min_length, max_length)
        palindromes.sort()
        i = bisect.bisect_left(palindromes, math.ceil(left**0.5))
        cnt = 0
        while i < len(palindromes):
            square = palindromes[i] ** 2
            if square > right:
                break
            if is_palindrome(square):
                cnt += 1
            i += 1
        return cnt


@pytest.mark.parametrize('left, right, expected', [
    ("4", "1000", 4),
    ("1", "2", 1),
    ("1020762146323", "142246798855636", 17),
    ("40000000000000000", "50000000000000000", 2),
])
def test(left, right, expected):
    assert expected == Solution().superpalindromesInRange(left, right)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
