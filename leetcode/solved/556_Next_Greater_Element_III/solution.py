#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21

Example 2:

Input: 21
Output: -1
"""
import sys
import pytest


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        rest = []
        while n:
            d = n % 10
            n //= 10
            rest.append(d)
            if n > 0 and n % 10 < d:
                rest.append(n % 10)
                n //= 10
                break
        else:
            return -1
        d = min(c for c in rest if c > rest[-1])
        rest.remove(d)
        ret = n * 10 + d
        for c in sorted(rest):
            ret *= 10
            ret += c
        return ret if ret < pow(2, 31) else -1


@pytest.mark.parametrize('n, expected', [
    (12, 21),
    (21, -1),
    (12345, 12354),
    (12443322, 13222344),
    (1999999999, -1)
])
def test(n, expected):
    assert expected == Solution().nextGreaterElement(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
