#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""
from typing import List
from functools import lru_cache


class Solution:
    def _coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for x in range(min(coins or [0]), amount + 1):
            for c in coins:
                if 0 <= x - c:
                    dp[x] = min(dp[x], 1 + dp[x - c])
        ret = dp[amount]
        return ret if ret != float('inf') else -1

    def ___coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = {c: 1 for c in coins}
        for x in range(1, amount + 1):
            for c in coins:
                dp[x] = min(dp.get(x, float('inf')), 1 + dp.get(x - c, float('inf')))
        ret = dp.get(amount, float('inf'))
        print(dp)
        return ret if ret != float('inf') else -1

    def __coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def coin_change(amount):
            if amount < 0:
                return float('inf')
            if amount == 0:
                return 0
            return min([1 + coin_change(amount - c) for c in coins] or [float('inf')])

        ret = coin_change(amount)
        return ret if ret != float('inf') else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        m = float('inf')

        @lru_cache(None)
        def coin_change(amount, cnt):
            nonlocal m
            if amount < 0:
                return m
            if amount == 0:
                return min(m, cnt)
            for c in coins:
                if c <= amount < c * (m - cnt):
                    sub = coin_change(amount - c, cnt + 1)
                    m = min(m, sub)
            return m

        coins = sorted(coins, reverse=True)
        ret = coin_change(amount, 0)
        return ret if ret != float('inf') else -1

    def coinChange2(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def coin_change(i, amount, prev_count):
            m = float('inf')
            if amount % coins[i] == 0:
                return amount // coins[i]
            if amount // coins[i] + 1 >= prev_count:
                return m
            if i == len(coins) - 1:
                return m
            for cnt, sub_amount in reversed(list(enumerate(range(0, amount + 1, coins[i])))):
                m = min(m, cnt + coin_change(i + 1, amount - sub_amount, m - cnt))
            return m

        coins = sorted(coins, reverse=True)
        ret = coin_change(0, amount, float('inf'))
        return ret if ret != float('inf') else -1


if __name__ == '__main__':
    cases = [
        (([1,2,5],11), 3),
        (([2], 3), -1),
        (([2], 2), 1),
        # (([], 2), -1),
        # (([], 0), 0),
        (([3,7,405,436], 8839), 25),
        (([80,149,71,111], 8683), 61),
        (([205,37,253,463,441,129,156,429,101,423,311], 6653), 15),
        (([1,2147483647], 2), 2),
        (([139,442,147,461,244,225,28,378,371], 9914), 22),
        (([357,239,73,52], 9832), 35)
    ]
    for case, expected in cases:
        actual = Solution().coinChange(*case)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
