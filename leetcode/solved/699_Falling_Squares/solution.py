#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are several squares being dropped onto the X-axis of a 2D plane.

You are given a 2D integer array positions where positions[i] = [lefti, sideLengthi] represents the ith square with a side length of sideLengthi that is dropped with its left edge aligned with X-coordinate lefti.

Each square is dropped one at a time from a height above any landed squares. It then falls downward (negative Y direction) until it either lands on the top side of another square or on the X-axis. A square brushing the left/right side of another square does not count as landing on it. Once it lands, it freezes in place and cannot be moved.

After each square is dropped, you must record the height of the current tallest stack of squares.

Return an integer array ans where ans[i] represents the height described above after dropping the ith square.

Example 1:

Input: positions = [[1,2],[2,3],[6,1]]
Output: [2,5,5]
Explanation:
After the first drop, the tallest stack is square 1 with a height of 2.
After the second drop, the tallest stack is squares 1 and 2 with a height of 5.
After the third drop, the tallest stack is still squares 1 and 2 with a height of 5.
Thus, we return an answer of [2, 5, 5].

Example 2:

Input: positions = [[100,100],[200,100]]
Output: [100,100]
Explanation:
After the first drop, the tallest stack is square 1 with a height of 100.
After the second drop, the tallest stack is either square 1 or square 2, both with heights of 100.
Thus, we return an answer of [100, 100].
Note that square 2 only brushes the right side of square 1, which does not count as landing on it.

Constraints:

	1 <= positions.length <= 1000
	1 <= lefti <= 108
	1 <= sideLengthi <= 106
"""
import bisect
import itertools
from heapq import heappop, heappush
from typing import List
import pytest
import sys


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        xs = set()
        for x, w in positions:
            xs.add(x)
            xs.add(x+w)
        segments = sorted(list(xs))

        box_segments = {}
        i = 0
        for x, w in sorted(positions):
            while i < len(segments) and segments[i] < x:
                i += 1
            j = i
            while j < len(segments) and segments[j] < x+w:
                j += 1
            box_segments[(x, w)] = [i, j]

        ret = []
        segment_heights = [0]*len(segments)
        max_so_far = 0
        for x, w in positions:
            s, e = box_segments[(x, w)]
            new_height = max(segment_heights[i] for i in range(s, e)) + w
            for i in range(s, e):
                segment_heights[i] = new_height
            max_so_far = max(max_so_far, new_height)
            ret.append(max_so_far)
        return ret

    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        """11/28/2022 18:00"""
        def query(i, s, e, l, r):
            if l <= s and e <= r:
                return heights[i]
            ret = 0
            m = s + (e-s)//2
            if l <= m:
                ret = max(ret, query(i*2+1, s, m, l, r))
            if r > m:
                ret = max(ret, query(i*2+2, m+1, e, l, r))
            return ret

        def update(i, s, e, l, r, v):
            if s == e:
                heights[i] = v
                return
            m = s + (e-s)//2
            if l <= m:
                update(i*2+1, s, m, l, r, v)
            if r > m:
                update(i*2+2, m+1, e, l, r, v)
            heights[i] = max(heights[i*2+1], heights[i*2+2])

        xs = set()
        for x, w in positions:
            xs.add(x)
            xs.add(x+w)
        segments = sorted(list(xs))
        n = len(segments)

        ret = []
        heights = [0]*(n*3)
        max_so_far = 0
        for x, w in positions:
            s = bisect.bisect_left(segments, x)
            e = bisect.bisect_left(segments, x+w)
            h = query(0, 0, n-1, s, e-1) + w
            update(0, 0, n-1, s, e-1, h)
            max_so_far = max(max_so_far, h)
            ret.append(max_so_far)
        return ret


@pytest.mark.parametrize('positions, expected', [
    ([[1,2],[2,3],[6,1]], [2,5,5]),
    ([[100,100],[200,100]], [100,100]),
    ([[6,1],[9,2],[2,4]], [1,2,4]),
    ([[9,10],[4,1],[2,1],[7,4],[6,10]], [10,10,10,14,24])
])
def test(positions, expected):
    assert expected == Solution().fallingSquares(positions)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
