
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given  a / b = 2.0, b / c = 3.0.
queries are:  a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return  [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is:  vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return  vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
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




@pytest.mark.parametrize('equations, values, queries, expected', [
    ([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]], [6.00000,0.50000,-1.00000,1.00000,-1.00000])
])
def test(equations, values, queries, expected):
    assert expected == Solution().calcEquation(equations, values, queries)
