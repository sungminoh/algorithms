
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

Note:

The total number of elements of the given matrix will not exceed 10,000.
"""
import sys
from typing import List
import pytest


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        ret = []
        n, m = len(matrix) - 1, len(matrix[0]) - 1
        for i in range(n + m + 1):  # 0 ~ n-1 + m-1
            if i % 2 == 0:
                for x in range(max(0, i - n), min(m, i) + 1):
                    y = i - x
                    ret.append(matrix[y][x])
            else:
                for x in range(min(m, i), max(0, i - n) - 1, -1):
                    y = i - x
                    ret.append(matrix[y][x])
        return ret


@pytest.mark.parametrize('matrix, expected', [
    ([[ 1, 2, 3 ],
      [ 4, 5, 6 ],
      [ 7, 8, 9 ]], [1,2,4,7,5,3,6,8,9]),
])
def test(matrix, expected):
    assert expected == Solution().findDiagonalOrder(matrix)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
