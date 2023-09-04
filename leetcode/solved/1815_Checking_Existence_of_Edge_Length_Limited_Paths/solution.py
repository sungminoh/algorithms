#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.

Example 1:

Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
Output: [false,true]
Explanation: The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.

Example 2:

Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
Output: [true,false]
Explanation: The above figure shows the given graph.

Constraints:

	2 <= n <= 105
	1 <= edgeList.length, queries.length <= 105
	edgeList[i].length == 3
	queries[j].length == 3
	0 <= ui, vi, pj, qj <= n - 1
	ui != vi
	pj != qj
	1 <= disi, limitj <= 109
	There may be multiple edges between two nodes.
"""
from pathlib import Path
import json
from functools import lru_cache
from collections import deque
from collections import defaultdict
from heapq import heappop, heappush
from typing import List
import pytest
import sys


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """TLE"""
        g = defaultdict(defaultdict)
        for u, v, d in edgeList:
            g[u][v] = g[v][u] = min(d, g[u].get(v, float('inf')), g[v].get(u, float('inf')))


        done = [False]*n
        memo = [[float('inf')]*n for _ in range(n)]
        def find(u):
            visited = [False]*n
            h = [(0, u)]
            while h:
                d, x = heappop(h)
                if visited[x]:
                    continue
                visited[x] = True
                memo[u][x] = memo[x][u] = min(memo[u][x], memo[x][u], d)
                for y, _d in g[x].items():
                    heappush(h, (max(d, _d), y))
            done[u] = True

        ret = []
        for u, v, d in queries:
            if not done[u]:
                find(u)
            ret.append(memo[u][v] < d)
        return ret

    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """MLE"""
        h = []
        for u, v, d in edgeList:
            heappush(h, (d, u, v))

        parents = [i for i in range(n)]
        memo = [[float('inf')]*n for _ in range(n)]
        def find(i):
            if parents[i] == i:
                return i
            parents[i] = find(parents[i])
            return parents[i]

        children = {i: set([i]) for i in range(n)}
        while h:
            d, u, v = heappop(h)
            pu = find(u)
            pv = find(v)
            if pu != pv:
                p = min(pu, pv)
                cs = set()
                for cu in children[pu]:
                    for cv in children[pv]:
                        memo[cu][cv] = memo[cv][cu] = d
                        cs.add(cu)
                        cs.add(cv)
                parents[pu] = parents[pv] = p
                children[p] = cs

        answer = []
        for u, v, l in queries:
            answer.append(memo[u][v] < l)

        return answer

    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """Sep 04, 2023 14:56"""
        parents = [i for i in range(n)]
        memo = defaultdict(int)
        def find(i):
            while parents[i] != i:
                i = parents[i]
            return i

        for u, v, d in sorted(edgeList, key=lambda x: x[2]):
            pu = find(u)
            pv = find(v)
            if pu != pv:
                p = min(pu, pv)
                memo[pu, pv] = memo[pv, pu] = d
                parents[pu] = parents[pv] = p

        answer = []
        for u, v, l in queries:
            dist = {u: 0}
            while u != parents[u]:
                dist[parents[u]] = memo[u, parents[u]]
                u = parents[u]
            d = 0
            while v != parents[v] and v not in dist:
                d = max(d, memo[v, parents[v]])
                v = parents[v]
            if v in dist:
                answer.append(max(d, dist[v]) < l)
            else:
                answer.append(False)

        return answer

    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """Sep 04, 2023 15:05"""
        parents = [i for i in range(n)]
        def find(i):
            while parents[i] != i:
                parents[i] = parents[parents[i]]
                i = parents[i]
            return i

        def union(u, v):
            pu = find(u)
            pv = find(v)
            if pu != pv:
                parents[pu] = parents[pv] = min(pu, pv)

        idx = 0
        answer = [False] * len(queries)
        edgeList.sort(key=lambda x: x[2])
        for i, (u, v, l) in sorted(enumerate(queries), key=lambda x: x[1][2]):
            while idx < len(edgeList) and edgeList[idx][2] < l:
                union(edgeList[idx][0], edgeList[idx][1])
                idx += 1
            answer[i] = find(u) == find(v)

        return answer


@pytest.mark.parametrize('args', [
    ((3, [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], [[0,1,2],[0,2,5]], [False,True])),
    ((5, [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], [[0,4,14],[1,4,13]], [True,False])),
    (json.load(open(Path(__file__).parent/'testcase.json'))),
    (json.load(open(Path(__file__).parent/'testcase2.json'))),
])
def test(args):
    assert args[-1] == Solution().distanceLimitedPathsExist(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
