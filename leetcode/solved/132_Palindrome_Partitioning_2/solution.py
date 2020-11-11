#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
import pytest
import inspect


def log(*msg):
    stack = inspect.stack()[1:]
    ntab = 0
    fname = stack[0].function
    while stack[0].function == fname:
        ntab += 1
        stack.pop(0)
    print(fname, '\t'*ntab, *msg)


def is_palindrome(s):
    return s[len(s)//2:] == s[(len(s)-1)//2::-1]


class Solution:
    def minCut2(self, s: str) -> int:
        palindrome = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            palindrome[i][i] = True
        for i in range(len(s) - 1):
            palindrome[i][i + 1] = s[i] == s[i + 1]
        for k in range(2, len(s)):
            for i in range(len(s) - k):
                palindrome[i][i+k] = palindrome[i+1][i+k-1] and s[i] == s[i+k]

        cut = [float('inf')] * len(s)
        cut[0] = 0
        for j in range(len(cut)):
            if palindrome[0][j]:
                cut[j] = 0
            else:
                for i in range(0, j):
                    if palindrome[j-i][j]:
                        cut[j] = min(cut[j], cut[j-i-1] + 1)
        return cut[-1]

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        self.memo = [None for _ in s]
        # self.m = len(s)-1
        # partitions = self.min_part(0, 0)
        # list(map(print, partitions))
        # return self.m
        return self.n_cut(0)

    def n_cut(self, i):
        if self.memo[i]:
            return self.memo[i]
        if is_palindrome(self.s[i:]):
            self.memo[i] = 0
            return 0
        for j in range(1, len(self.s)):
            if is_palindrome(self.s[:j]) and is_palindrome(self.s[j:]):
                self.memo[i] = 1
                return 1
        m = float('inf')
        for j in range(len(self.s)-1, i, -1):
            if is_palindrome(self.s[i:j]):
                m = min(m, 1 + self.n_cut(j))
        self.memo[i] = m
        return self.memo[i]

    def min_part(self, i, d):
        if d >= self.m:
            return []
        if is_palindrome(self.s[i:]):
            self.m = d
            return [[self.s[i:]]]
        if self.memo[i]:
            self.m = min(self.m, *[len(x)-1+d for x in self.memo[i]])
            return [x for x in self.memo[i] if len(x)-1+d <= self.m]
        ret = []
        for j in range(len(self.s)-1, i, -1):
            if is_palindrome(self.s[i:j]):
                ret.extend([[self.s[i:j], *p] for p in self.min_part(j, d+1)])
        self.memo[i] = [x for x in ret if len(x)-1+d <= self.m]
        return self.memo[i]


@pytest.mark.parametrize('s, expected', [
    ('aab', 1),
    ("abcccb", 1),
    ("abcde", 4),
    ("abcdefghijklmnopqrstuvwxyz", 25),
    ("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", 51),
    ("eegiicgaeadbcfacfhifdbiehbgejcaeggcgbahfcajfhjjdgj", 42),
    ("efe", 0),
    ("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp", 452),
    ("adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece", 273)
])
def test(s, expected):
    assert expected == Solution().minCut(s)
