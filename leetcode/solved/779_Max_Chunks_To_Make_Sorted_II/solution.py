#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array arr.

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

Example 1:

Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.

Example 2:

Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.

Constraints:

	1 <= arr.length <= 2000
	0 <= arr[i] <= 108
"""
from typing import List
import pytest
import sys


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        N = len(arr)

        def build_minmax(arr):
            minmax = []
            for n in arr:
                if not minmax:
                    minmax.append((n, n))
                else:
                    minmax.append((
                        min(minmax[-1][0], n),
                        max(minmax[-1][1], n)))
            return minmax

        left_minmax = build_minmax(arr)
        right_minmax = build_minmax(arr[::-1])[::-1]
        splits = [N]
        sp = N
        for i in range(N-1, 0, -1):
            if left_minmax[i-1][1] <= right_minmax[i][0]:
                sp = i
            splits.append(sp)
        splits.reverse()

        ret = 0
        i = 0
        while i < N:
            j = splits[i]
            ret += 1
            i = j

        return ret

    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = [arr[0]]
        for n in arr[1:]:
            m = chunks[-1]
            while chunks and chunks[-1] > n:
                chunks.pop()
            chunks.append(max(m, n))
        return len(chunks)


@pytest.mark.parametrize('args', [
    (([5,4,3,2,1], 1)),
    (([2,1,3,4,4], 4)),
    (([4,2,2,1,1], 1)),
    (([0,3,0,3,2], 2)),
])
def test(args):
    assert args[-1] == Solution().maxChunksToSorted(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
