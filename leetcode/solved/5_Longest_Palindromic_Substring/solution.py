#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

	1 <= s.length <= 1000
	s consist of only digits and English letters.
"""
import sys
import pytest


class Solution:
    def longestPalindrome1(self, s):
        """12/30/2017 17:39"""
        n = len(s)

        def get_odd_palindrome_length_from(p):
            i = j = p
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            # print('odd from\t%s:\t%s' % (p, s[i+1:j]))
            return s[i+1:j]

        def get_even_palindrome_length_from(p):
            i, j = p, p+1
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            # print('even from\t%s:\t%s' % (p, s[i+1:j]))
            return s[i+1:j]

        ret = ''
        for i in range(len(s)):
            odd_palindrome = get_odd_palindrome_length_from(i)
            even_palindrome = get_even_palindrome_length_from(i)
            ret = max(ret, odd_palindrome, even_palindrome, key=len)
        return ret

    def longestPalindrome(self, s):
        """12/30/2017 18:32"""
        def is_palindrome(s):
            p = len(s)//2
            return s[:p] == s[-1:-p-1:-1]
        length = 1
        start = 0
        was = True
        if s == s[::-1]:
            return s
        for i in range(1, len(s)):
            if was and i-length-1 >= 0 and s[i-length-1] == s[i]:
                start = i-length-1
                length += 2
                continue
            if is_palindrome(s[i-length:i+1]):
                start = i-length
                length += 1
                was = True
                continue
            if is_palindrome(s[i-length+1:i+1]):
                was = True
            else:
                was = False
        return s[start:start+length]

    def longestPalindrome(self, s: str) -> str:
        """06/19/2022 18:10
        Manacher's algorithm
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        def manacher(s):
            """
            s = abcd -> s' = #a#b#c#d#
            """
            n = 2*len(s)+1

            def get(i):
                return None if i%2 == 0 else s[i//2]

            def expand(c, d):
                while c-d-1 >= 0 and c+d+1 < n and get(c-d-1) == get(c+d+1):
                    d += 1
                return d

            dists = [0]*n
            c = d = 0
            i = 0
            while i < n:
                if i > c+d:
                    dists[i] = expand(i, 0)
                else:
                    j = 2*c-i
                    if i + dists[j] == c+d:
                        dists[i] = expand(i, dists[j])
                        if i+dists[i] > c+d:
                            c, d = i, dists[i]
                    else:
                        dists[i] = dists[j]
                i += 1
            return dists

        def restore(c, d):
            return s[c//2 - d//2:c//2 + (d+1)//2]

        md = 0
        ret = ''
        for i, d in enumerate(manacher(s)):
            if d > md:
                md = d
                ret = restore(i, d)
        return ret


@pytest.mark.parametrize('s, expected', [
    ("babad", "bab"),
    ("cbbd", "bb"),
])
def test(s, expected):
    assert expected == Solution().longestPalindrome(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
