#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.

Example 1:

Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4
Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.

Example 2:

Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
Output: 4

Example 3:

Input: m = 3, n = 3, ops = []
Output: 9

Constraints:

	1 <= m, n <= 4 * 104
	0 <= ops.length <= 104
	ops[i].length == 2
	1 <= ai <= m
	1 <= bi <= n
"""
import sys
from typing import List
import pytest


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        ma = m
        mb = n
        for a, b in ops:
            ma = min(ma, a)
            mb = min(mb, b)
        return ma*mb


@pytest.mark.parametrize('m, n, ops, expected', [
    (3, 3, [[2,2],[3,3]], 4),
    (3, 3, [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]], 4),
    (3, 3, [], 9),
])
def test(m, n, ops, expected):
    assert expected == Solution().maxCount(m, n, ops)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
