#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

Example 1:

Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).

Example 2:

Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation: There is a cycle from 0 to 0.

Constraints:

	n == colors.length
	m == edges.length
	1 <= n <= 105
	0 <= m <= 105
	colors consists of lowercase English letters.
	0 <= aj, bj < n
"""
from collections import Counter
from collections import defaultdict
from typing import Tuple
from typing import Dict
from typing import List
import pytest
import sys


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """TLE"""
        indegree = defaultdict(int)
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            indegree[b] += 1
        if not g:
            return 1

        starts = [n for n in g if indegree[n] == 0]
        if not starts:
            return -1 if indegree else 0

        visited = [False for _ in colors]
        cnt = Counter()
        def dfs(n):
            cnt[colors[n]] += 1
            visited[n] = True
            ret = 0
            if not g[n]:
                ret = cnt.most_common(1)[0][1]
            else:
                for m in g[n]:
                    if visited[m]:
                        ret = float('inf')
                    else:
                        ret = max(ret, dfs(m))
            cnt[colors[n]] -= 1
            visited[n] = False
            return ret

        ret = max(dfs(n) for n in starts)
        return ret if ret != float('inf') else -1

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """TLE"""
        indegree = defaultdict(int)
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            indegree[b] += 1
        if not g:
            return 1

        starts = [n for n in g if indegree[n] == 0]
        if not starts:
            return -1 if indegree else 0


        palette = {c: i for i, c in enumerate(set(colors))}

        class MyCounter:
            def __init__(self, d: List[Tuple[str, int]]):
                self.cnt = [0] * len(palette)
                for k, v in d:
                    self.cnt[palette[k]] += v

            def __add__(self, other):
                ret = MyCounter([])
                ret.cnt = [a + b for a, b in zip(self.cnt, other.cnt)]
                return ret

            def __hash__(self):
                return hash(tuple(self.cnt))

            def most_common(self):
                return max(self.cnt)


        visited = [False]*len(colors)
        memo = {}  # returns possible counters under the node
        def dfs(n):
            if n in memo:
                return memo[n]
            visited[n] = True
            cycle = False
            cnt = MyCounter([(colors[n], 1)])
            ret = set()
            if not g[n]:
                ret.add(cnt)
            else:
                for m in g[n]:
                    if visited[m]:
                        cycle = True
                    else:
                        sub_cnts = dfs(m)
                        if not sub_cnts:
                            cycle = True
                        for sub_cnt in sub_cnts:
                            ret.add(cnt + sub_cnt)
            if cycle:
                ret = []

            visited[n] = False
            memo[n] = ret
            return memo[n]

        ret = 0
        for n in starts:
            sub = dfs(n)
            if not sub:
                return -1
            for cnt in sub:
                ret = max(ret, cnt.most_common())
        return ret

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """Sep 02, 2023 17:14"""
        indegree = defaultdict(int)
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            indegree[b] += 1
        if not g:
            return 1

        starts = [n for n in g if indegree[n] == 0]
        if not starts:
            return -1 if indegree else 0

        palette = {c: i for i, c in enumerate(set(colors))}
        cindexes = [palette[c] for c in colors]
        visited = [False]*len(colors)

        memo = {}  # returns possible counters under the node
        def dfs(n):
            if n in memo:
                return memo[n]
            visited[n] = True
            cycle = False
            cnt = [0]*len(palette)
            cnt[cindexes[n]] = 1
            if g[n]:
                for m in g[n]:
                    if visited[m]:
                        cycle = True
                    else:
                        sub_cnt = dfs(m)
                        if not sub_cnt:
                            cycle = True
                        else:
                            for i, c in enumerate(sub_cnt):
                                cnt[i] = max(cnt[i], c + (1 if i == cindexes[n] else 0))
            if cycle:
                cnt = None
            visited[n] = False
            memo[n] = cnt
            return memo[n]

        ret = 0
        for n in starts:
            cnt = dfs(n)
            if not cnt:
                return -1
            ret = max(ret, max(cnt))
        return ret


@pytest.mark.parametrize('args', [
    (("abaca", [[0,1],[0,2],[2,3],[3,4]], 3)),
    (("a", [[0,0]], -1)),
    (("g", [], 1)),
    (("nnllnzznn", [[0,1],[1,2],[2,3],[2,4],[3,5],[4,6],[3,6],[5,6],[6,7],[7,8]], 5)),
    (("ab", [[0,1],[1,1]], -1)),
    (("qddqqqddqqdqddddddqdqqddddqdqdqqdddqddqdqqdqqqqqddqddqqddqqqdqqqqdqdddddqdq", [[0,1],[1,2],[2,3],[3,4],[3,5],[4,5],[3,6],[5,6],[6,7],[5,7],[3,7],[6,8],[5,8],[4,8],[8,9],[9,10],[10,11],[9,11],[9,12],[11,12],[6,12],[11,13],[9,13],[13,14],[12,14],[10,14],[11,14],[13,15],[14,15],[12,16],[9,16],[7,16],[15,17],[13,17],[17,18],[11,18],[17,19],[18,19],[13,19],[17,20],[18,20],[19,21],[17,21],[12,22],[21,22],[16,22],[22,23],[21,23],[16,24],[22,24],[15,25],[24,25],[20,25],[12,25],[23,26],[26,27],[13,27],[27,28],[21,28],[26,28],[28,29],[15,30],[27,30],[24,30],[21,30],[27,31],[30,31],[25,32],[29,32],[17,33],[31,33],[32,33],[25,34],[33,35],[31,35],[34,35],[30,36],[35,37],[36,37],[26,38],[36,38],[34,38],[37,38],[38,39],[22,39],[39,40],[40,41],[38,41],[20,41],[41,42],[37,42],[40,43],[42,43],[43,44],[41,44],[32,44],[38,44],[39,44],[43,45],[44,45],[44,46],[45,46],[45,47],[42,47],[43,48],[45,49],[45,50],[48,51],[30,51],[46,52],[48,52],[38,52],[51,52],[47,53],[45,53],[53,54],[48,54],[30,54],[50,55],[30,55],[36,55],[55,56],[39,56],[54,56],[50,57],[56,58],[32,58],[57,59],[49,59],[38,60],[60,61],[35,61],[54,61],[53,61],[54,62],[58,62],[62,63],[40,63],[58,63],[49,64],[63,64],[47,64],[39,64],[45,64],[62,65],[64,65],[54,65],[52,66],[61,66],[60,66],[55,67],[65,67],[45,68],[56,68],[36,68],[67,69],[66,69],[27,70],[60,70],[67,70],[48,71],[70,71],[53,71],[62,72],[72,73],[73,74]], 26)),
])
def test(args):
    assert args[-1] == Solution().largestPathValue(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
