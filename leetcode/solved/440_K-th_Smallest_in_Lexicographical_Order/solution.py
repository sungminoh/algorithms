#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 ≤ k ≤ n ≤ 109.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
"""
import sys
import pytest


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def get_steps(n, c):
            ret = 0
            n1, n2 = c, c+1
            while n1 <= n:
                if n2 <= n:
                    ret += n2 - n1
                else:
                    ret += n - n1 + 1
                n1 *= 10
                n2 *= 10
            return ret

        c = 1
        while k > 1:
            s = get_steps(n, c)
            if s < k:
                c += 1
                k -= s
            else:
                c *= 10
                k -= 1;
        return c


@pytest.mark.parametrize('n, k, expected', [
    (13, 2, 10),
    (2, 2, 2),
    (10, 3, 2),  # 1 10 2 3 4 5 6 7 8 9
    (100, 10, 17)  # 1 10 100 11 12 13 14 15 16 17 ...
])
def test(n, k, expected):
    assert expected == Solution().findKthNumber(n, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
