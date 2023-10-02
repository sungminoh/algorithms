from functools import lru_cache
from itertools import accumulate
from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger.

Example 2:

Input: piles = [1,2,3,4,5,100]
Output: 104

Constraints:

	1 <= piles.length <= 100
	1 <= piles[i] <= 104
"""
import pytest
import sys


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        """Sep 23, 2023 13:35"""
        reverse_cumsum = list(reversed(list(accumulate(reversed(piles))))) + [0]

        @lru_cache(None)
        def dp(i, m):
            ret = 0
            acc = 0
            for x in range(2*m):
                if i+x >= len(piles):
                    break
                acc += piles[i+x]
                ret = max(ret, acc + reverse_cumsum[i+x+1] - dp(i+x+1, max(m, x+1)))
            return ret

        return dp(0, 1)


@pytest.mark.parametrize('args', [
    (([2,7,9,4,4], 10)),
    (([1,2,3,4,5,100], 104)),
])
def test(args):
    assert args[-1] == Solution().stoneGameII(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
