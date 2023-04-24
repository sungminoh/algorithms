#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

Example 1:

Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

Example 2:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2

Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.

Constraints:

	1 <= n <= 105
	1 <= connections.length <= min(n * (n - 1) / 2, 105)
	connections[i].length == 2
	0 <= ai, bi < n
	ai != bi
	There are no repeated connections.
	No two computers are connected by more than one cable.
"""
from collections import defaultdict
from typing import List
import pytest
import sys


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """Apr 23, 2023 21:05"""

        class UnionFind:
            def __init__(self):
                self.p = {}
                self.edges = defaultdict(int)

            def find(self, i):
                self.p.setdefault(i, i)
                if i != self.p[i]:
                    self.p[i] = self.find(self.p[i])
                return self.p[i]

            def union(self, i, j):
                self.edges[i] += 1
                self.edges[j] += 1
                ip = self.find(i)
                jp = self.find(j)
                self.p[max(ip, jp)] = min(ip, jp)

        uf = UnionFind()
        for a, b in connections:
            uf.union(a, b)

        edges = defaultdict(int)
        cnt = defaultdict(int)
        for i in range(n):
            ip = uf.find(i)
            cnt[ip] += 1
            edges[ip] += uf.edges[i]

        remainder = 0
        for rep in cnt:
            remainder += edges[rep]//2 - (cnt[rep]-1)

        return -1 if remainder < len(cnt)-1 else len(cnt)-1


@pytest.mark.parametrize('args', [
    ((4, [[0,1],[0,2],[1,2]], 1)),
    ((6, [[0,1],[0,2],[0,3],[1,2],[1,3]], 2)),
    ((6, [[0,1],[0,2],[0,3],[1,2]], -1)),
])
def test(args):
    assert args[-1] == Solution().makeConnected(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
