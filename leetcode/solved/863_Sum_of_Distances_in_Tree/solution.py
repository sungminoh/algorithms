#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

Example 1:

Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.

Example 2:

Input: n = 1, edges = []
Output: [0]

Example 3:

Input: n = 2, edges = [[1,0]]
Output: [1,1]

Constraints:

	1 <= n <= 3 * 104
	edges.length == n - 1
	edges[i].length == 2
	0 <= ai, bi < n
	ai != bi
	The given input represents a valid tree.
"""
from pathlib import Path
import json
from collections import defaultdict
from collections import deque
from typing import List
import pytest
import sys


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        dp = [None] * n

        def bfs(i):
            ret = [float('inf')]*n
            ret[i] = 0
            queue = set([i])
            while queue:
                new_queue = set()
                for j in queue:
                    for k in graph[j]:
                        if ret[j] + 1 < ret[k]:
                            new_queue.add(k)
                            ret[k] = ret[j] + 1
                for j in queue:
                    if dp[j]:
                        for k in range(len(ret)):
                            cached_dist = ret[j] + dp[j][k]
                            if cached_dist < ret[k]:
                                ret[k] = cached_dist
                                if k in new_queue:
                                    new_queue.remove(k)
                queue = new_queue
            dp[i] = ret
            return sum(ret)

        return [bfs(i) for i in range(n)]

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        """Sep 19, 2021 22:59"""
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        children = [0]*n
        answer = [0]*n

        def dfs(i):
            children[i] += 1
            for j in graph[i]:
                if children[j] == 0:
                    dfs(j)
                    children[i] += children[j]
                    answer[i] += answer[j] + children[j]

        def find_answer(i, parent=-1):
            for j in graph[i]:
                if j != parent:
                    answer[j] = answer[i] - children[j] + n - children[j]
                    find_answer(j, i)

        dfs(0)
        find_answer(0)
        return answer

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        """TLE"""
        dists = [[0]*n for _ in range(n)]
        queue = deque([])
        for a, b in edges:
            dists[a][b] = dists[b][a] = 1
            queue.extend([(a, b), (b, a)])

        while queue:
            a, b = queue.popleft()
            for c, dist in enumerate(dists[b]):
                if dist == 0 or c == a or c == b:
                    continue
                dist_ac = dists[a][b]+dist
                if dists[a][c] == 0 or dist_ac < dists[a][c]:
                    dists[a][c] = dists[c][a] = dist_ac
                    queue.extend([(a, c), (c, a)])

        return [sum(row) for row in dists]

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        """TLE"""
        dists = [[0]*n for _ in range(n)]
        graph = [[] for _ in range(n)]
        for a, b in edges:
            dists[a][b] = dists[b][a] = 1
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(i, p):
            for j in range(n):
                if j != i and j != p and dists[p][j] > 0:
                    dists[i][j] = dists[j][i] = dists[i][p]+dists[p][j]
            for j in graph[i]:
                if j != p:
                    dfs(j, i)

        if n == 0:
            return []
        if n == 1:
            return [0]
        for j in graph[0]:
            dfs(j, 0)

        return [sum(row) for row in dists]

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        """TLE"""
        dists = [{} for _ in range(n)]
        graph = [[] for _ in range(n)]
        for a, b in edges:
            dists[a][b] = dists[b][a] = 1
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(i, p):
            for j in dists[p]:
                if j != i:
                    dists[i][j] = dists[j][i] = dists[i][p]+dists[p][j]
            for j in graph[i]:
                if j != p:
                    dfs(j, i)

        if n == 0:
            return []
        if n == 1:
            return [0]
        for j in graph[0]:
            dfs(j, 0)

        return [sum(dists[i].values()) for i in range(n)]

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        """Feb 19, 2023 18:59"""
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        numnodes = [0]*n
        sumdists = [0]*n

        def dfs(i):
            numnodes[i] += 1
            for j in graph[i]:
                if numnodes[j] == 0:
                    dfs(j)
                    numnodes[i] += numnodes[j]
                    # dist to i from sub nodes
                    sumdists[i] += numnodes[j] + sumdists[j]

        def merge(i, p):
            for j in graph[i]:
                if j != p:
                    numnodes_others = n - numnodes[j]
                    sumdists_others = sumdists[i] - sumdists[j] - numnodes[j]
                    # add dists to j from non sub nodes
                    sumdists[j] += sumdists_others + numnodes_others
                    merge(j, i)

        # 0 is the root
        dfs(0)
        merge(0, -1)
        return sumdists


@pytest.mark.parametrize('n, edges, expected', [
    (6, [[0,1],[0,2],[2,3],[2,4],[2,5]], [8,12,6,10,10,10]),
    (1, [], [0]),
    (2, [[1,0]], [1,1]),
    (200, [[112,91],[158,18],[183,96],[179,69],[183,157],[170,154],[173,162],[24,102],[140,100],[80,115],[87,154],[79,174],[46,115],[30,194],[129,9],[101,82],[170,26],[33,123],[172,124],[2,8],[148,149],[16,98],[174,48],[128,76],[175,87],[16,127],[171,124],[20,69],[128,159],[198,192],[99,63],[151,79],[194,155],[53,26],[2,133],[56,70],[154,191],[78,38],[137,70],[116,135],[69,176],[127,9],[14,1],[169,56],[187,125],[67,20],[59,33],[24,69],[89,126],[168,174],[110,194],[39,81],[58,191],[188,8],[51,166],[167,96],[23,96],[58,131],[122,20],[33,42],[25,0],[47,33],[37,132],[166,195],[57,131],[131,79],[78,92],[7,147],[62,68],[120,113],[172,80],[177,83],[154,197],[11,106],[79,147],[60,131],[161,85],[18,95],[152,80],[93,186],[145,175],[196,41],[39,27],[57,165],[150,29],[118,97],[51,56],[22,84],[161,32],[175,182],[171,45],[156,81],[113,162],[187,65],[32,153],[12,51],[163,54],[147,143],[142,9],[26,141],[163,33],[51,0],[172,91],[174,185],[131,113],[100,17],[51,50],[94,160],[44,111],[154,187],[170,157],[6,165],[72,52],[196,71],[134,100],[121,1],[61,146],[101,118],[126,166],[3,46],[87,80],[14,154],[178,39],[32,117],[40,61],[191,107],[98,119],[19,174],[67,74],[169,130],[105,39],[17,87],[56,64],[57,101],[135,150],[83,164],[34,197],[38,81],[87,128],[31,33],[21,69],[28,0],[12,88],[172,103],[51,114],[151,49],[73,4],[62,162],[56,139],[71,166],[72,3],[33,56],[136,129],[106,124],[84,13],[37,99],[56,66],[166,69],[109,90],[4,113],[46,36],[111,22],[127,160],[43,67],[80,198],[20,189],[37,127],[32,166],[87,29],[14,9],[86,131],[79,8],[5,16],[186,91],[144,191],[190,86],[179,180],[30,57],[177,51],[6,181],[10,170],[38,29],[55,138],[104,4],[55,172],[154,61],[95,136],[193,65],[22,90],[35,137],[199,161],[22,174],[46,184],[99,108],[75,65],[56,149],[58,51],[77,79],[15,106]], [1204,1300,1568,1768,1402,1832,1592,1572,1372,1266,1326,1952,1206,1936,1104,1952,1634,1242,2038,1554,1520,1530,1542,1902,1528,1402,1322,1984,1402,1224,1394,1554,1346,1356,1342,1760,1772,1632,1406,1786,1340,1746,1554,1912,1936,1954,1574,1554,1554,1574,1208,1010,2162,1520,1750,1568,1172,1202,922,1554,1224,1142,1596,2024,1370,1332,1370,1714,1794,1332,1366,1352,1964,1600,1912,1530,1442,1378,1602,1180,1200,1594,1592,1400,1738,1738,1222,1050,1404,1552,1738,1564,1800,1958,1836,1842,1704,1788,1830,1826,1436,1394,1726,1570,1600,1984,1754,1130,2024,1936,1786,1738,1762,1208,1208,1386,1812,1544,1590,2028,1406,1498,1718,1554,1560,1336,1354,1442,1244,1456,1566,1026,1830,1766,1634,1614,1648,1562,1766,1370,1634,1520,1464,1572,1130,1442,1340,1374,1566,1368,1418,1376,1398,1544,948,1786,1792,1318,2236,1442,1638,1540,1400,1552,1598,1396,1158,1902,1554,1368,1128,1756,1372,1598,1356,1244,1530,1204,1984,1528,1726,1790,1442,1510,1772,1554,1760,1138,1570,1718,1420,932,1594,1530,1588,1356,1548,1144,1396,1738]),
    json.load(open(Path(__file__).parent/'testcase.json')),
])
def test(n, edges, expected):
    assert expected == Solution().sumOfDistancesInTree(n, edges)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
