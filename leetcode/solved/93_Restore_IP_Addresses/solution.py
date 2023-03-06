#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

	For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Constraints:

	1 <= s.length <= 20
	s consists of digits only.
"""
from typing import List
import pytest
import sys


class Solution:
    def restoreIpAddresses(self, s):
        """May 06, 2018 03:02"""
        def restoreSplittedIpAddresses(s):
            memo = {}
            if s in memo:
                return memo[s]
            if len(s) == 0:
                return [[]]
            elif len(s) == 1:
                return [[s]]
            ret = []
            if len(s) >= 3 and s[0] != '0' and int(s[:3]) < 256:
                ret.extend([[s[:3]] + sub for sub in restoreSplittedIpAddresses(s[3:]) if len(sub) < 4])
            if len(s) >= 2 and s[0] != '0':
                ret.extend([[s[:2]] + sub for sub in restoreSplittedIpAddresses(s[2:]) if len(sub) < 4])
            ret.extend([[s[:1]] + sub for sub in restoreSplittedIpAddresses(s[1:]) if len(sub) < 4])
            memo[s] = ret
            return ret

        return ['.'.join(x) for x in restoreSplittedIpAddresses(s) if len(x) == 4]

    def restoreIpAddresses(self, s: str) -> List[str]:
        """Mar 05, 2023 23:02"""
        def dfs(i, remain):
            if remain == 0:
                if i == len(s):
                    return [[]]
                else:
                    return []
            if i >= len(s):
                return []

            ret = []
            for j in range(1, 4):
                n = int(s[i:i+j])
                if 0 <= n <= 255:
                    ret.extend([s[i:i+j], *x] for x in dfs(i+j, remain-1))
                if n == 0 or n > 255:
                    break
            return ret

        return ['.'.join(x) for x in dfs(0, 4)]


@pytest.mark.parametrize('args', [
    (("25525511135", ["255.255.11.135","255.255.111.35"])),
    (("0000", ["0.0.0.0"])),
    (("101023", ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"])),
])
def test(args):
    actual = Solution().restoreIpAddresses(*args[:-1])
    print(actual)
    assert sorted(args[-1]) == sorted(actual)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
