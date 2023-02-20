#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: The first group has [1,4], and the second group has [2,3].

Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Explanation: We need at least 3 groups to divide them. We cannot put them in two groups.

Constraints:

	1 <= n <= 2000
	0 <= dislikes.length <= 104
	dislikes[i].length == 2
	1 <= ai < bi <= n
	All the pairs of dislikes are unique.
"""
from typing import List
import pytest
import sys


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        """Feb 19, 2023 17:34"""
        graph = [[] for _ in range(n+1)]
        for i, j in dislikes:
            graph[i].append(j)
            graph[j].append(i)

        def dfs(i, gp):
            for j in graph[i]:
                if j in group:
                    if group[j] == gp:
                        return False
                else:
                    group[j] = -gp
                    if not dfs(j, -gp):
                        return False
            return True

        group = {}
        for i, _ in dislikes:
            if i not in group:
                group[i] = 1
                if not dfs(i, 1):
                    return False
        return True


@pytest.mark.parametrize('n, dislikes, expected', [
    (4, [[1,2],[1,3],[2,4]], True),
    (3, [[1,2],[1,3],[2,3]], False),
    (1, [], True),
    (5, [[1,2],[3,4],[4,5],[3,5]], False),
])
def test(n, dislikes, expected):
    assert expected == Solution().possibleBipartition(n, dislikes)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
