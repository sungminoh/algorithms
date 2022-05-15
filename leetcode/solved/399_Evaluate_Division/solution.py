#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

Constraints:

	1 <= equations.length <= 20
	equations[i].length == 2
	1 <= Ai.length, Bi.length <= 5
	values.length == equations.length
	0.0 < values[i] <= 20.0
	1 <= queries.length <= 20
	queries[i].length == 2
	1 <= Cj.length, Dj.length <= 5
	Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""
from collections import defaultdict
import sys
from typing import List
import pytest


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """04/21/2020 00:52"""
        relations = defaultdict(list)
        for (a, b), k in zip(equations, values):
            relations[a].append((k, b))
            relations[b].append((1/k, a))

        memo = dict()
        def dfs(s, e, visited):
            if (s, e) in memo:
                return memo[(s, e)]
            for coeficient, n in relations[s]:
                if n == e:
                    return coeficient
                if n not in visited:
                    visited.add(s)
                    ret = dfs(n, e, visited)
                    if ret > 0:
                        memo[(s, e)] = coeficient * ret
                        return memo[(s, e)]
                    visited.remove(s)
            return -1

        return [dfs(a, b, set()) for a, b in queries]

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """DFS"""
        relation = {}
        for (a, b), v in zip(equations, values):
            relation.setdefault(a, {})
            relation.setdefault(b, {})
            relation[a][b] = v
            relation[b][a] = 1/v

        def dfs(s, e, visited):
            if s not in relation:
                return -1.0
            if s == e:
                return 1.0
            for k, v in relation[s].items():
                if k not in visited:
                    visited.add(k)
                    r = dfs(k, e, visited)
                    if r != -1:
                        return v*r
            return -1.0

        return [dfs(a, b, set()) for a, b in queries]

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """02/21/2022 11:08
        Union Set
        Time complexity: O(nlogn) + O(mlogn)
        Space complexity: O(n)
        """
        class UnionFind:
            def __init__(self):
                self.d = {}

            def find(self, x):
                """O(logn)"""
                if x not in self.d:
                    self.d[x] = [x, 1]
                p, v = self.d[x]
                if x != p:
                    root, multiple = self.find(p)
                    self.d[x] = [root, multiple*v]
                return self.d[x]

            def union(self, a, b, m):
                """O(logn)"""
                pa, ma = self.find(a)
                pb, mb = self.find(b)
                # a = m*b
                # a = ma*pa
                # b = mb*pb
                # ma*pa = m*mb*pb
                # pa = m*mb/ma * pb
                # pb = ma/(m*mb) * pa
                if pa < pb:
                    self.d[pb] = [pa, ma/(m*mb)]
                else:
                    self.d[pa] = [pb, (m*mb)/ma]

        us = UnionFind()
        # log(n*logn)
        for (a, b), v in zip(equations, values):
            us.union(a, b, v)

        ret = []
        # log(m*logn)
        for a, b in queries:
            if a not in us.d or b not in us.d:
                ret.append(-1.0)
            else:
                pa, ma = us.find(a)
                pb, mb = us.find(b)
                # a = ma*pa
                # b = mb*pb
                if pa == pb:
                    ret.append(ma/mb)
                else:
                    ret.append(-1.0)

        return ret

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """05/14/2022 18:01"""
        graph = {}
        for (a, b), v in zip(equations, values):
            graph.setdefault(a, {})
            graph.setdefault(b, {})
            graph[a][b] = v
            graph[b][a] = 1/v

        def dfs(a, b, visited):
            if a not in graph:
                return -1.
            if b in graph[a]:
                return graph[a][b]
            for k, v in graph[a].items():
                if k not in visited:
                    visited.add(k)
                    sub = dfs(k, b, visited)
                    if sub >= 0:
                        return v*sub
                    visited.remove(k)
            return -1.

        return [dfs(a, b, set([a])) for a, b in queries]


@pytest.mark.parametrize('equations, values, queries, expecteds', [
    ([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]], [6.00000,0.50000,-1.00000,1.00000,-1.00000]),
    ([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]], [3.75000,0.40000,5.00000,0.20000]),
    ([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]], [0.50000,2.00000,-1.00000,-1.00000]),
])
def test(equations, values, queries, expecteds):
    assert expecteds == Solution().calcEquation(equations, values, queries)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
