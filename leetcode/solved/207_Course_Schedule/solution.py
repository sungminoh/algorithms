#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""
from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        self.build_graph(numCourses, prerequisites)
        if not self.indep:
            return False
        self.remains = set(range(numCourses))
        for i in self.indep:
            self.path = set()
            if not self.dfs(i):
                return False
        return len(self.remains) == 0

    def build_graph(self, numCourses, prerequisites):
        self.graph = defaultdict(list)
        self.indep = set(range(numCourses))
        for pre, cur in prerequisites:
            self.graph[pre].append(cur)
            if cur in self.indep:
                self.indep.remove(cur)

    def dfs(self, k):
        if k in self.path:
            return False
        if k not in self.remains:
            return True
        self.remains.remove(k)
        self.path.add(k)
        ret = all(self.dfs(n) for n in self.graph[k])
        self.path.remove(k)
        return ret


def main():
    inputs = [
        (2, [[1, 0]]),
        (2, [[1, 0], [0, 1]]),
        (1, []),
        (3, [[1, 0]]),
        (3, [[1, 0], [2, 0]]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
        (3, [[0, 2], [1, 2], [2, 0]]),
        (8, [[1, 0], [2, 6], [1, 7], [5, 1], [6, 4], [7, 0], [0, 5]])
    ]
    exptecteds = [
        True,
        False,
        True,
        True,
        True,
        True,
        False,
        False
    ]
    for (numCourses, prerequisites), expected in zip(inputs, exptecteds):
        actual = Solution().canFinish(numCourses, prerequisites)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')

if __name__ == '__main__':
    main()
