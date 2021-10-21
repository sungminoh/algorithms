#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

	After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:

Input: prices = [1]
Output: 0

Constraints:

	1 <= prices.length <= 5000
	0 <= prices[i] <= 1000
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """12/27/2019 02:51"""
        if not prices:
            return 0

        def foo(i):
            if i == 0:
                return [-prices[0], 0, 0]
            # posses, can not buy, can buy
            sub = foo(i - 1)
            # keep or buy, sell, wait
            return [max(sub[0], sub[2] - prices[i]), sub[0] + prices[i], max(sub[1], sub[2])]

        return max(foo(len(prices) - 1))

    def maxProfit(self, prices: List[int]) -> int:
        """12/27/2019 02:53"""
        if not prices:
            return 0

        money = [-prices[0], 0, 0]
        for p in prices[1:]:
            money = [max(money[0], money[2] - p), money[0] + p, max(money[1], money[2])]
        return max(money)

    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i, position):
            """
            position: 0(no), 1(yes), 2(cooldown)
            """
            if i == len(prices):
                return 0
            if position == 0:
                return max(dp(i+1, 0), -prices[i] + dp(i+1, 1))
            elif position == 1:
                return max(dp(i+1, 1), prices[i] + dp(i+1, 2))
            else:
                return dp(i+1, 0)

        return dp(0, 0)

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [0, -prices[0], 0]
        for p in prices[1:]:
            dp = [
                max(dp[0], dp[2]),
                max(dp[0]-p, dp[1]),
                dp[1]+p,
            ]
        return max(dp)


@pytest.mark.parametrize('prices, expected', [
    ([1,2,3,0,2], 3),
    ([1], 0),
])
def test(prices, expected):
    assert expected == Solution().maxProfit(prices)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
