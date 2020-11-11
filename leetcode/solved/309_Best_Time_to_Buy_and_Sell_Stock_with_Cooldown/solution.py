#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # posses, can not buy, can buy
        money = [-prices[0], 0, 0]
        for p in prices[1:]:
            # keep or buy, sell, wait
            money = [max(money[0], money[2] - p), money[0] + p, max(money[1], money[2])]
        return max(money)


if __name__ == '__main__':
    cases = [
        ([1,2,3,0,2], 3),
        ([1,2,4], 3)
    ]
    for case, expected in cases:
        actual = Solution().maxProfit(case)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
