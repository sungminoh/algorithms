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

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""
from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.build_graph(numCourses, prerequisites)
        basics = set(range(numCourses)).difference(self.num_prerequisites.keys())
        curriculum = []
        while basics:
            course = basics.pop()
            curriculum.append(course)
            for next_course in self.next_courses[course]:
                self.num_prerequisites[next_course] -= 1
                if self.num_prerequisites[next_course] == 0:
                    basics.add(next_course)
        if len(curriculum) == numCourses:
            return curriculum
        else:
            return []

    def build_graph(self, numCourses, prerequisites):
        self.next_courses = defaultdict(set)
        self.num_prerequisites = defaultdict(int)
        for cur, pre in prerequisites:
            self.next_courses[pre].add(cur)
            self.num_prerequisites[cur] += 1


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
        actual = len(Solution().findOrder(numCourses, prerequisites)) == numCourses
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')


if __name__ == '__main__':
    main()
