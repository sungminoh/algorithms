#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

	For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:

	1 <= numCourses <= 2000
	0 <= prerequisites.length <= numCourses * (numCourses - 1)
	prerequisites[i].length == 2
	0 <= ai, bi < numCourses
	ai != bi
	All the pairs [ai, bi] are distinct.
"""
import sys
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """03/15/2019 22:54"""
        next_courses = defaultdict(set)
        num_prerequisites = defaultdict(int)
        for cur, pre in prerequisites:
            next_courses[pre].add(cur)
            num_prerequisites[cur] += 1

        basics = set(range(numCourses)).difference(num_prerequisites.keys())
        curriculum = []
        while basics:
            course = basics.pop()
            curriculum.append(course)
            for next_course in next_courses[course]:
                num_prerequisites[next_course] -= 1
                if num_prerequisites[next_course] == 0:
                    basics.add(next_course)
        if len(curriculum) == numCourses:
            return curriculum
        else:
            return []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = {i: set() for i in range(numCourses)}
        post = {i: set() for i in range(numCourses)}
        for a, b in prerequisites:
            pre[a].add(b)
            post[b].add(a)

        ret = []
        degree_zero = [a for a, bs in pre.items() if len(bs) == 0]
        while degree_zero:
            new_degree_zero = []
            ret.extend(degree_zero)
            for b in degree_zero:
                for a in post[b]:
                    pre[a].discard(b)
                    if len(pre[a]) == 0:
                        new_degree_zero.append(a)
            degree_zero = new_degree_zero

        return ret if len(ret) == numCourses else []


@pytest.mark.parametrize('numCourses, prerequisites, expected', [
    (2, [[1,0]], [0,1]),
    (4, [[1,0],[2,0],[3,1],[3,2]], [0,2,1,3]),
    (1, [], [0]),
    (3, [[1,0],[1,2],[0,1]], []),
])
def test(numCourses, prerequisites, expected):
    assert expected == Solution().findOrder(numCourses, prerequisites)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
