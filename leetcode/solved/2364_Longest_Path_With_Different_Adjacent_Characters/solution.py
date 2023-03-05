#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.

Example 1:

Input: parent = [-1,0,0,1,1,2], s = "abacbe"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
It can be proven that there is no longer path that satisfies the conditions.

Example 2:

Input: parent = [-1,0,0,0], s = "aabc"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is returned.

Constraints:

	n == parent.length == s.length
	1 <= n <= 105
	0 <= parent[i] <= n - 1 for all i >= 1
	parent[0] == -1
	parent represents a valid tree.
	s consists of only lowercase English letters.
"""
from typing import List
import pytest
import sys


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        """Mar 05, 2023 14:51"""
        n = len(parent)
        g = [[] for _ in range(n)]
        for i, p in enumerate(parent[1:], 1):
            g[p].append(i)

        ret = 0
        def dfs(a):
            nonlocal ret
            subs = [0, 0]
            for b in g[a]:
                sub = dfs(b)
                if s[b] != s[a]:
                    if sub > subs[0]:
                        subs[0] = sub
                        subs.sort()
            ret = max(ret, sum(subs)+1)
            return max(subs) + 1

        dfs(0)
        return ret


@pytest.mark.parametrize('args', [
    (([-1,0,0,1,1,2], "abacbe", 3)),
    (([-1,0,0,0], "aabc", 3)),
])
def test(args):
    assert args[-1] == Solution().longestPath(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
