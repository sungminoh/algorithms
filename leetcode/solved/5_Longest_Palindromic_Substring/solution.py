#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""


class Solution:
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
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


def main():
    print(Solution().longestPalindrome(input()))


if __name__ == '__main__':
    main()
