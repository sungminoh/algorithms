#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""


class Solution:
    memo = {}

    def restoreSplittedIpAddresses(self, s):
        if s in self.memo:
            return self.memo[s]
        if len(s) == 0:
            return [[]]
        elif len(s) == 1:
            return [[s]]
        ret = []
        if len(s) >= 3 and s[0] != '0' and int(s[:3]) < 256:
            ret.extend([[s[:3]] + sub for sub in self.restoreSplittedIpAddresses(s[3:]) if len(sub) < 4])
        if len(s) >= 2 and s[0] != '0':
            ret.extend([[s[:2]] + sub for sub in self.restoreSplittedIpAddresses(s[2:]) if len(sub) < 4])
        ret.extend([[s[:1]] + sub for sub in self.restoreSplittedIpAddresses(s[1:]) if len(sub) < 4])
        self.memo[s] = ret
        return ret

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return ['.'.join(x) for x in self.restoreSplittedIpAddresses(s) if len(x) == 4]


def main():
    print(Solution().restoreIpAddresses(input()))


if __name__ == '__main__':
    main()
