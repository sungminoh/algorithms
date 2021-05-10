#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]

Constraints:

	1 <= candidates.length <= 100
	1 <= candidates[i] <= 50
	1 <= target <= 30
"""
from functools import lru_cache
import sys
from collections import Counter
from typing import Tuple
from typing import Set
from typing import List
import pytest


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        DP using recursion. Use set to deduplicate.
        Time complexity: O(n*m)
        Space complexity: O(n*m)
        """
        candidates = list(sorted(candidates))

        @lru_cache(None)
        def comb(i, t) -> Set[Tuple[int]]:
            if t == 0:
                return set([tuple()])
            if i == len(candidates) or candidates[i] > t:
                return set()
            ret = set()
            for x in comb(i+1, t-candidates[i]):
                ret.add(tuple([candidates[i], *x]))
            ret.update(comb(i+1, t))
            return ret

        return list(list(x) for x in comb(0, target))

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        DFS without nonlocal variable.
        Copy a current path every subroutine call.
        Time complexity: O(n*m)
        Space complexity: O(n)  # callstack exclude the return
        """
        candidates = list(sorted(candidates))

        def dfs(i, t) -> List[List[int]]:
            if t == 0:
                return [[]]
            if i == len(candidates) or candidates[i] > t:
                return []
            ret = []
            j = i
            while j < len(candidates):
                for x in dfs(j+1, t-candidates[j]):
                    ret.append([candidates[j], *x])
                j += 1
                while j < len(candidates) and candidates[j] == candidates[j-1]:
                    j += 1
            return ret

        return dfs(0, target)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        DFS using nonlocal variable
        Copy a current path only at last.
        Time complexity: O(n*m)
        Space complexity: O(n)  # callstack exclude the return
        """
        candidates = list(sorted(candidates))
        result = []

        def dfs(i, t, cur):
            if t == 0:
                result.append(cur[:])
            if i == len(candidates) or candidates[i] > t:
                return
            j = i
            while j < len(candidates) and candidates[j] <= t:
                cur.append(candidates[j])
                dfs(j+1, t-candidates[j], cur)
                cur.pop()
                j += 1
                while j < len(candidates) and candidates[j] == candidates[j-1]:
                    j += 1

        dfs(0, target, [])
        return result


@pytest.mark.parametrize('candidates, target, expected', [
    ([10,1,2,7,6,1,5], 8, [
        [1,1,6],
        [1,2,5],
        [1,7],
        [2,6]
    ]),
    ([2,5,2,1,2], 5,
     [
         [1,2,2],
         [5]
     ]),
    ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27, []),
])
def test(candidates, target, expected):
    assert sorted(expected) == sorted(Solution().combinationSum2(candidates, target))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
