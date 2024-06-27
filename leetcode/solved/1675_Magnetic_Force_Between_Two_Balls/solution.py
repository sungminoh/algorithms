#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

Example 1:

Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.

Example 2:

Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.

Constraints:

	n == position.length
	2 <= n <= 105
	1 <= position[i] <= 109
	All integers in position are distinct.
	2 <= m <= position.length
"""
from pathlib import Path
import json
from functools import lru_cache
from typing import List
import pytest
import sys


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        """RecursionError: maximum recursion depth exceeded"""
        position.sort()

        @lru_cache(None)
        def dfs(i, balls):
            if balls == 0:
                return float('inf')
            if i+balls >= len(position):
                return 0
            ret = dfs(i+1, balls)
            for j in range(i+1, len(position)-balls+1):
                ret = max(ret, min(position[j]-position[i], dfs(j, balls-1)))
            return ret

        return max(dfs(i, m-1) for i in range(len(position)))

    def maxDistance(self, position: List[int], m: int) -> int:
        """Jun 26, 2024 23:25"""
        position.sort()

        def doable(distance):
            cnt = 1
            j = 0
            for i in range(1, len(position)):
                if position[i]-position[j] >= distance:
                    j = i
                    cnt += 1
            return cnt >= m

        def bisearch(s, e):
            while s <= e:
                p = s + (e-s)//2
                if doable(p):
                    s = p+1
                else:
                    e = p-1
            return s-1

        return bisearch(1, position[-1] - position[0])


@pytest.mark.parametrize('args', [
    (([1,2,3,4,7], 3, 3)),
    (([5,4,3,2,1,1000000000], 2, 999999999)),
    ((json.load(open(Path(__file__).parent/'testcase.json')), 23, 44)),
])
def test(args):
    assert args[-1] == Solution().maxDistance(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
