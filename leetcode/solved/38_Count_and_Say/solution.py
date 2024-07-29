#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

	countAndSay(1) = "1"
	countAndSay(n) is the run-length encoding of countAndSay(n - 1).

Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.

Example 1:

Input: n = 4

Output: "1211"

Explanation:

countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"

Example 2:

Input: n = 1

Output: "1"

Explanation:

This is the base case.

Constraints:

	1 <= n <= 30

Follow up: Could you solve it iteratively?
"""
import math
import pytest
import sys


class Solution:
    def countAndSay(self, n: int) -> str:
        """11/05/2022 18:09"""
        if n == 1:
            return '1'
        sub = self.countAndSay(n-1)
        ret = ''
        char = sub[0]
        cnt = 1
        for i in range(1, len(sub)):
            if sub[i] != char:
                ret += str(cnt) + char
                char = sub[i]
                cnt = 0
            cnt += 1
        ret += str(cnt) + char
        return ret

    def countAndSay(self, n: int) -> str:
        """Jul 02, 2024 21:53"""
        ret = '1'
        for _ in range(n-1):
            cnt = 0
            tmp = []
            for i, c in enumerate(ret):
                cnt += 1
                if i < len(ret)-1 and ret[i+1] == c:
                    continue
                else:
                    tmp.append(f'{cnt}{c}')
                    cnt = 0
            ret = ''.join(tmp)
        return ret


@pytest.mark.parametrize('args', [
    ((4, "1211")),
    ((1, "1")),
    ((30, "")),
])
def test(args):
    assert args[-1] == Solution().countAndSay(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
