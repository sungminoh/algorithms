
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic. 1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0

A slice (P, Q) of array A is called arithmetic if the sequence:
    A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1

The function should return the number of arithmetic slices in the array A.

Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
"""
from typing import List
import pytest


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        count_all_ends_with = [0] * len(A)
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                count_all_ends_with[i] = count_all_ends_with[i - 1] + 1
        return sum(count_all_ends_with)

    def _numberOfArithmeticSlices(self, A: List[int]) -> int:
        def count_all_ends_with(i):
            ret = 0
            diff = A[i - 1] - A[i]
            for j in range(i - 1, 0, -1):
                if A[j - 1] - A[j] == diff:
                    ret += 1
                else:
                    return ret
            return ret

        ret = 0
        for i in range(2, len(A)):
            ret += count_all_ends_with(i)
        return ret


@pytest.mark.parametrize('A, expected', [
    ([1,2,3,4], 3),
    ([1,2,3,8,9,10], 2)
])
def test(A, expected):
    assert expected == Solution().numberOfArithmeticSlices(A)
