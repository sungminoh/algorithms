#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

"""
from collections import defaultdict


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # trivial case
        self.s = s
        self.p = p
        self.memo = defaultdict(defaultdict)
        return self.is_match(0, 0)

    def is_match(self, i, j):
        s, p = self.s, self.p
        if i >= len(s) and j >= len(p):
            return True
        elif j >= len(p):
            return False
        elif i >= len(s):
            if j < len(p)-1 and p[j+1] == '*':
                return self.is_match(i, j+2)
            else:
                return False
        if j in self.memo[i]:
            return self.memo[i][j]
        if j+1 < len(p) and p[j+1] == '*':
            self.memo[i][j] = self.is_match(i, j+2) \
                or ((s[i] == p[j] or p[j] == '.') and self.is_match(i+1, j))
        else:
            self.memo[i][j] = ((s[i] == p[j] or p[j] == '.') and self.is_match(i+1, j+1))
        return self.memo[i][j]


def main():
    s = input()
    p = input()
    print(Solution().isMatch(s, p))


if __name__ == '__main__':
    main()
