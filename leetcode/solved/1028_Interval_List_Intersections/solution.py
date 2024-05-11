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

Constraints:

	0 <= firstList.length, secondList.length <= 1000
	firstList.length + secondList.length >= 1
	0 <= starti < endi <= 109
	endi < starti+1
	0 <= startj < endj <= 109
	endj < startj+1
"""
import heapq
from collections import deque
from typing import List
import pytest
import sys


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """Dec 03, 2021 22:31"""
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
        """Dec 03, 2021 22:36"""
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

    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """May 05, 2024 14:05"""
        ret = []
        start_max_heap = []
        end_min_heap = []

        def insert(queue):
            s, e = queue.popleft()
            heapq.heappush(start_max_heap, (-s, len(queue), queue))
            heapq.heappush(end_min_heap, (e, len(queue), queue))

        queues = [deque(firstList), deque(secondList)]
        for q in queues:
            if q:
                insert(q)
            else:
                return ret

        while end_min_heap and start_max_heap:
            # clean up
            if start_max_heap and start_max_heap[0][1] != len(start_max_heap[0][2]):
                heapq.heappop(start_max_heap)
            # discard if no overlap
            elif end_min_heap[0][0] < -start_max_heap[0][0]:
                assert len(start_max_heap) > 0
                _, l, q = heapq.heappop(end_min_heap)
                if l == len(q):
                    if len(q) > 0:
                        insert(q)
                    else:
                        break
            else:
                e, l, q = heapq.heappop(end_min_heap)
                if l == len(q):
                    ret.append([-start_max_heap[0][0], e])
                    if len(q) > 0:
                        insert(q)
                    else:
                        break
        return ret


@pytest.mark.parametrize('args', [
    (([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]], [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]])),
    (([[1,3],[5,9]], [], [])),
    (([], [[4,8],[10,12]], [])),
    (([[1,7]], [[3,10]], [[3,7]])),
])
def test(args):
    assert args[-1] == Solution().intervalIntersection(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
