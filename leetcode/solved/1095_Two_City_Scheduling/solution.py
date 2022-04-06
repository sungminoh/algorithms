#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

Example 1:

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

Example 2:

Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859

Example 3:

Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
Output: 3086

Constraints:

	2 * n == costs.length
	2 <= costs.length <= 100
	costs.length is even.
	1 <= aCosti, bCosti <= 1000
"""
import sys
from typing import List
import pytest


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        Sort by gap in descending order
        and assign each with the largest gap first
        """
        costs.sort(key=lambda x: abs(x[0]-x[1]), reverse=True)
        ab_cst = [0, 0]
        ab_cnt = [0, 0]
        for i, (a, b) in enumerate(costs):
            if abs(ab_cnt[0] - ab_cnt[1]) == len(costs)-i:
                if ab_cnt[0] < ab_cnt[1]:
                    ab_cnt[0] += 1
                    ab_cst[0] += a
                else:
                    ab_cnt[1] += 1
                    ab_cst[1] += b
            else:
                if a < b:
                    ab_cnt[0] += 1
                    ab_cst[0] += a
                else:
                    ab_cnt[1] += 1
                    ab_cst[1] += b
        return sum(ab_cst)

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        Simply sort by cost_a - cost_b
        and assign early half to go a and the others to B
        """
        costs.sort(key=lambda x: x[0]-x[1])
        ret = 0
        for i, (a, b) in enumerate(costs):
            if i < len(costs)//2:
                ret += a
            else:
                ret += b
        return ret



@pytest.mark.parametrize('costs, expected', [
    ([[10,20],[30,200],[400,50],[30,20]], 110),
    ([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]], 1859),
    ([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]], 3086),
])
def test(costs, expected):
    assert expected == Solution().twoCitySchedCost(costs)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
