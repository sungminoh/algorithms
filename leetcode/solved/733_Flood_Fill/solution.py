
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on.  Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:

Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

Note:
The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0  and 0 .
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""
import sys
from typing import List
import pytest


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image or not image[0]:
            return image

        def neighbor(i, j):
            if i > 0:
                yield i - 1, j
            if j > 0:
                yield i, j - 1
            if i < len(image) - 1:
                yield i + 1, j
            if j < len(image[0]) - 1:
                yield i, j + 1

        stack = [(sr, sc)]
        c = image[sr][sc]
        while stack:
            i, j = stack.pop()
            image[i][j] = newColor
            for _i, _j in neighbor(i, j):
                if image[_i][_j] == c and image[_i][_j] != newColor:
                    stack.append((_i, _j))
        return image


@pytest.mark.parametrize('image, sr, sc, newColor, expected', [
    ([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2, [[2,2,2],[2,2,0],[2,0,1]]),
    ([[0,0,0],[0,1,1]], 1, 1, 1, [[0,0,0],[0,1,1]])
])
def test(image, sr, sc, newColor, expected):
    assert expected == Solution().floodFill(image, sr, sc, newColor)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
