#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

Note:

	arr will have length in range [1, 10].
	arr[i] will be a permutation of [0, 1, ..., arr.length - 1].
"""
import sys
from typing import List
import pytest


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)
        min_from_right = [float('inf')] * (len(arr)+1)
        for i in range(len(arr)-1, -1, -1):
            min_from_right[i] = min(min_from_right[i+1], arr[i])
        cnt = 0
        m = -float('inf')
        for i in range(len(arr)):
            m = max(m, arr[i])
            if m <= min_from_right[i+1]:
                cnt += 1
                m = -float('inf')
        return cnt


@pytest.mark.parametrize('arr, expected', [
    ([4,3,2,1,0], 1),
    ([1,0,2,3,4], 4),
    ([0], 1),
    ([0,1], 2),
    ([0,2,1], 2)
])
def test(arr, expected):
    assert expected == Solution().maxChunksToSorted(arr)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
