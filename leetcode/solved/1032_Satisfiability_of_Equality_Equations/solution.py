#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

Example 1:

Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.

Example 2:

Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

Constraints:

	1 <= equations.length <= 500
	equations[i].length == 4
	equations[i][0] is a lowercase letter.
	equations[i][1] is either '=' or '!'.
	equations[i][2] is '='.
	equations[i][3] is a lowercase letter.
"""
from typing import List
import pytest
import sys


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        class UnionFind:
            def __init__(self):
                self.p = {}

            def union(self, a, b):
                x = self.find(a)
                y = self.find(b)
                self.p[x] = self.p[y] = min(x, y)

            def find(self, x):
                self.p.setdefault(x, x)
                if x != self.p[x]:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]

        uf = UnionFind()
        inequality = set()
        for equation in equations:
            a, b = sorted([equation[0], equation[-1]])
            if equation[1:-1] == '==':
                uf.union(a, b)
            else:
                inequality.add((a, b))

        for a, b in inequality:
            if uf.find(a) == uf.find(b):
                return False

        return True


@pytest.mark.parametrize('equations, expected', [
    (["a==b","b!=a"], False),
    (["b==a","a==b"], True),
])
def test(equations, expected):
    assert expected == Solution().equationsPossible(equations)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
