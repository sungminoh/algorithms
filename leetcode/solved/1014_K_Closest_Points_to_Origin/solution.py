#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Constraints:

	1 <= k <= points.length <= 104
	-104 < xi, yi < 104
"""
from heapq import heappop
from heapq import heappush
import random
from pathlib import Path
import json
import sys
from typing import List
import pytest


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Quick selection
        TLE due to the worst case
        """
        def dist(p):
            return p[0]**2 + p[1]**2

        def quick_select(arr, s, e, k, key=dist):
            if s == e:
                return s
            p = random.randint(s, e)
            arr[e], arr[p] = arr[p], arr[e]
            v = key(arr[e])
            i = s
            j = e-1
            while i <= j:
                if key(arr[i]) < v:
                    i += 1
                elif key(arr[j]) >= v:
                    j -= 1
                else:
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i], arr[e] = arr[e], arr[i]
            if i > k:
                return quick_select(arr, s, i-1, k)
            if i < k:
                return quick_select(arr, i+1, e, k)
            return i

        quick_select(points, 0, len(points)-1, k-1)
        return points[:k]

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Heap
        Time complexity: O(nlogk)
        Space complexity: O(k)
        """
        def dist(p):
            return p[0]**2 + p[1]**2

        heap = []
        for p in points:
            heappush(heap, (-dist(p), p))
            while len(heap) > k:
                heappop(heap)
        return [x[1] for x in heap]


@pytest.mark.parametrize('points, k, expected', [
    ([[1,3],[-2,2]], 1, [[-2,2]]),
    ([[3,3],[5,-1],[-2,4]], 2, [[3,3],[-2,4]]),
    ([[1,3],[-2,2],[2,-2]], 2, [[-2,2],[2,-2]]),
    (*json.load(open(Path(__file__).parent/'testcase.json')), []),
])
def test(points, k, expected):
    assert sorted(expected) == sorted(Solution().kClosest(points, k))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
