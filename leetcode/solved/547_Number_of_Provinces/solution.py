#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:

	1 <= n <= 200
	n == isConnected.length
	n == isConnected[i].length
	isConnected[i][j] is 1 or 0.
	isConnected[i][i] == 1
	isConnected[i][j] == isConnected[j][i]
"""
from typing import List
import pytest
import sys


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        """Jun 05, 2020 02:51"""
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(i):
            if M[i][i] == 0:
                return 0
            M[i][i] = 0
            for j_, v in enumerate(M[i]):
                if j_ == i or v <= 0:
                    continue
                dfs(j_)
            return 1

        cnt = 0
        if not M or not M[0]:
            return cnt
        for i in range(len(M)):
            cnt += dfs(i)
        return cnt

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """May 11, 2024 18:56"""
        N = len(isConnected)
        visited = 0

        def dfs(i):
            nonlocal visited
            for j, c in enumerate(isConnected[i]):
                if c == 0:
                    continue
                if not (1<<j)&visited:
                    visited |= (1<<j)
                    dfs(j)
            return 1

        ret = 0
        for i in range(N):
            if not (1<<i)&visited:
                ret += dfs(i)
        return ret


@pytest.mark.parametrize('args', [
    (([[1,1,0],[1,1,0],[0,0,1]], 2)),
    (([[1,0,0],[0,1,0],[0,0,1]], 3)),
    ([[1,1,0],
      [1,1,1],
      [0,1,1]], 1),
    ([[1,0,0,1],
      [0,1,1,0],
      [0,1,1,1],
      [1,0,1,1]], 1)
])
def test(args):
    assert args[-1] == Solution().findCircleNum(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
