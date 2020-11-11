
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:

The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph looks like this:

The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

Note:

	The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
	The size of flights will be in range [0, n * (n - 1) / 2].
	The format of each flight will be (src, dst, price).
	The price of each flight will be in the range [1, 10000].
	k is in the range of [0, n - 1].
	There will not be any duplicated flights or self cycles.
"""
import heapq
import sys
from typing import List
import pytest


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
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



    def _findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
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




@pytest.mark.parametrize('n, edges, src, dst, k, expected', [
    (3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1, 200),
    (3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0, 500),
    (5, [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], 2, 1, 1, -1),
    (5,[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],0,2,2, 7),
    (10,[[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]],6,0,7, 14),
])
def test(n, edges, src, dst, k, expected):
    print()
    assert expected == Solution().findCheapestPrice(n, edges, src, dst, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
