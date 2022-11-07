#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.

Return the largest possible overlap.

Example 1:

Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.

The number of positions that have a 1 in both images is 3 (shown in red).

Example 2:

Input: img1 = [[1]], img2 = [[1]]
Output: 1

Example 3:

Input: img1 = [[0]], img2 = [[0]]
Output: 0

Constraints:

	n == img1.length == img1[i].length
	n == img2.length == img2[i].length
	1 <= n <= 30
	img1[i][j] is either 0 or 1.
	img2[i][j] is either 0 or 1.
"""
from collections import defaultdict
from typing import List
import pytest
import sys


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        """09/20/2020 11:42"""
        n = len(img1)

        def count(i, j):
            ret = 0
            x1 = abs(min(i, 0))
            y1 = abs(min(j, 0))
            x2 = max(i, 0)
            y2 = max(j, 0)
            for dx in range(min(n-x1, n-x2)):
                for dy in range(min(n-y1, n-y2)):
                    ret += img1[x1+dx][y1+dy] & img2[x2+dx][y2+dy]
            return ret

        m = 0
        for i in range(-n+1, n):
            for j in range(-n+1, n):
                m = max(m, count(i, j))
        return m

    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        """09/20/2020 11:53"""
        n = len(img1)
        m1 = set((x, y) for x in range(n) for y in range(n) if img1[x][y] == 1)
        m2 = set((x, y) for x in range(n) for y in range(n) if img2[x][y] == 1)
        cnt = defaultdict(int)
        for x1, y1 in m1:
            for x2, y2 in m2:
                cnt[x1-x2, y1-y2] += 1
        return max(cnt.values()) if cnt.values() else 0

    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        """
        11/06/2022 15:30
        TLE
        """
        m1, n1 = len(img1), len(img2[0])
        m2, n2 = len(img2), len(img2[0])
        ret = 0
        for i in range(1, m1+m2):
            for j in range(1, n1+n2):
                cnt = 0
                for x in range(min(i, m1, m2, m1+m2-i)):
                    x1 = max(0, m1-i)+x
                    x2 = max(0, i-max(m1, m2))+x
                    for y in range(min(j, n1, n2, n1+n2-j)):
                        y1 = max(0, n1-j)+y
                        y2 = max(0, j-max(n1, n2))+y
                        if 1 == img1[x1][y1] \
                                == img2[x2][y2]:
                            cnt += 1
                ret = max(ret, cnt)
        return ret


@pytest.mark.parametrize('img1, img2, expected', [
    ([[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]], 3),
    ([[1]], [[1]], 1),
    ([[0]], [[0]], 0),
    ([[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
     [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0]],
     1),
    ([[1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1,1,0,1,1,0,0,0,1,0],[0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0],[0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,1,1,0,0,0,0,0,1,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1],[0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,1,1,0,1],[0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,1,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,0,0,0,0],[0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0],[1,1,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,1,0,1,0,1,1,0,0],[0,1,0,0,0,0,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,0,0,1],[0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0],[0,0,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0],[0,1,0,0,1,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0,0,1,0,1,0],[0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0],[0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0],[0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],[0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0]],
     [[0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0],[0,1,1,0,0,0,0,0,1,1,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0],[0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,1,0,0,1,1,0,0],[0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0],[0,0,1,1,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,1,0,1,1,0,1],[0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[1,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0],[0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0],[1,0,1,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,1,0,0],[1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1],[0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1,1,0,0],[1,0,1,1,0,1,1,0,0,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0],[0,0,0,0,0,1,0,1,1,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0],[1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,0,0],[0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0],[0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,1,0,1],[1,0,0,1,0,0,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1],[0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1],[1,0,0,0,1,0,0,0,0,1,1,1,0,1,0,1,1,0,1,0,0,0,0,0,0],[0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1],[0,0,1,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0],[0,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0],[0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,0,1,0,1,1,0,0,0],[0,0,0,0,1,1,0,0,1,1,0,1,1,0,0,0,1,1,0,0,0,0,1,1,0]],
     58),
    ([[0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0],[0,1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0],[1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0],[1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,1,0,1,0,0,0],[1,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0],[1,0,0,1,0,0,0,1,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,0],[1,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,1,1,1,0,0,1,0],[0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0],[1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],[1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,1,1,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],[1,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1],[1,0,1,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0],[0,0,1,0,0,1,0,0,0,1,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,1,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0]],
     [[0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,0,0,1],[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,0,1],[1,1,0,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1],[1,1,1,1,0,1,1,1,1,1,0,0,1,1,1,0,1,1,0,1,0,0,1,1,1],[1,1,0,0,1,0,1,1,1,0,0,1,1,0,1,0,0,0,1,1,0,0,1,0,1],[0,1,1,1,1,0,1,0,0,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,1],[1,1,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1],[1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1],[0,0,1,1,1,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,0,1],[1,1,0,1,1,1,1,0,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,0,1,0,1,1],[0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,1,0,0,1,1,1],[1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,1,0,1,1,1,1,0,0,1,1],[1,0,1,1,1,1,0,0,1,1,0,1,1,1,0,0,0,1,0,1,1,1,1,0,1],[1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0],[1,1,1,1,0,0,0,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,0],[0,1,1,0,1,1,1,0,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],[1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,0,1,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1],[1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,0,1,0],[1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,1,0,1,1,0,0,1,1,1,1],[1,1,0,1,1,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1],[0,0,1,1,1,0,1,1,1,1,0,0,0,0,1,1,0,1,0,1,0,1,0,1,1],[0,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,0,1,0,0,1],[1,1,0,1,1,1,0,1,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1]],
     113),
])
def test(img1, img2, expected):
    assert expected == Solution().largestOverlap(img1, img2)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
