#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Example 1:

Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []

Example 3:

Input: firstList = [], secondList = [[4,8],[10,12]]
Output: []

Example 4:

Input: firstList = [[1,7]], secondList = [[3,10]]
Output: [[3,7]]

Constraints:

	0 <= firstList.length, secondList.length <= 1000
	firstList.length + secondList.length >= 1
	0 <= starti < endi <= 109
	endi < starti+1
	0 <= startj < endj <= 109
	endj < startj+1
"""
import sys
from typing import List
import pytest


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ret = []
        i, j = 0, 0
        is_open = [False, False]
        while i < len(firstList) and j < len(secondList):
            if not any(is_open):
                if firstList[i][0] < secondList[j][0]:
                    is_open[0] = True
                elif firstList[i][0] > secondList[j][0]:
                    is_open[1] = True
                else:
                    is_open[0] = is_open[1] = True
            elif all(is_open):
                open_from = max(firstList[i][0], secondList[j][0])
                if firstList[i][1] < secondList[j][1]:
                    is_open[0] = False
                    ret.append([open_from, firstList[i][1]])
                    i += 1
                elif firstList[i][1] > secondList[j][1]:
                    is_open[1] = False
                    ret.append([open_from, secondList[j][1]])
                    j += 1
                else:
                    is_open[0] = is_open[1] = False
                    ret.append([open_from, firstList[i][1]])
                    i += 1
                    j += 1
            elif is_open[0]:
                if firstList[i][1] >= secondList[j][0]:
                    is_open[1] = True
                else:
                    is_open[0] = False
                    i += 1
            elif is_open[1]:
                if firstList[i][0] <= secondList[j][1]:
                    is_open[0] = True
                else:
                    is_open[1] = False
                    j += 1
        return ret

    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ret = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            if firstList[i][1] < secondList[j][0]:
                i += 1
            elif firstList[i][0] > secondList[j][1]:
                j += 1
            else:
                ret.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
                if firstList[i][1] < secondList[j][1]:
                    i += 1
                else:
                    j += 1
        return ret


@pytest.mark.parametrize('firstList, secondList, expected', [
    ([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]], [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]),
    ([[1,3],[5,9]], [], []),
    ([], [[4,8],[10,12]], []),
    ([[1,7]], [[3,10]], [[3,7]]),
])
def test(firstList, secondList, expected):
    assert expected == Solution().intervalIntersection(firstList, secondList)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
