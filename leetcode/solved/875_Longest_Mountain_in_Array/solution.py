#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

	B.length >= 3
	There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1]  B[i+1] > ... > B[B.length - 1]

(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.

Note:

	0 <= A.length <= 10000
	0 <= A[i] <= 10000

Follow up:

	Can you solve it using only one pass?
	Can you solve it in O(1) space?
"""
import sys
from typing import List
import pytest


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        # 0: increase, 1: decrese
        mode = 0
        cnt = 0
        ret = 0
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                if mode == 1:
                    mode = 0
                    cnt = 0
                cnt += 1
            elif A[i] < A[i-1]:
                if mode == 0:
                    mode = 1
                if cnt > 0:
                    cnt += 1
                    ret = max(ret, cnt)
            else:
                mode = 0
                cnt = 0
        else:
            if mode == 1:
                ret = max(ret, cnt)
        return ret + 1 if ret > 0 else 0

    def _longestMountain(self, A: List[int]) -> int:
        inc = [0] * len(A)
        dec = [0] * len(A)
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                inc[i] = inc[i-1] + 1
        for i in range(len(A)-2, -1, -1):
            if A[i] > A[i+1]:
                dec[i] = dec[i+1] + 1

        ret = 0
        for i, d in zip(inc, dec):
            if i > 0 and d > 0:
                ret = max(ret, i+d+1)
        return ret


@pytest.mark.parametrize('A, expected', [
    ([2,1,4,7,3,2,5], 5),
    ([2,2,2], 0),
    ([], 0),
    ([2,3], 0),
    ([0,0,1,0,0,1,1,1,1,1], 3)
])
def test(A, expected):
    assert expected == Solution().longestMountain(A)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
