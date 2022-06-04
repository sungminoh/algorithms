#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

Constraints:

	1 <= coins.length <= 12
	1 <= coins[i] <= 231 - 1
	0 <= amount <= 104
"""
from functools import lru_cache
import sys
from typing import List
import pytest


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for x in range(min(coins or [0]), amount + 1):
            for c in coins:
                if 0 <= x - c:
                    dp[x] = min(dp[x], 1 + dp[x - c])
        ret = dp[amount]
        return ret if ret != float('inf') else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = {c: 1 for c in coins}
        for x in range(1, amount + 1):
            for c in coins:
                dp[x] = min(dp.get(x, float('inf')), 1 + dp.get(x - c, float('inf')))
        ret = dp.get(amount, float('inf'))
        return ret if ret != float('inf') else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
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
                # accelerate
                if c <= amount < c * (m - cnt):
                    sub = coin_change(amount - c, cnt + 1)
                    m = min(m, sub)
            return m

        coins = sorted(coins, reverse=True)
        ret = coin_change(amount, 0)
        return ret if ret != float('inf') else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def coin_change(i, amount, prev_count):
            m = float('inf')
            if amount % coins[i] == 0:
                return amount // coins[i]
            # accelerate
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

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        @lru_cache(None)
        def dfs(i, amount):
            if amount == 0:
                return 0
            if i >= len(coins):
                return float('inf')
            if coins[i] > amount:
                return dfs(i+1, amount)
            ret = float('inf')
            for cnt in range(amount//coins[i], -1, -1):
                s = cnt*coins[i]
                remain = amount-s
                # find next coin
                j = i+1
                while j < len(coins):
                    if coins[j] <= remain:
                        break
                    j += 1
                # discard no hope cases
                if j < len(coins) and remain/coins[j] > ret-cnt:
                    continue
                sub = dfs(j, remain)
                ret = min(ret, cnt+sub)
            return ret

        ret = dfs(0, amount)
        return ret if ret < float('inf') else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        if not coins:
            return 0 if amount == 0 else -1

        # handle edge cases
        def gcd(a, b):
            if a < b:
                return gcd(b, a)
            if a%b == 0:
                return b
            return gcd(a%b, b)

        d = coins[0]
        for c in coins[1:]:
            d = gcd(d, c)
            if d == 1:
                break
        if d > 0 and amount%d > 0:
            return -1

        # simplify
        coins = [c//d for c in coins]
        amount = amount//d

        ret = float('inf')
        @lru_cache(None)
        def dfs(amount, cnt):
            nonlocal ret
            if amount == 0:
                ret = cnt
                return
            if amount < 0:
                return
            for coin in coins:
                # Critical to accelerate
                if coin > amount or coin*(ret-cnt) < amount:
                    continue
                # for c in range(amount//coin, 0, -1):
                dfs(amount-coin, cnt+1)

        dfs(amount, 0)
        return ret if ret < float('inf') else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Bitwise BFS. from discussion
        """
        step, seen = 0, 1 << amount
        while seen & 1 != 1:
            cur = seen
            for coin in coins:
                cur |= seen >> coin
            if cur == seen:
                return -1
            step, seen = step + 1, cur
        return step


@pytest.mark.parametrize('coins, amount, expected', [
    ([1,2,5], 11, 3),
    ([2], 3, -1),
    ([1], 0, 0),
    ([3,7,405,436], 8839, 25),
    ([2], 2, 1),
    ([], 2, -1),
    ([], 0, 0),
    ([80,149,71,111], 8683, 61),
    ([205,37,253,463,441,129,156,429,101,423,311], 6653, 15),
    ([1,2147483647], 2, 2),
    ([139,442,147,461,244,225,28,378,371], 9914, 22),
    ([357,239,73,52], 9832, 35),
    ([2,4,6,8,10,12,14,16,18,20,22,24], 9999, -1),
    ([1], 10000, 10000),
])
def test(coins, amount, expected):
    assert expected == Solution().coinChange(coins, amount)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
