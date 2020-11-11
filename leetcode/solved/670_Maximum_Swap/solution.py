#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:

Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:

Input: 9973
Output: 9973
Explanation: No swap.

Note:

The given number is in the range [0, 108]
"""
import sys
import pytest


class Solution:
    def maximumSwap(self, num: int) -> int:
        ns =list(str(num))
        mxir = [-1]
        for i in range(len(ns)-2, -1, -1):
            if ns[i] > ns[mxir[-1]]:
                mxir.append(i)
            else:
                mxir.append(mxir[-1])
        mxir.reverse()
        for i, j in enumerate(mxir):
            if ns[i] < ns[j]:
                ns[i], ns[j] = ns[j], ns[i]
                break
        return int(''.join(ns))

@pytest.mark.parametrize('num, expected', [
    (2736, 7236),
    (9973, 9973),
    (98368, 98863)
])
def test(num, expected):
    assert expected == Solution().maximumSwap(num)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
