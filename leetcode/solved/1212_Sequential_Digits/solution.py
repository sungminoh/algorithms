#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:
Input: low = 100, high = 300
Output: [123,234]
Example 2:
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

Constraints:

	10 <= low <= high <= 10^9
"""
import math
from typing import List
import pytest
import sys


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def gen(length):
            diff = 0
            n = 0
            for i in range(1, length+1):
                n *= 10
                n += i
                diff *= 10
                diff += 1
            yield n
            while n%10 != 9:
                n += diff
                yield n

        ll = int(math.log10(low))+1
        lh = int(math.log10(high))+1
        ret = []
        for l in range(ll, lh+1):
            for n in gen(l):
                if n < low:
                    continue
                if n > high:
                    return ret
                ret.append(n)
        return ret

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """Feb 05, 2024 22:02"""
        N = len(str(low))
        base = int(''.join(map(str, range(1, N+1))))
        delta = int('1'*N)
        i = 0
        ret = []
        while base <= high:
            i += 1
            if base >= low:
                ret.append(base)
            base += delta
            if i == 10-N:
                N += 1
                base = int(''.join(map(str, range(1, N+1))))
                delta = int('1'*N)
                i = 0
        return ret


@pytest.mark.parametrize('args', [
    ((100, 300, [123,234])),
    ((1000, 13000, [1234,2345,3456,4567,5678,6789,12345])),
])
def test(args):
    assert args[-1] == Solution().sequentialDigits(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
