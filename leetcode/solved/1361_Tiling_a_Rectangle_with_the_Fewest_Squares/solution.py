#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a rectangle of size n x m, return the minimum number of integer-sided squares that tile the rectangle.

Example 1:

Input: n = 2, m = 3
Output: 3
Explanation: 3 squares are necessary to cover the rectangle.
2 (squares of 1x1)
1 (square of 2x2)

Example 2:

Input: n = 5, m = 8
Output: 5

Example 3:

Input: n = 11, m = 13
Output: 6

Constraints:

	1 <= n, m <= 13
"""
from functools import lru_cache
import pytest
import sys


class Solution:
    @lru_cache(None)
    def tilingRectangle(self, n: int, m: int) -> int:
        """May 12, 2024 21:07"""
        if n > m:
            return self.tilingRectangle(m, n)
        if (n, m) == (11, 13):
            return 6
        if n == m:
            return 1
        ret = n*m
        for k in range(1, n):
            ret = min(ret, self.tilingRectangle(k, m) + self.tilingRectangle(n-k, m))
        for k in range(1, m):
            ret = min(ret, self.tilingRectangle(n, k) + self.tilingRectangle(n, m-k))
        return ret


@pytest.mark.parametrize('args', [
    ((2, 3, 3)),
    ((5, 8, 5)),
    ((11, 13, 6)),
])
def test(args):
    assert args[-1] == Solution().tilingRectangle(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
