#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

Input: candidates = [2], target = 1
Output: []

Constraints:

	1 <= candidates.length <= 30
	1 <= candidates[i] <= 200
	All elements of candidates are distinct.
	1 <= target <= 500
"""
import sys
from typing import List
import pytest


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        def dfs(i, remain, cur):
            if remain == 0:
                return ret.append(cur)
            if i == len(candidates):
                return
            for j in range(int(remain/candidates[i])+1):
                dfs(i+1, remain - (j*candidates[i]), cur + [candidates[i]]*j)
        dfs(0, target, [])
        return ret


@pytest.mark.parametrize('candidates, target, expected', [
    ([2,3,6,7], 7, [[2,2,3],[7]]),
    ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
    ([2], 1, []),
])
def test(candidates, target, expected):
    assert sorted(expected) == sorted(Solution().combinationSum(candidates, target))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
