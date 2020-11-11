#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

"""
from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cnt = defaultdict(int)
        for c in t:
            cnt[c] += 1
        n_chars = len(t)
        l, r = 0, 0
        length = float('inf')
        start = 0

        while r < len(s):
            if s[r] in cnt:
                if cnt[s[r]] > 0:
                    n_chars -= 1
                cnt[s[r]] -= 1
            while n_chars <= 0:
                if r - l + 1 < length:
                    length = r - l + 1
                    start = l
                if s[l] in cnt:
                    cnt[s[l]] += 1
                    if cnt[s[l]] > 0:
                        n_chars += 1
                l += 1
            r += 1
        return s[start:start+length] if length < float('inf') else ''

    def _minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        if len(t) == 1:
            return t if t in s else ""

        self.cleared = set()
        self.chars = Counter(t)
        self.cnt = defaultdict(int)

        l = 0
        while l < len(s) and s[l] not in self.chars:
            l += 1
        if l == len(s):
            return ""

        self.found(s[l])

        r = l+1
        if r == len(s):
            return ""
        ret = s
        while r < len(s):
            if s[r] in self.chars:
                self.found(s[r])
                if s[r] == s[l] and self.cnt[s[r]] > self.chars[s[r]]:
                    self.pop(s[l])
                    l += 1
                    while l < r:
                        if s[l] in self.chars:
                            if self.cnt[s[l]] > self.chars[s[l]]:
                                self.pop(s[l])
                            else:
                                break
                        l += 1
                if len(self.cleared) == len(self.chars):
                    ret = min(ret, s[l:r+1], key=len)
            r += 1
        if len(self.cleared) == len(self.chars):
            return ret
        else:
            return ""

    def found(self, c):
        self.cnt[c] += 1
        if self.cnt[c] >= self.chars[c]:
            self.cleared.add(c)

    def pop(self, c):
        self.cnt[c] -= 1
        if self.cnt[c] < self.chars[c]:
            self.cleared.pop(c)



def main():
    s = input()
    t = input()
    print(Solution().minWindow(s, t))


if __name__ == '__main__':
    main()
