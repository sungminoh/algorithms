
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.

Example 1:

Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation:
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}

Note:
	1. N is an integer within the range [1, 20,000].
	2. The elements of A are all distinct.
	3. Each element of A is an integer within the range [0, N-1].
"""
import sys
from typing import List
import pytest


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        pool = set(nums)

        def iterate(n):
            cnt = 0
            while n in pool:
                pool.remove(n)
                cnt += 1
                n = nums[n]
            return cnt

        m = 1
        for n in nums:
            m = max(m, iterate(n))
        return m


@pytest.mark.parametrize('nums, expected', [
    ([5,4,0,3,1,6,2], 4),
])
def test(nums, expected):
    assert expected == Solution().arrayNesting(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
