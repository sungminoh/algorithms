#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

Return the number of pairs of different nodes that are unreachable from each other.

Example 1:

Input: n = 3, edges = [[0,1],[0,2],[1,2]]
Output: 0
Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.

Example 2:

Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
Output: 14
Explanation: There are 14 pairs of nodes that are unreachable from each other:
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
Therefore, we return 14.

Constraints:

	1 <= n <= 105
	0 <= edges.length <= 2 * 105
	edges[i].length == 2
	0 <= ai, bi < n
	ai != bi
	There are no repeated edges.
"""
from collections import defaultdict
from typing import List
import pytest
import sys


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        """Apr 23, 2023 21:24"""
        class UnionFind:
            def __init__(self):
                self.p = {}

            def find(self, i):
                self.p.setdefault(i, i)
                if self.p[i] != i:
                    self.p[i] = self.find(self.p[i])
                return self.p[i]

            def union(self, i, j):
                ip = self.find(i)
                jp = self.find(j)
                self.p[max(ip, jp)] = min(ip, jp)

        uf = UnionFind()
        for a, b in edges:
            uf.union(a, b)

        cnt = defaultdict(int)
        for i in range(n):
            cnt[uf.find(i)] += 1

        ret = 0
        acc = 0
        for c in cnt.values():
            ret += acc*c
            acc += c
        return ret


@pytest.mark.parametrize('args', [
    ((3, [[0,1],[0,2],[1,2]], 0)),
    ((7, [[0,2],[0,5],[2,4],[1,6],[5,4]], 14)),
])
def test(args):
    assert args[-1] == Solution().countPairs(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
