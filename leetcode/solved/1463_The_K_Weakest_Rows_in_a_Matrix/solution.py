#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

	The number of soldiers in row i is less than the number of soldiers in row j.
	Both rows have the same number of soldiers and i < j.

Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Example 1:

Input: mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3
Output: [2,0,3]
Explanation:
The number of soldiers in each row is:
- Row 0: 2
- Row 1: 4
- Row 2: 1
- Row 3: 2
- Row 4: 5
The rows ordered from weakest to strongest are [2,0,3,1,4].

Example 2:

Input: mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2
Output: [0,2]
Explanation:
The number of soldiers in each row is:
- Row 0: 1
- Row 1: 4
- Row 2: 1
- Row 3: 1
The rows ordered from weakest to strongest are [0,2,3,1].

Constraints:

	m == mat.length
	n == mat[i].length
	2 <= n, m <= 100
	1 <= k <= m
	matrix[i][j] is either 0 or 1.
"""
import sys
from heapq import heappop
from heapq import heappush
import operator
from typing import List
import pytest


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """
        Time complexity: O(n*logm*logk)
        Space complexity: O(k)
        """
        def bisearch(arr, x, func=operator.lt):
            l, r = 0, len(arr)-1
            while l <= r:
                m = l + (r-l)//2
                if func(arr[m], x):
                    l = m+1
                else:
                    r = m-1
            return l

        h = []  # (-num_ones, -row_index)
        for i, row in enumerate(mat):
            num_ones = bisearch(row, 0, func=operator.gt)
            if len(h)<k or num_ones < -h[0][0]:
                heappush(h, (-num_ones, -i))
            while len(h)>k:
                heappop(h)

        ret = []
        while h:
            ret.append(-heappop(h)[1])
        return ret[::-1]


@pytest.mark.parametrize('mat, k, expected', [
    ([[1,1,0,0,0],
      [1,1,1,1,0],
      [1,0,0,0,0],
      [1,1,0,0,0],
      [1,1,1,1,1]], 3, [2,0,3]),
    ([[1,0,0,0],
      [1,1,1,1],
      [1,0,0,0],
      [1,0,0,0]], 2, [0,2]),
])
def test(mat, k, expected):
    assert expected == Solution().kWeakestRows(mat, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
