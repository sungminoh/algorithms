#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Constraints:

	1 <= s.length <= 104
	s contains English letters (upper-case and lower-case), digits, and spaces ' '.
	There is at least one word in s.

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
"""
import pytest
import sys


class Solution:
    def reverseWords(self, s):
        """07/27/2018 20:40	"""
        def reverse(lst, i, j):
            while i < j:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1

        # trim and remove multiple whitespaces
        import re
        s = re.sub(r'\s+', ' ', s.strip())
        # return trivial case
        if not s:
            return ''

        lst = list(s)
        # reverse
        reverse(lst, 0, len(lst)-1)
        # reverse each word
        i = 0
        for j, c in enumerate(lst):
            if c == ' ':
                reverse(lst, i, j-1)
                i = j+1
        else:
            reverse(lst, i, j)
        return ''.join(lst)

    def reverseWords(self, s: str) -> str:
        # use list as mutable string
        s = list(s)

        # compress
        end = len(s)-1
        while s[end] == ' ':
            end -= 1

        i = 0
        for j in range(end+1):
            c = s[j]
            if c == ' ' and (i == 0 or s[i-1] == ' '):
                continue
            s[i] = c
            i += 1
        length = i

        # reverse
        def reverse(arr, i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        reverse(s, 0, length-1)

        # reverse words back
        i = 0
        for j in range(length):
            if s[j] == ' ':
                reverse(s, i, j-1)
                i = j+1
        reverse(s, i, length-1)

        return ''.join(s[:length])


    def reverseWords(self, s: str) -> str:
        """11/19/2022 13:36"""
        return ' '.join(reversed(s.split()))

    def reverseWords(self, s: str) -> str:
        """11/20/2022 13:22"""
        s = list(s)

        def compress(s):
            i = j = 0
            p = ' '
            while i < len(s):
                if not (p == ' ' and s[i] == ' '):
                    s[j] = s[i]
                    j += 1
                p = s[i]
                i += 1
            while s[j-1] == ' ':
                j -= 1
                s[j] = ''
            while j < len(s):
                s[j] = ''
                j += 1

        def reverse(i, j, s):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        def find_all_words(s):
            ret = []
            i = j = 0
            while i < len(s):
                if s[i] == ' ' and i != j:
                    yield j, i-1
                    i += 1
                    j = i
                else:
                    i += 1
            if j != i:
                yield j, i-1
            return ret

        compress(s)
        for i, j in find_all_words(s):
            reverse(i, j, s)
        reverse(0, len(s)-1, s)
        return ''.join(s)


@pytest.mark.parametrize('s, expected', [
    ("the sky is blue", "blue is sky the"),
    ("  hello world  ", "world hello"),
    ("a good   example", "example good a"),
    ("  Bob    Loves  Alice   ", "Alice Loves Bob"),
    ("Alice does not even like bob", "bob like even not does Alice"),
])
def test(s, expected):
    assert expected == Solution().reverseWords(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
