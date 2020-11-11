#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:

	1 <= k <= arr.length
	1 <= arr.length <= 10^4
	Absolute value of elements in the array and x will not exceed 104
"""
import sys
from heapq import heappop
from heapq import heappush
from typing import List
import pytest


def binsearch(arr, x):
    i, j = 0, len(arr)-1
    while i <= j:
        m = i + (j-i)//2
        if arr[m] < x:
            i = m+1
        else:
            j = m-1
    return i


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i, j = 0, len(arr)-k-1
        while i <= j:
            m = i + (j-i)//2
            if x-arr[m] <= arr[m+k]-x:
                j = m-1
            else:
                i = m+1
        return arr[i:i+k]

    def _findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = binsearch(arr, x)
        l, r = i - 1, i
        ret = []
        while len(ret) < k:
            if l < 0:
                ret.append(arr[r])
                r += 1
            elif r >= len(arr):
                ret.insert(0, arr[l])
                l -= 1
            elif x - arr[l] <= arr[r] - x:
                ret.insert(0, arr[l])
                l -= 1
            else:
                ret.append(arr[r])
                r += 1
        return ret


    def _findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = binsearch(arr, x)
        ret = arr[i:min(i+k, len(arr))]
        for j in range(i-1, max(-1, i-1-k), -1):
            if len(ret) < k or x - arr[j] <= ret[-1] - x:
                ret.insert(0, arr[j])
            if len(ret) > k:
                ret.pop()
        return ret

    def _findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k >= len(arr):
            return arr
        ret = []
        for n in arr:
            gap = abs(x - n)
            if len(ret) < k or gap < -ret[0][0]:
                heappush(ret, (-gap, n))
            while len(ret) > k:
                heappop(ret)
        return sorted([x[1] for x in ret])


@pytest.mark.parametrize('arr, k, x, expected', [
    ([1,2,3,4,5], 4, 3, [1,2,3,4]),
    ([1,2,3,4,5], 4, -1, [1,2,3,4]),
    ([0,0,1,2,3,3,4,7,7,8], 3, 5, [3,3,4]),
    ([1], 1, 1, [1])
])
def test(arr, k, x, expected):
    assert expected == Solution().findClosestElements(arr, k, x)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
