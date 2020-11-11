#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i, j = 0, 0
        i_, j_ = 0, -1
        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                i_, j_ = i, j
                j += 1
            elif j_ != -1:
                i_ += 1
                i, j = i_, j_+1
            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1
        return True if j == len(p) else False

    def _isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.s = s
        self.p = p
        if not s and not p:
            return True
        elif not p:
            return False

        self.memo = [[None for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        return self.im(0, 0)

    def im(self, i, j):
        s = self.s
        p = self.p
        if i >= len(s) and j >= len(p):
            return True
        elif j >= len(p):
            return False
        elif self.memo[i][j] is not None:
            return self.memo[i][j]
        print()
        print(s[i:])
        print(p[j:])

        if p[j] == '?':
            self.memo[i][j] = i < len(s) and self.im(i+1, j+1)
        elif p[j] == '*':
            self.memo[i][j] = self.im(i, j+1) or (i < len(s) and self.im(i+1, j))
        else:
            self.memo[i][j] = i < len(s) and s[i] == p[j] and self.im(i+1, j+1)
        return self.memo[i][j]




def main():
    s = input()
    p = input()
    # s = "aabababbaabbbbbaab"
    # p = "******a"
    print(Solution().isMatch(s, p))


if __name__ == '__main__':
    main()
