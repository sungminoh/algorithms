#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

Constraints:

	n == gas.length == cost.length
	1 <= n <= 105
	0 <= gas[i], cost[i] <= 104
"""
from pathlib import Path
import json
import itertools
from typing import List
import pytest
import sys


class Solution:
    def canCompleteCircuit(self, gas, cost):
        """07/08/2018 06:25"""
        gain = [g - c for g, c in zip(gas, cost)]
        acc = [gain[0]]
        for i, g in enumerate(gain[1:]):
            acc.append(acc[i] + g)
        for i, g in enumerate(gain):
            acc.append(acc[len(gain)-1+i] + g)
        mins = []
        m = float('inf')
        for a in reversed(acc):
            if a < m:
                mins.append(a)
                m = a
            else:
                mins.append(m)
        mins.reverse()
        for i, (m, a, g) in enumerate(zip(mins, acc, gain)):
            if m - a + g >= 0:
                return i
        return -1

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """Feb 01, 2022 10:30"""
        n = len(gas)

        min_val = float('inf')
        min_idx = 0
        for i, v in enumerate(itertools.accumulate(g - c for g, c in zip(gas, cost))):
            if v <= min_val:
                min_val = v
                min_idx = i

        if min_val >= 0:
            return 0

        acc = 0
        for i in range(min_idx+1, min_idx+1+n):
            acc += (gas[i%n] - cost[i%n])
            if acc < 0:
                return -1

        return min_idx+1

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """Mar 05, 2023 12:03"""
        acc = 0
        min_acc = float('inf')
        min_i = -1
        for i, (g, c) in enumerate(zip(gas, cost)):
            acc += g-c
            if acc < min_acc:
                min_acc = acc
                min_i = i
        return (min_i+1) % len(gas) if acc >= 0 else -1


@pytest.mark.parametrize('args', [
    (([1,2,3,4,5], [3,4,5,1,2], 3)),
    (([2,3,4], [3,4,3], -1)),
    (([3,3,4], [3,4,4], -1)),
    (([1000, 1002, 1000, 999], [1000, 1001, 1000, 999], 0)),
    ((*json.load(open(Path(__file__).parent/'testcase.json')), 0)),
])
def test(args):
    assert args[-1] == Solution().canCompleteCircuit(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
