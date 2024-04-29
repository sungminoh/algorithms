#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
An array is squareful if the sum of every pair of adjacent elements is a perfect square.

Given an integer array nums, return the number of permutations of nums that are squareful.

Two permutations perm1 and perm2 are different if there is some index i such that perm1[i] != perm2[i].

Example 1:

Input: nums = [1,17,8]
Output: 2
Explanation: [1,8,17] and [17,8,1] are the valid permutations.

Example 2:

Input: nums = [2,2,2]
Output: 1

Constraints:

	1 <= nums.length <= 12
	0 <= nums[i] <= 109
"""
from collections import Counter
from collections import defaultdict
from typing import List
import pytest
import sys


class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        """Apr 28, 2024 19:06 TLE"""
        N = len(nums)

        def is_square(x):
            return pow(int(pow(x, 0.5)), 2) == x

        graph = [[] for _ in range(N)]
        for i in range(N):
            for j in range(i):
                if is_square(nums[i] + nums[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        visited = set()
        def dfs(i, acc):
            if len(acc) == N:
                visited.add(tuple([nums[x] for x in acc]))
            for j in graph[i]:
                if j not in acc:
                    acc.append(j)
                    dfs(j, acc)
                    acc.pop()

        for i in range(N):
            dfs(i, [i])
        return len(visited)

    def numSquarefulPerms(self, nums: List[int]) -> int:
        """Apr 28, 2024 19:15"""
        N = len(nums)

        def is_square(x):
            return pow(int(pow(x, 0.5)), 2) == x

        counter = Counter(nums)
        distinct_nums = list(counter.keys())
        DN = len(distinct_nums)

        graph = defaultdict(set)
        for i in range(DN):
            for j in range(i+1):
                a, b = distinct_nums[i], distinct_nums[j]
                if is_square(a + b):
                    graph[a].add(b)
                    graph[b].add(a)

        def dfs(a, acc, cnt):
            if cnt == N:
                return 1
            ret = 0
            for b in graph[a]:
                acc.setdefault(b, 0)
                if acc[b] < counter[b]:
                    acc[b] += 1
                    ret += dfs(b, acc, cnt+1)
                    acc[b] -= 1
            return ret

        ret = 0
        for a in distinct_nums:
            ret += dfs(a, {a: 1}, 1)
        return ret


@pytest.mark.parametrize('args', [
    (([1,17,8], 2)),
    (([2,2,2], 1)),
    (([2,2,2,2,2,2,2,2,2,2,2], 1)),
])
def test(args):
    assert args[-1] == Solution().numSquarefulPerms(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
