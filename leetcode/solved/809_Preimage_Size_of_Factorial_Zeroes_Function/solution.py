#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Let f(x) be the number of zeroes at the end of x!. Recall that x! = 1 * 2 * 3 * ... * x and by convention, 0! = 1.

	For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) = 2 because 11! = 39916800 has two zeroes at the end.

Given an integer k, return the number of non-negative integers x have the property that f(x) = k.

Example 1:

Input: k = 0
Output: 5
Explanation: 0!, 1!, 2!, 3!, and 4! end with k = 0 zeroes.

Example 2:

Input: k = 5
Output: 0
Explanation: There is no x such that x! ends in k = 5 zeroes.

Example 3:

Input: k = 3
Output: 5

Constraints:

	0 <= k <= 109
"""
import pytest
import sys
from collections import deque


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        """TLE
         5 10 15 20 25
         1  1  1  1  2
        30 35 40 45 50
         1  1  1  1  2
         ...
        80 85 90 95 100
         1  1  1  1  2
        105 110 115 120 125
          1   1   1   1   3
        130 135 140 145 150
          1   1   1   1   2
        """
        i = 0
        while True:
            acc = 0
            j = 5
            while i//j:
                acc += i//j
                j *= 5
            if acc>= k:
                break
            i += 5
        return 5 if acc == k else 0

    def preimageSizeFZF(self, k: int) -> int:
        """Apr 14, 2024 12:19"""
        def num_zeros(n):
            acc = 0
            j = 5
            while n//j:
                acc += n//j
                j *= 5
            return acc

        def bisearch(s, e, k):
            while s <= e:
                m = s + (e-s)//2
                cnt = num_zeros(m)
                if cnt <= k:
                    s = m+1
                else:
                    e = m-1
            return s-1

        i = bisearch(0, k*5, k)
        if i < 0:
            return 0
        return 5 if k == num_zeros(i) else 0


@pytest.mark.parametrize('args', [
    ((0, 5)),
    ((5, 0)),
    ((3, 5)),
    ((25, 5)),
    ((79, 0)),
    ((80502705, 0)),
])
def test(args):
    assert args[-1] == Solution().preimageSizeFZF(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
