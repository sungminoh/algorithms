#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        cnt = {c: 0 for c in s}
        cnt[s[0]] = 1
        size = 1
        j = 0
        fi = fj = 0
        for i in range(1, len(s)):
            cnt[s[i]] += 1
            while cnt[s[i]] > 1:
                cnt[s[j]] -= 1
                j += 1
            if i - j + 1 > size:
                size = i - j + 1
                fi = i
                fj = j
        return s[fj:fi+1]
        # return size


def main():
    print(Solution().lengthOfLongestSubstring(input()))


if __name__ == '__main__':
    main()
