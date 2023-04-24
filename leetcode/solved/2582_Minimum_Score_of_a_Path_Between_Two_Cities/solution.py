#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

	A path is a sequence of roads between two cities.
	It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
	The test cases are generated such that there is at least one path between 1 and n.

Example 1:

Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
Output: 5
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.

Example 2:

Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
Output: 2
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.

Constraints:

	2 <= n <= 105
	1 <= roads.length <= 105
	roads[i].length == 3
	1 <= ai, bi <= n
	ai != bi
	1 <= distancei <= 104
	There are no repeated edges.
	There is at least one path between 1 and n.
"""
from heapq import heappop, heappush
from typing import List
import pytest
import sys


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """Apr 23, 2023 19:11"""
        g = [{} for _ in range(n+1)]
        for a, b, d in roads:
            g[a][b] = g[b][a] = d

        def dijkstra(a, dest):
            dists = {}
            h = []
            for b, d in g[a].items():
                heappush(h, (d, b))
            while h:
                d, b = heappop(h)
                if d < dists.get(b, float('inf')):
                    dists[b] = d
                    for c, _d in g[b].items():
                        heappush(h, (min(d, _d), c))
            return dists.get(dest, float('inf'))

        return dijkstra(1, n)

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """Apr 23, 2023 19:19
        Simply the minimum path connected to the start point
        """
        g = [{} for _ in range(n+1)]
        for a, b, d in roads:
            g[a][b] = g[b][a] = d

        ret = float('inf')
        visited = set()
        q = [1]
        while q:
            _q = []
            for a in q:
                for b, d in g[a].items():
                    if b not in visited:
                        visited.add(b)
                        _q.append(b)
                    ret = min(ret, d)
            q = _q
        return ret if n in visited else float('inf')


@pytest.mark.parametrize('args', [
    ((4, [[1,2,9],[2,3,6],[2,4,5],[1,4,7]], 5)),
    ((4, [[1,2,2],[1,3,4],[3,4,7]], 2)),
])
def test(args):
    assert args[-1] == Solution().minScore(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
