#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:

	1 <= prices.length <= 105
	0 <= prices[i] <= 104
"""
import sys
from typing import List
import pytest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        mn = float('inf')
        for p in prices:
            ret = max(ret, p-mn)
            mn = min(mn, p)
        return ret


@pytest.mark.parametrize('prices, expected', [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0),
])
def test(prices, expected):
    assert expected == Solution().maxProfit(prices)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
