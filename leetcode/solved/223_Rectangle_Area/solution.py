#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
223. Rectangle Area
Medium

247

492

Favorite

Share
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.
"""
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
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


if __name__ == '__main__':
    cases = [
        [-3, 0, 3, 4, 0, -1, 9, 2]
    ]
    expecteds = [
        45
    ]
    for case, expected in zip(cases, expecteds):
        actual = Solution().computeArea(*case)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
