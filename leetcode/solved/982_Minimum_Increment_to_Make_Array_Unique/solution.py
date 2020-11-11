
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.

Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].

Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

Note:
    1. 0 <= A.length <= 40000
    2. 0 <= A[i] < 40000
"""
import sys
from typing import List
import pytest


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        A = sorted(A)
        visited = set([A[0]])
        m = A[0]
        cnt = 0
        for a in A[1:]:
            if a <= m:
                m += 1
                cnt += m - a
            else:
                m = a
        return cnt


@pytest.mark.parametrize('A, expected', [
    ([1,2,2], 1),
    ([3,2,1,2,1,7], 6),
])
def test(A, expected):
    assert expected == Solution().minIncrementForUnique(A)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
