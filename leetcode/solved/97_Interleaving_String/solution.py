#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

"""
from functools import lru_cache

class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        if not s3:
            return True
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        return self.foo(0, 0)

    @lru_cache(maxsize=None)
    def foo(self, i, j):
        k = i + j
        if k == len(self.s3):
            return True
        return (i < len(self.s1) and self.s1[i] == self.s3[k] and self.foo(i+1, j))\
            or (j < len(self.s2) and self.s2[j] == self.s3[k] and self.foo(i, j+1))



def main():
    # s1 = input()
    # s2 = input()
    # s3 = input()
    s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
    s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
    s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    print(Solution().isInterleave(s1, s2, s3))


if __name__ == '__main__':
    main()
