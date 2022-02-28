#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Constraints:

	1 <= k <= num.length <= 105
	num consists of only digits.
	num does not have any leading zeros except for the zero itself.
"""
import sys
import pytest


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """04/22/2020 21:51"""
        for _ in range(k):
            idx = -1
            for i in range(len(num) - 1):
                if num[i] > num[i+1]:
                    idx = i
                    break
            else:
                idx = len(num) - 1
            num = num[0:idx] + num[idx+1:]
        idx = 0
        while idx < len(num) and num[idx] == '0':
            idx += 1
        return num[idx:] or '0'

    def removeKdigits(self, num: str, k: int) -> str:
        """04/22/2020 21:59"""
        stack = []
        for n in num:
            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        if k > 0:
            stack = stack[:-k]
        return ''.join(stack).lstrip('0') or '0'

    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and stack[-1] > n and k:
                stack.pop()
                k -= 1
            stack.append(n)
        while stack and k:
            stack.pop()
            k -= 1
        return ''.join(stack).lstrip('0') or '0'


@pytest.mark.parametrize('num, k, expected', [
    ("1432219", 3, "1219"),
    ("10200", 1, "200"),
    ("11200", 1, "1100"),
    ("10", 2, "0"),
    ('9', 1, '0')
    ("1234567890", 9, '0')
])
def test(num, k, expected):
    assert expected == Solution().removeKdigits(num, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
