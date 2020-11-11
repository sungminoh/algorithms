#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
from typing import List
import random


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1]:
                s += prices[i+1] - prices[i]
        return s


def gen_case():
    size = random.randint(0, 10)
    ret = []
    for _ in range(size):
        ret.append(random.randint(1, 1.5 * size))
    return ret, None


if __name__ == '__main__':
    cases = [
        ([7,1,5,3,6,4], 7),
        ([1,2,3,4,5], 4),
        ([7,6,4,3,1], 0)
    ]
    result = []
    for case, expected in cases:
        print(case, expected)
        actual = Solution().maxProfit(case)
        ans = expected == actual
        result.append(ans)
        print(f'{ans}\texpected: {expected}\tactual: {actual}')
    if not all(result):
        raise Exception('Wrong')
