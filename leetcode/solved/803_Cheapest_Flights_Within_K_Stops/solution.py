#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Example 1:

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Example 2:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Example 3:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

Constraints:

	1 <= n <= 100
	0 <= flights.length <= (n * (n - 1) / 2)
	flights[i].length == 3
	0 <= fromi, toi < n
	fromi != toi
	1 <= pricei <= 104
	There will not be any multiple flights between two cities.
	0 <= src, dst, k < n
	src != dst
"""
import heapq
from typing import List
import pytest
import sys


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """May 02, 2020 02:07"""
        mat = [[-1] * n for _ in range(n)]
        for s, d, p in flights:
            mat[s][d] = p

        dist = [{} for _ in range(K + 1)]
        for city, price in enumerate(mat[src]):
            if price < 0:
                continue
            dist[0][city] = price
        for i in range(1, K + 1):
            for depart, spend in dist[i - 1].items():
                for arrival, price in enumerate(mat[depart]):
                    if price < 0:
                        continue
                    dist[i][arrival] = min(dist[i].get(arrival, float('inf')), spend + price)
        prices = [d[dst] for d in dist if dst in d]
        return min(prices) if prices else -1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """May 02, 2020 02:12"""
        mat = [[-1] * n for _ in range(n)]
        for s, d, p in flights:
            mat[s][d] = p

        connected = [(0, -1, src)]
        # visited = set()
        while connected:
            p, d, arrival = heapq.heappop(connected)
            if arrival == dst:
                return p
            if d < K:
                for connected_city, price in enumerate(mat[arrival]):
                    if price < 0:
                        continue
                    heapq.heappush(connected, (p + price, d + 1, connected_city))
        return -1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """Mar 12, 2023 17:33"""
        g = [{} for _ in range(n)]
        for f, t, p in flights:
            g[f][t] = p

        spending = {src: 0}
        q = [(src, 0)]
        dist = 0
        while q and dist < k+1:
            _q = []
            for a, total in q:
                if spending[a] > total:
                    continue
                for b, price in g[a].items():
                    spend = total + price
                    if spend < spending.get(b, float('inf')):
                        spending[b] = spend
                        _q.append((b, spend))
            q = _q
            dist += 1

        return spending.get(dst, -1)


@pytest.mark.parametrize('args', [
    ((4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1, 700)),
    ((3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1, 200)),
    ((3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0, 500)),
    ((5, [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], 2, 1, 1, -1)),
    ((5,[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],0,2,2, 7)),
    ((10,[[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]],6,0,7, 14)),
])
def test(args):
    assert args[-1] == Solution().findCheapestPrice(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
