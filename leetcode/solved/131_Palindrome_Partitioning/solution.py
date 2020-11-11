#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
from collections import defaultdict

class Solution:
    def is_palindrome(self, i, j):
        while i < j:
            if self.s[i] != self.s[j-1]:
                return False
            i += 1
            j -= 1
        return True

    def part(self, i):
        if i == len(self.s):
            return [[]]
        if self.memo[i]:
            return self.memo[i]
        ret = self.memo[i]
        for j in range(i+1, len(self.s)+1):
            if self.is_palindrome(i, j):
                ret.extend([[self.s[i:j], *x]for x in self.part(j)])
        return ret

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.s = s
        self.memo = defaultdict(list)
        return self.part(0)


def main():
    s = input()
    print(Solution().partition(s))


if __name__ == '__main__':
    main()
