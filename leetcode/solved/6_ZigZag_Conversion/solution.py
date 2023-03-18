#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

Constraints:

	1 <= s.length <= 1000
	s consists of English letters (lower-case and upper-case), ',' and '.'.
	1 <= numRows <= 1000
"""
import itertools
import pytest
import sys


class Solution:
    def convert(self, s, numRows):
        """Jan 13, 2018 02:07
        n=numRows
        Δ=2n-2    1                           2n-1                         4n-3
        Δ=        2                     2n-2  2n                    4n-4   4n-2
        Δ=        3               2n-3        2n+1              4n-5       .
        Δ=        .           .               .               .            .
        Δ=        .       n+2                 .           3n               .
        Δ=        n-1 n+1                     3n-3    3n-1                 5n-5
        Δ=2n-2    n                           3n-2                         5n-4
        """
        if numRows == 1:
            return s
        stride = 2*numRows - 2
        ret = list(s[::stride])
        for i in range(1, numRows-1):
            j = i
            while j < len(s):
                ret.append(s[j])
                diag_position = j + stride - (2*i)
                if diag_position < len(s):
                    ret.append(s[diag_position])
                j += stride
        ret.extend(s[numRows-1::stride])
        return ''.join(ret)

    def convert(self, s: str, numRows: int) -> str:
        """Mar 18, 2023 14:50"""
        if numRows == 1:
            return s

        def gen(n, i):
            if i == 1 or i == n:
                yield from range(i-1, len(s), 2*(n-1))
            else:
                yield from itertools.chain(*itertools.zip_longest(
                    range(i-1, len(s), 2*(n-1)),
                    range(2*n-i-1, len(s), 2*(n-1))))

        return ''.join(s[i] for i in itertools.chain(*[gen(numRows, i) for i in range(1, numRows+1)]) if i is not None)


@pytest.mark.parametrize('args', [
    (("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR")),
    (("PAYPALISHIRING", 4, "PINALSIGYAHRPI")),
    (("A", 1, "A")),
])
def test(args):
    assert args[-1] == Solution().convert(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
