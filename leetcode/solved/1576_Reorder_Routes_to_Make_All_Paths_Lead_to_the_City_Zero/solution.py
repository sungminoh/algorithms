#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

Example 1:

Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 2:

Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 3:

Input: n = 3, connections = [[1,0],[2,0]]
Output: 0

Constraints:

	2 <= n <= 5 * 104
	connections.length == n - 1
	connections[i].length == 2
	0 <= ai, bi <= n - 1
	ai != bi
"""
from collections import defaultdict
from typing import List
import pytest
import sys


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """Apr 23, 2023 21:17"""
        g = [{} for _ in range(n)]
        for a, b in connections:
            g[a][b] = 1
            g[b][a] = 0

        visited = set([0])
        def dfs(a):
            ret = 0
            for b in g[a]:
                if b not in visited:
                    visited.add(b)
                    ret += g[a][b]
                    ret += dfs(b)
            return ret
        return dfs(0)


@pytest.mark.parametrize('args', [
    ((6, [[0,1],[1,3],[2,3],[4,0],[4,5]], 3)),
    ((5, [[1,0],[1,2],[3,2],[3,4]], 2)),
    ((3, [[1,0],[2,0]], 0)),
])
def test(args):
    assert args[-1] == Solution().minReorder(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
