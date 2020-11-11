
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array, strs, with strings consisting of only 0s and 1s. Also two integers m and n.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are "10","0001","1","0".

Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

Constraints:
* 1 <= strs.length <= 600
* 1 <= strs[i].length <= 100
* strs[i] consists only of digits '0' and '1'.
* 1 <= m, n <= 100
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def count(s):
            ret = [0, 0]
            for c in s:
                ret[int(c)] += 1
            return ret

        cnt = [count(s) for s in strs]

        @lru_cache(None)
        def _rec(i, m, n):
            if i >= len(strs):
                return 0
            ret = _rec(i + 1, m, n)
            a, b = cnt[i]
            if m >= a and n >= b:
                ret = max(ret, 1 + _rec(i + 1, m - a, n - b))
            return ret

        return _rec(0, m, n)


@pytest.mark.parametrize('strs, m, n, expected', [
    (["10","0001","111001","1","0"], 5, 3, 4),
    (["10","0","1"], 1, 1, 2),
])
def test(strs, m, n, expected):
    assert expected == Solution().findMaxForm(strs, m, n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
