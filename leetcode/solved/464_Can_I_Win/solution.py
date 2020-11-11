#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
"""
import sys
from functools import lru_cache
import pytest


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        used = 1 << maxChoosableInteger

        def is_used(used, n):
            return (used >> (maxChoosableInteger - n)) % 2 > 0

        def toggle_use(used, n):
            return used ^ (1 << (maxChoosableInteger - n))

        @lru_cache(None)
        def dfs(used, total):
            m = 0
            s = 0
            for n in range(1, maxChoosableInteger + 1):
                if not is_used(used, n) and n > m:
                    m = n
                    s += n
            if m >= total:
                return True
            if s < total:
                return False
            for n in range(1, maxChoosableInteger + 1):
                if is_used(used, n):
                    continue
                used = toggle_use(used, n)
                for m in range(1, maxChoosableInteger + 1):
                    if is_used(used, m):
                        continue
                    used = toggle_use(used, m)
                    remain = total - n - m
                    if remain <= 0 or not dfs(used, total - n - m):
                        used = toggle_use(used, m)
                        break
                    used = toggle_use(used, m)
                else:
                    return True
                used = toggle_use(used, n)
            return False

        return dfs(used, desiredTotal)


@pytest.mark.parametrize('maxChoosableInteger, desiredTotal, expected', [
    (10, 11, False),
    (10, 40, False),
    (4, 6, True),
    (18, 79, True),
])
def test(maxChoosableInteger, desiredTotal, expected):
    print()
    assert expected == Solution().canIWin(maxChoosableInteger, desiredTotal)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
