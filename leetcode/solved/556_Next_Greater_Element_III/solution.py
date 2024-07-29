#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

Example 1:
Input: n = 12
Output: 21
Example 2:
Input: n = 21
Output: -1

Constraints:

	1 <= n <= 231 - 1
"""
import bisect
import pytest
import sys


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """Jun 07, 2020 23:42"""
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

    def nextGreaterElement(self, n: int) -> int:
        """Jul 03, 2024 09:42"""
        def bisect(arr, x, lo=None, hi=None):
            lo = lo or 0
            hi = hi or len(arr)-1
            while lo <= hi:
                mi = lo + (hi-lo)//2
                if arr[mi] > x:
                    lo = mi+1
                else:
                    hi = mi-1
            return hi

        s = list(map(int, str(n)))
        i = len(s)-1
        while i > 0:
            if s[i] > s[i-1]:
                break
            i -= 1
        if i == 0:
            return -1
        j = bisect(s, s[i-1], lo=i)
        if j < len(s):
            s[j], s[i] = s[i], s[j]
        ret = int(''.join(map(str, [*s[:i-1], s[i], *sorted([s[i-1], *s[i+1:]])])))
        return -1 if ret >= 2**31 else ret


@pytest.mark.parametrize('args', [
    ((12, 21)),
    ((21, -1)),
    ((12345, 12354)),
    ((230241, 230412)),
    ((2147483486, -1)),
    ((2147483476, 2147483647)),
    ((12443322, 13222344)),
    ((1999999999, -1)),
])
def test(args):
    assert args[-1] == Solution().nextGreaterElement(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
