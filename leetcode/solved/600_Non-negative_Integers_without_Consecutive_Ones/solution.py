#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a positive integer n, find the number of non-negative integers less than or equal to n, whose binary representations do NOT contain consecutive ones.

Example 1:

Input: 5
Output: 5
Explanation:
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.

Note:
1 <= n <= 109
"""
from functools import lru_cache
from traitlets.config.sphinxdoc import reverse_aliases
import sys
import pytest


class Solution:
    def findIntegers(self, num: int) -> int:
        """
        Time complexity: O(logn)
        Space complexity: O(logn)
        """
        b = bin(num)[2:]

        @lru_cache(None)
        def rec(i, previous, relaxed: bool):
            if i == len(b):
                return 1
            cnt = rec(i+1, 0, True if relaxed or b[i] == '1' else False)
            if (relaxed or b[i] == '1') and previous == 0:
                cnt += rec(i+1, 1, relaxed)
            return cnt

        return rec(0, 0, False)


@pytest.mark.parametrize('num, expected', [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 5),
    (7, 5),
    (8, 6),
])
def test(num, expected):
    assert expected == Solution().findIntegers(num)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
