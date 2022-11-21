#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

Example 1:

Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45

Example 2:

Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
Output: 16

Constraints:

	-104 <= ax1 <= ax2 <= 104
	-104 <= ay1 <= ay2 <= 104
	-104 <= bx1 <= bx2 <= 104
	-104 <= by1 <= by2 <= 104
"""
import pytest
import sys


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        """08/13/2019 20:48"""
        if A > C:
            A, C = C, A
        if B > D:
            B, D = D, B
        if E > G:
            E, G = G, E
        if F > H:
            F, H = H, F
        w1 = C-A
        h1 = D-B
        w2 = G-E
        h2 = H-F
        wi = max(0, min(C, G) - max(A, E))
        hi = max(0, min(D, H) - max(B, F))
        return w1*h1 + w2*h2 - wi*hi

    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        p1, p2, q1, q2 = (ax1, ay1), (ax2, ay2), (bx1, by1), (bx2, by2)

        def overlap(p1, p2, q1, q2):
            x1 = max(p1[0], q1[0])
            x2 = min(p2[0], q2[0])
            y1 = max(p1[1], q1[1])
            y2 = min(p2[1], q2[1])
            return max(0, x2-x1) * max(0, y2-y1)

        def area(p1, p2):
            return abs(p1[0] - p2[0]) * abs(p1[1] - p2[1])

        return area(p1, p2) + area(q1, q2) - overlap(p1, p2, q1, q2)


@pytest.mark.parametrize('ax1, ay1, ax2, ay2, bx1, by1, bx2, by2, expected', [
    (-3, 0, 3, 4, 0, -1, 9, 2, 45),
    (-2, -2, 2, 2, -2, -2, 2, 2, 16),
])
def test(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2, expected):
    assert expected == Solution().computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
