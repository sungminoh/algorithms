#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""


class Solution:
    memo = {}
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s in self.memo:
            return self.memo[s]
        if len(s) == 0:
            return 1
        if int(s[0]) == 0:
            return 0
        n = self.numDecodings(s[1:])
        if 10 <= int(s[:2]) <= 26:
            n += self.numDecodings(s[2:])
        self.memo[s] = n
        return n


def main():
    print(Solution().numDecodings(input()))


if __name__ == '__main__':
    main()
