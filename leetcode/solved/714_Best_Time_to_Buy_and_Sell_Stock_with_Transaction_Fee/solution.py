#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.
You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.  You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)
Return the maximum profit you can make.

Example 1:

Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1Selling at prices[3] = 8Buying at prices[4] = 4Selling at prices[5] = 9The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Note:
0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        cash = 0
        hold = -prices[0]
        for p in prices:
            cash = max(cash, hold + p - fee)
            hold = max(hold, cash - p)
        return max(cash, hold)

    def _maxProfit(self, prices: List[int], fee: int) -> int:
        def date_state(i, s):
            if i == len(prices)-1:
                return max(0, prices[i] - fee) if s > 0 else 0
            return max(date_state(i+1, s), s*prices[i] - ((s+1)//2) * fee + date_state(i+1, -1*s))

        return date_state(0, -1)


@pytest.mark.parametrize('prices, fee, expected', [
    ([1, 3, 2, 8, 4, 9], 2, 8),
])
def test(prices, fee, expected):
    assert expected == Solution().maxProfit(prices, fee)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
