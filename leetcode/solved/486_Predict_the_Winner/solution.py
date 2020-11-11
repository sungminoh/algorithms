
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:

Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2. If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. Hence, player 1 will never be the winner and you need to return False.

Example 2:

Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

Note:

1
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(i, j):
            if i + 1 == j:
                return nums[i] - nums[j] if nums[i] > nums[j] else nums[j] - nums[i]
            elif i >= j:
                return 0
            # case 1
            return max(min([nums[i] - nums[i + 1] + dfs(i + 2, j),
                            nums[i] - nums[j] + dfs(i + 1, j - 1)]),
                       min([nums[j] - nums[j - 1] + dfs(i, j - 2),
                            nums[j] - nums[i] + dfs(i + 1, j - 1)]))
        i, j = 0, len(nums) - 1
        if i > j:
            return False
        elif i == j:
            return True
        elif i + 1 == j:
            return True
        return all(x >= 0 for x in [nums[0] - nums[1] + dfs(i + 2, j), nums[0] - nums[j] + dfs(i + 1, j - 1)]) \
            or all(x >= 0 for x in [nums[j] - nums[j - 1] + dfs(i, j - 2), nums[j] - nums[0] + dfs(i + 1, j - 1)])


@pytest.mark.parametrize('nums, expected', [
    ([1, 5, 2], False),
    ([1, 5, 233, 7], True),
    ([1, 1], True),
    ([1,1,1,1,1,1,1,1], True),
    ([1,1,567,1,1,99], True)
])
def test(nums, expected):
    assert expected == Solution().PredictTheWinner(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
