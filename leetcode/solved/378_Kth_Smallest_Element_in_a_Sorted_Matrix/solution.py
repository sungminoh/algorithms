
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

Note:
You may assume k is always valid, 1 &le; k &le; n2.
"""
from typing import List
import pytest


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            # not found
            return
        if k == 1:
            return matrix[0][0]
        if k == len(matrix) ** 2:
            return matrix[-1][-1]

        def cnt(n, key=lambda n, e: e < n):
            cnt = 0
            c = len(matrix) - 1
            for row in matrix:
                while c >= 0 and not key(n, row[c]):
                    c -= 1
                cnt += c + 1
                if c < 0:
                    break
            return cnt

        l, r = matrix[0][0], matrix[-1][-1]
        while l <= r:
            m = l + (r - l) // 2
            cnt_smaller = cnt(m, lambda n, e: e < n)
            cnt_smaller_or_equal_to = cnt(m, lambda n, e: e <= n)
            if k <= cnt_smaller:
                r = m - 1
            elif k > cnt_smaller_or_equal_to:
                l = m + 1
            else:
                return m
        # not found
        return None


@pytest.mark.parametrize('matrix, k,expected', [
    ([[ 1,  5,  9],
      [10, 11, 13],
      [12, 13, 15]],
     8, 13),
])
def test(matrix, k, expected):
    assert expected == Solution().kthSmallest(matrix, k)
