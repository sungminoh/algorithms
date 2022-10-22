#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

	lefti is the x coordinate of the left edge of the ith building.
	righti is the x coordinate of the right edge of the ith building.
	heighti is the height of the ith building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

Example 1:

Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.

Example 2:

Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]

Constraints:

	1 <= buildings.length <= 104
	0 <= lefti < righti <= 231 - 1
	1 <= heighti <= 231 - 1
	buildings is sorted by lefti in non-decreasing order.
"""
from typing import List
import pytest
import sys
from heapq import heappop, heappush


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """06/14/2020 13:46"""
        buildings.sort(key=lambda x: (x[0], -x[2], x[1]))  # sort l, h, r
        heap = [(0, float('inf'))]  # -h, r
        ret = []
        for l, r, h in buildings:
            while heap[0][1] <= l:
                ph, pr = heappop(heap)
                while heap[0][0] == ph:
                    _, _pr =heappop(heap)
                    pr = max(pr, _pr)
                while heap[0][1] <= pr:
                    heappop(heap)
                if pr < l or -heap[0][0] >= h:
                    ret.append([pr, -heap[0][0]])
            if h > -heap[0][0] and (not ret or h != ret[-1][1]):
                ret.append([l, h])
            heappush(heap, (-h, r))

        while len(heap) > 1:
            ph, pr = heappop(heap)
            while heap[0][0] == ph:
                _, _pr =heappop(heap)
                pr = max(pr, _pr)
            while heap[0][1] <= pr:
                heappop(heap)
            ret.append([pr, -heap[0][0]])
        return ret

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """10/21/2022 19:50"""
        ret = []
        cur_h = 0
        hp = []  # -h, r

        def pop_before(hp, bound, cur_h):
            right_bound = -1
            while hp and hp[0][1] < bound:
                h, r = heappop(hp)
                h = -h
                if r > right_bound:
                    right_bound = r
                    while hp and hp[0][1] <= right_bound:
                        heappop(hp)
                    cur_h = 0 if not hp else -hp[0][0]
                    if h > cur_h:
                        ret.append([r, cur_h])
            return cur_h

        i = 0
        while i < len(buildings):
            cur_h = pop_before(hp, buildings[i][0], cur_h)
            cur_h = 0 if not hp else -hp[0][0]

            mh = 0
            j = i
            while j < len(buildings) and buildings[j][0] == buildings[i][0]:
                l, r, h = buildings[j]
                mh = max(mh, h)
                heappush(hp, (-h, r))
                j += 1
            if mh > cur_h:
                ret.append([l, mh])
                cur_h = mh
            i = j

        pop_before(hp, float('inf'), 0)
        return ret


@pytest.mark.parametrize('buildings, expected', [
    ([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]],
     [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]),
    ([[0,2,3],[2,5,3]],
     [[0,3],[5,0]]),
    ([[1,2,1],[1,2,2],[1,2,3]], [[1,3],[2,0]]),
    ([[0,5,7],[5,10,7],[5,10,12],[10,15,7],[15,20,7],[15,20,12],[20,25,7]], [[0,7],[5,12],[10,7],[15,12],[20,7],[25,0]]),
])
def test(buildings, expected):
    actual = Solution().getSkyline(buildings)
    print(actual)
    assert actual == sorted(actual)
    assert expected == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
