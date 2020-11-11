
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""
import sys
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ab_counter = defaultdict(int)
        for a in A:
            for b in B:
                ab_counter[a + b] += 1

        cd_counter = defaultdict(int)
        for c in C:
            for d in D:
                cd_counter[c + d] += 1

        ret = 0
        for k, v in ab_counter.items():
            ret += v * cd_counter.get(-k, 0)
        return ret


@pytest.mark.parametrize('A, B, C, D, expected', [
    ([1, 2], [-2,-1], [-1, 2], [ 0, 2], 2),
])
def test(A, B, C, D, expected):
    print()
    assert expected == Solution().fourSumCount(A, B, C, D)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
