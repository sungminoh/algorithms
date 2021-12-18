#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:

	position[i] + 2 or position[i] - 2 with cost = 0.
	position[i] + 1 or position[i] - 1 with cost = 1.

Return the minimum cost needed to move all the chips to the same position.

Example 1:

Input: position = [1,2,3]
Output: 1
Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.

Example 2:

Input: position = [2,2,2,3,3]
Output: 2
Explanation: We can move the two chips at position  3 to position 2. Each move has cost = 1. The total cost = 2.

Example 3:

Input: position = [1,1000000000]
Output: 1

Constraints:

	1 <= position.length <= 100
	1 <= position[i] <= 10^9
"""
import sys
from typing import List
import pytest


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        s = [0, 0]
        for p in position:
            s[p%2] += 1
        return min(s)


@pytest.mark.parametrize('positions, expected', [
    ([1,2,3], 1),
    ([2,2,2,3,3], 2),
    ([1,1000000000], 1),
])
def test(positions, expected):
    assert expected == Solution().minCostToMoveChips(positions)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
