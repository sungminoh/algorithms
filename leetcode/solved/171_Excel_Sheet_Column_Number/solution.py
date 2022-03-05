#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

Example 1:

Input: columnTitle = "A"
Output: 1

Example 2:

Input: columnTitle = "AB"
Output: 28

Example 3:

Input: columnTitle = "ZY"
Output: 701

Constraints:

	1 <= columnTitle.length <= 7
	columnTitle consists only of uppercase English letters.
	columnTitle is in the range ["A", "FXSHRXW"].
"""
import sys
import string
import pytest


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        m = {c: i for i, c in enumerate(string.ascii_uppercase, 1)}
        ret = 0
        base = 1
        for i in range(len(columnTitle)-1, -1, -1):
            ret += base*m[columnTitle[i]]
            base *= len(string.ascii_uppercase)
        return ret


@pytest.mark.parametrize('columnTitle, expected', [
    ("A", 1),
    ("AB", 28),
    ("ZY", 701),
])
def test(columnTitle, expected):
    assert expected == Solution().titleToNumber(columnTitle)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
