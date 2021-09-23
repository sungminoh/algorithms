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
import sys
from collections import deque
from collections import defaultdict
from typing import List
import pytest


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


@pytest.mark.parametrize('n, edges, expected', [
    (6, [[0,1],[0,2],[2,3],[2,4],[2,5]], [8,12,6,10,10,10]),
    (1, [], [0]),
    (2, [[1,0]], [1,1]),
    (4, [[1,2],[3,2],[3,0]], [6,6,4,4]),
    (7, [[0,5],[3,5],[1,3],[0,2],[4,6],[5,6]], [12,17,17,12,17,9,12]),
    (7, [[1,4],[5,1],[0,1],[2,6],[6,3],[2,5]], [17,12,12,20,17,11,15]),
    json.load(open(Path(__file__).parent/'testcase.json')),
])
def test(n, edges, expected):
    assert expected == Solution().sumOfDistancesInTree(n, edges)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
