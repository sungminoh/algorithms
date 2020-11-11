#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.  (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  It is guaranteed that the given input always makes it possible.

Example:
Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation:
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.

Note:

	A, B are arrays with the same length, and that length will be in the range [1, 1000].
	A[i], B[i] are integer values in the range [0, 2000].
"""
import sys
from typing import List
import pytest


class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        if not A or not B:
            return 0
        # nonswap, swap
        cnt = (0, 1)
        for i in range(1, len(A)):
            nonswap_cnt = []
            swap_cnt = []
            if A[i] > A[i-1] and B[i] > B[i-1]:
                # prev nonswap -> cur nonswap
                nonswap_cnt.append(cnt[0])
                # prev swap -> cur swap
                swap_cnt.append(cnt[1] + 1)
            if A[i] > B[i-1] and B[i] > A[i-1]:
                # prev swap -> cur nonswap
                nonswap_cnt.append(cnt[1])
                # prev nonswap -> cur swap
                swap_cnt.append(cnt[0]+1)
            cnt = (min(nonswap_cnt), min(swap_cnt))
        return min(cnt)


@pytest.mark.parametrize('A, B, expected', [
    ([1,3,5,4], [1,2,3,7], 1),
])
def test(A, B, expected):
    assert expected == Solution().minSwap(A, B)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
