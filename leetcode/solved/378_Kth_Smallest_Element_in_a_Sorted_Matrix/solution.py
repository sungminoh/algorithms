#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:

Input: matrix = [[-5]], k = 1
Output: -5

Constraints:

	n == matrix.length
	n == matrix[i].length
	1 <= n <= 300
	-109 <= matrix[i][j] <= 109
	All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
	1 <= k <= n2
"""
import bisect
import sys
import itertools
from typing import List
import pytest


def quick_select(arr, k):
    def rec(s, e, k):
        p = arr[e]
        i = s
        j = e-1
        while i <= j:
            if arr[i] <= p:
                i += 1
            elif arr[j] > p:
                j -= 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
        arr[i], arr[e] = arr[e], arr[i]
        if i > k-1:
            return rec(s, i-1, k)
        elif i < k-1:
            return rec(i+1, e, k)
        return arr[i]
    return rec(0, len(arr)-1, k)


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """04/13/2020 20:00"""
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

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Quick select
        Time complexity: O(n*n) (average)
        Space complexity: O(n*n) (to make a list)
        """
        return quick_select(list(itertools.chain(*matrix)), k)

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Binary search on the value
        Time complexity: O(max-min)
        Space complexity: O(1)
        """
        l = matrix[0][0]
        h = matrix[-1][-1]
        while l < h:
            m = l + (h-l)//2
            smaller_cnt = sum(bisect.bisect_right(row, m) for row in matrix)
            if smaller_cnt < k:
                l = m+1
            else:
                h = m
        return l


@pytest.mark.parametrize('arr, k, expected', [
    ([[1,5,9],[10,11,13],[12,13,15]], 8, 13),
    ([[-5]], 1, -5),
    ([[1,1,1],[1,1,1],[10,10,10]], 7, 10)
])
def test(arr, k, expected):
    assert expected == Solution().kthSmallest(arr, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
