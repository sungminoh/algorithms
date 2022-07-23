#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.

Example 1:

Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32

Example 2:

Input: n = "82734"
Output: 8

Example 3:

Input: n = "27346209830709182346"
Output: 9

Constraints:

	1 <= n.length <= 105
	n consists of only digits.
	n does not contain any leading zeros and represents a positive integer.
"""
import sys
import pytest


class Solution:
    def minPartitions(self, n: str) -> int:
        """06/09/2021 05:05"""
        return max(int(x) for x in n)

    def minPartitions(self, n: str) -> int:
        """07/22/2022 21:51"""
        return max(map(int, n))


@pytest.mark.parametrize('n, expected', [
    ("32", 3),
    ("82734", 8),
    ("27346209830709182346", 9),
])
def test(n, expected):
    assert expected == Solution().minPartitions(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
