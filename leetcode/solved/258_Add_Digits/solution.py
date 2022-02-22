#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.

Example 2:

Input: num = 0
Output: 0

Constraints:

	0 <= num <= 231 - 1

Follow up: Could you do it without any loop/recursion in O(1) runtime?
"""
import sys
import pytest


class Solution:
    def addDigits(self, num: int) -> int:
        def reduce(num):
            ret = 0
            while num:
                ret += num%10
                num //= 10
            return ret

        ret = reduce(num)
        while ret//10:
            ret = reduce(ret)

        return ret


@pytest.mark.parametrize('num, expected', [
    (38, 2),
    (0, 0),
])
def test(num, expected):
    assert expected == Solution().addDigits(num)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
