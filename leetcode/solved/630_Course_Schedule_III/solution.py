#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.

Example 1:

Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3
Explanation:
There are totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day.
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.

Example 2:

Input: courses = [[1,2]]
Output: 1

Example 3:

Input: courses = [[3,2],[4,3]]
Output: 0

Constraints:

	1 <= courses.length <= 104
	1 <= durationi, lastDayi <= 104
"""
import sys
from heapq import heappop, heappush
from typing import List
import pytest


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """05/20/2021 23:41
        After sort the course by the due, take course as much as possible.
        if a course doesn't end by its due, see if we could've take the current
        course instead of one that took the longest
        Time complexity: O(n*logn)
        Space complexity: O(n)
        """
        taken = []
        current = 0
        for course in sorted(courses, key=lambda x: x[1]):
            if current + course[0] <= course[1]:
                heappush(taken, -course[0])
                current += course[0]
            elif taken:
                longest_time_taken = -taken[0]
                if current - longest_time_taken + course[0] <= course[1] \
                        and course[0] < longest_time_taken:
                    heappop(taken)
                    heappush(taken, -course[0])
                    current -= longest_time_taken
                    current += course[0]
        return len(taken)

    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """05/20/2021 23:48
        Same logic but simplified
        Time complexity: O(n*logn)
        Space complexity: O(n)
        """
        taken = []
        current = 0
        for takes, due in sorted(courses, key=lambda x: x[1]):
            current += takes
            heappush(taken, -takes)
            if current > due:
                current += heappop(taken)
        return len(taken)

    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """07/05/2022 08:47"""
        s = 0
        h = []
        courses.sort(key=lambda x: (x[1], -x[0]))
        for duration, lastday in courses:
            heappush(h, -duration)
            s += duration
            while s > lastday:
                s += heappop(h)
        return len(h)


@pytest.mark.parametrize('courses, expected', [
    ([[100,200],[200,1300],[1000,1250],[2000,3200]], 3),
    ([[1,2]], 1),
    ([[3,2],[4,3]], 0),
    ([[100,2],[32,50]], 1),
    ([[9,14],[7,12],[1,11],[4,7]], 3),
    ([[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]], 4),
])
def test(courses, expected):
    assert expected == Solution().scheduleCourse(courses)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
