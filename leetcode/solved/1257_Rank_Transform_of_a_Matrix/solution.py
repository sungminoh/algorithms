#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].

The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:

	The rank is an integer starting from 1.
	If two elements p and q are in the same row or column, then:

		If p < q then rank(p) < rank(q)
		If p == q then rank(p) == rank(q)
		If p > q then rank(p) > rank(q)

	The rank should be as small as possible.

It is guaranteed that answer is unique under the given rules.

Example 1:

Input: matrix = [[1,2],[3,4]]
Output: [[1,2],[2,3]]
Explanation:
The rank of matrix[0][0] is 1 because it is the smallest integer in its row and column.
The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and matrix[0][0] is rank 1.
The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and matrix[0][0] is rank 1.
The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1], matrix[1][1] > matrix[1][0], and both matrix[0][1] and matrix[1][0] are rank 2.

Example 2:

Input: matrix = [[7,7],[7,7]]
Output: [[1,1],[1,1]]

Example 3:

Input: matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
Output: [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]

Example 4:

Input: matrix = [[7,3,6],[1,4,5],[9,8,2]]
Output: [[5,1,4],[1,2,3],[6,3,1]]

Constraints:

	m == matrix.length
	n == matrix[i].length
	1 <= m, n <= 500
	-109 <= matrix[row][col] <= 109
"""
import sys
import bisect
from collections import defaultdict
import copy
import itertools
from typing import List
import pytest


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        """ Union-find
        Time compplexity: O(m*n*log(mn))
        Space compplexity: O(m*n)
        """
        positions = defaultdict(set)
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                positions[matrix[i][j]].add((i, j))

        ret = [[0]*n for _ in range(m)]
        # max rank of each row and column
        rowm = [0]*m
        colm = [0]*n

        def find(arr, i):
            if arr[i] != i:
                arr[i] = find(arr, arr[i])
            return arr[i]

        # assign rank from the samllest value
        for v in sorted(positions.keys()):
            # if either column or row is the same, they are in the same group.
            #  thus, they are going to have the same rank
            groups = list(range(m+n))
            for i, j in positions[v]:
                gi = find(groups, i)
                gj = find(groups, m+j)
                groups[gi] = groups[gj] = min(gi, gj)

            # iterate positions of each group
            group_positions = defaultdict(set)
            for i, j in positions[v]:
                group_positions[find(groups, i)].add((i, j))
            for g, poss in group_positions.items():
                # each group's rank should be 1 larger than max rank of any
                #  row or column of any positions
                rank = max(max(rowm[i], colm[j]) for i, j in poss) + 1
                for i, j in poss:
                    rowm[i] = colm[j] = rank
                    ret[i][j] = rank

        return ret


@pytest.mark.parametrize('matrix, expected', [
    ([[1,2],[3,4]], [[1,2],[2,3]]),
    ([[7,7],[7,7]], [[1,1],[1,1]]),
    ([[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]], [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]),
    ([[7,3,6],[1,4,5],[9,8,2]], [[5,1,4],[1,2,3],[6,3,1]]),
])
def test(matrix, expected):
    print()
    actual = Solution().matrixRankTransform(matrix)
    for row in actual:
        print(row)
    assert expected == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
