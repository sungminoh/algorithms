#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:
Input: s = "God Ding"
Output: "doG gniD"

Constraints:

	1 <= s.length <= 5 * 104
	s contains printable ASCII characters.
	s does not contain any leading or trailing spaces.
	There is at least one word in s.
	All the words in s are separated by a single space.
"""
import pytest
import sys


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([x[::-1] for x in s.split()])


@pytest.mark.parametrize('s, expected', [
    ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
    ("God Ding", "doG gniD"),
])
def test(s, expected):
    assert expected == Solution().reverseWords(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
