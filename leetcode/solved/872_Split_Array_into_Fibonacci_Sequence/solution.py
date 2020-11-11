#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

	0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
	F.length >= 3;
	and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.

Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]

Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]

Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.

Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.

Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.

Note:

	1 <= S.length <= 200
	S contains only digits.
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def dfs(i, cur):
            if i == len(S):
                if len(cur) >= 3:
                    return cur
                return None
            for j in range(i, len(S)):
                n = int(S[i:j+1])
                if n > 2**31 - 1:
                    return None
                if len(cur) < 2 or n == cur[-1]+cur[-2]:
                    ret = dfs(j+1, cur + [n])
                    if ret is not None:
                        return ret
                if S[i] == '0':
                    return None
            return None

        return dfs(0, [])

    def splitIntoFibonacci(self, S: str) -> List[int]:
        ret = []
        def dfs(i, cur):
            if i == len(S):
                if len(cur) >= 3:
                    ret.append(cur)
            for j in range(i, len(S)):
                n = int(S[i:j+1])
                if n > 2**31 - 1:
                    break
                if len(cur) < 2 or n == cur[-1]+cur[-2]:
                    dfs(j+1, cur + [n])
                if S[i] == '0':
                    break
        dfs(0, [])
        for l in ret:
            for i in range(2, len(l)):
                assert l[i] == l[i-1] + l[i-2]
        return ret[0] if ret else []


@pytest.mark.parametrize('S, expected', [
("123456579", [123,456,579]),
("11235813", [1,1,2,3,5,8,13]),
("112358130", []),
("0123", []),
("1101111", [110, 1, 111]),
("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511", [])
])
def test(S, expected):
    print()
    actual = Solution().splitIntoFibonacci(S)
    print(actual)
    assert len(actual) < 3 or ''.join(map(str, actual)) == S
    assert len(actual) < 3 or all(actual[i] == actual[i-1]+actual[i-2] for i in range(2, len(actual)))

    # assert expected == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
