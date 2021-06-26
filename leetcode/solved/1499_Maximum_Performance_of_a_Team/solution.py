#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.

Example 1:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation:
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.

Example 2:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.

Example 3:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72

Constraints:

	1 <= k <= n <= 105
	speed.length == n
	efficiency.length == n
	1 <= speed[i] <= 105
	1 <= efficiency[i] <= 108
"""
from pathlib import Path
import json
import sys
from heapq import heappop
from heapq import heappush
from typing import List
import pytest


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        """
        Time complexity: O(nlogn)  # sort
        Space complexity: O(k)  # heap
        """
        ret = 0
        acc = 0
        h = []
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            heappush(h, s)
            acc += s
            if len(h) > k:
                acc -= heappop(h)
            ret = max(ret, acc*e)
        return ret % (int(1e9)+7)


@pytest.mark.parametrize('n, speed, efficiency, k, expected', [
    (6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2, 60),
    (6, [2,10,3,1,5,8], [5,4,3,9,7,2], 3, 68),
    (6, [2,10,3,1,5,8], [5,4,3,9,7,2], 4, 72),
    (*json.load(open(Path(__file__).parent/'testcase.json')),301574164),
])
def test(n, speed, efficiency, k, expected):
    assert expected == Solution().maxPerformance(n, speed, efficiency, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
