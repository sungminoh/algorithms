#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:

	If version1 < version2, return -1.
	If version1 > version2, return 1.
	Otherwise, return 0.

Example 1:

Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 2:

Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: version1 does not specify revision 2, which means it is treated as "0".

Example 3:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.

Constraints:

	1 <= version1.length, version2.length <= 500
	version1 and version2 only contain digits and '.'.
	version1 and version2 are valid version numbers.
	All the given revisions in version1 and version2 can be stored in a 32-bit integer.
"""
from itertools import zip_longest
import sys
import pytest


class Solution:
    def compareVersion(self, version1, version2):
        """07/28/2018 17:50"""
        from itertools import zip_longest
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]
        for a, b in zip_longest(v1, v2):
            a = a or 0
            b = b or 0
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0

    def compareVersion(self, version1: str, version2: str) -> int:
        for n1, n2 in zip_longest(version1.split('.'), version2.split('.')):
            n1 = n1.lstrip('0') if n1 else ''
            n1 = int(n1 or '0')
            n2 = n2.lstrip('0') if n2 else ''
            n2 = int(n2 or '0')
            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1
        return 0


@pytest.mark.parametrize('version1, version2, expected', [
    ("1.01", "1.001", 0),
    ("1.0", "1.0.0", 0),
    ("0.1", "1.1", -1),
    ("1.0.1", "1", 1),
    ("1.2", "1.10", -1),
])
def test(version1, version2, expected):
    assert expected == Solution().compareVersion(version1, version2)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
