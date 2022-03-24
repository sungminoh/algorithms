#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.

Example 2:

Input: n = 2
Output: 6
Explanation: All possible orders:
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.

Example 3:

Input: n = 3
Output: 90

Constraints:

	1 <= n <= 500
"""
import sys
import pytest


class Solution:
    def countOrders(self, n: int) -> int:
        """top-down recursion"""
        if n == 1:
            return 1
        MOD = int(1e9+7)
        pos = 2*n-1
        return (self.countOrders(n-1) * ((pos + 1) * pos)//2) % MOD

    def countOrders(self, n: int) -> int:
        """bottom-up"""
        MOD = int(1e9+7)
        ret = 1
        for i in range(1, n):
            ret *= (2*i+2)*(2*i+1)//2
            ret %= MOD
        return ret


@pytest.mark.parametrize('n, expected', [
    (1, 1),
    (2, 6),
    (3, 90),
])
def test(n, expected):
    assert expected == Solution().countOrders(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
