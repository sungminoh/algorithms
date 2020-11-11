#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A password is considered strong if below conditions are all met:

 It has at least 6 characters and at most 20 characters.
 It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
 It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).

Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one change.
"""
import sys
import pytest


class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        def num_missing_chars(s):
            missed = [1, 1, 1]
            for c in s:
                if 'A' <= c <= 'Z':
                    missed[0] = 0
                elif 'a' <= c <= 'z':
                    missed[1] = 0
                elif '0' <= c <= '9':
                    missed[2] = 0
            return sum(missed)

        cnt = num_missing_chars(s)

        delete = 0
        if len(s) < 6:
            return max(cnt, 6 - len(s))
        elif len(s) > 20:
            delete = len(s) - 20

        replace = 0
        one, two = 0, 0
        i = 0
        while i < len(s):
            repeat_len = 1
            while i + repeat_len < len(s) and s[i] == s[i+repeat_len]:
                repeat_len += 1
            if repeat_len >= 3:
                replace += repeat_len//3
                if repeat_len % 3 == 0: one += 1
                if repeat_len % 3 == 1: two += 1
            i += repeat_len

        if delete == 0:
            return max(cnt, replace)

        replace -= min(delete, one)
        replace -= min(max(0, delete-one), 2*two) // 2
        replace -= max(0, delete-one-2*two) // 3
        return delete + max(cnt, replace)




@pytest.mark.parametrize('s, expected', [
    ("aaaaaaaaaaaaAsaxqwd1aaaa" , 7)
])
def test(s, expected):
    assert expected == Solution().strongPasswordChecker(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
