#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

Example 1:

Input: start = "X", end = "L"
Output: false
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

Example 2:

Input: start = "LLR", end = "RRL"
Output: false

Example 3:

Input: start = "XLLR", end = "LXLX"
Output: false

Constraints:

	1 <= start.length <= 104
	start.length == end.length
	Both start and end will only consist of characters in 'L', 'R', and 'X'.
"""
import sys
import pytest


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        s = [(i, c) for i, c in enumerate(start) if c != 'X']
        e = [(i, c) for i, c in enumerate(end) if c != 'X']
        return len(s) == len(e) \
            and all(c1 == c2 \
                    and ((i1 >= i2 and c1 == 'L') \
                         or (i1 <= i2 and c1 == 'R')) \
                    for (i1, c1), (i2, c2) in zip(s, e))

    def _canTransform(self, start: str, end: str) -> bool:
        chars = list(start)
        def dfs(i):
            if i == len(start):
                return ''.join(chars) == end
            ret = []
            if ''.join(chars[i:i+2]) in {'XL', 'LX', 'XR', 'RX'}:
                chars[i], chars[i+1] = chars[i+1], chars[i]
                ret.append(dfs(i+1))
                chars[i], chars[i+1] = chars[i+1], chars[i]
            ret.append(dfs(i+1))
            return any(ret)

        return dfs(0)



@pytest.mark.parametrize('start, end, expected', [
    ('RXXLRXRXL', 'XRLXXRRLX', True),
    ('LLR', 'RRL', False),
    ('XLLR', 'LXLX', False),
    ("LXXLXRLXXL", "XLLXRXLXLX", False),
    ("XXXLXXXXXX", "XXXLXXXXXX", True)
])
def test(start, end, expected):
    assert expected == Solution().canTransform(start, end)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
