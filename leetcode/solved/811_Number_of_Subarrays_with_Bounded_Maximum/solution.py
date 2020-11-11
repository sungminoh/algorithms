#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We are given an array A of positive integers, and two positive integers L and R (L <= R).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.

Example :
Input:
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

Note:

	L, R  and A[i] will be an integer in the range [0, 10^9].
	The length of A will be in the range of [1, 50000].
"""
import sys
from typing import List
import pytest


class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        cnt = 0
        p = -1
        s = -1
        for i, n in enumerate(A):
            if n > R:
                if p >= 0:
                    cnt += (i-p-1)*(p-s)
                s = i
                p = -1
            elif L <= n <= R:
                if p >= 0:
                    cnt += (i-p-1)*(p-s)
                cnt += i-s
                p = i
        if p >= 0:
            cnt += (len(A)-p-1)*(p-s)
        return cnt


@pytest.mark.parametrize('A, L, R, expected', [
    ([2,1,4,3], 2, 3, 3),
    ([73,55,36,5,55,14,9,7,72,52], 32, 69, 22),
])
def test(A, L, R, expected):
    assert expected == Solution().numSubarrayBoundedMax(A, L, R)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
