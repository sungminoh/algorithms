#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

	|a - x| < |b - x|, or
	|a - x| == |b - x| and a < b

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:

	1 <= k <= arr.length
	1 <= arr.length <= 104
	arr is sorted in ascending order.
	-104 <= arr[i], x <= 104
"""
from heapq import heappop
from heapq import heappush
import sys
import bisect
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
        """07/13/2020 00:00"""
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

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """07/13/2020 00:15"""
        i = binsearch(arr, x)
        ret = arr[i:min(i+k, len(arr))]
        for j in range(i-1, max(-1, i-1-k), -1):
            if len(ret) < k or x - arr[j] <= ret[-1] - x:
                ret.insert(0, arr[j])
            if len(ret) > k:
                ret.pop()
        return ret

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """07/13/2020 00:21"""
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

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """07/13/2020 00:31"""
        i, j = 0, len(arr)-k-1
        while i <= j:
            m = i + (j-i)//2
            if x-arr[m] <= arr[m+k]-x:
                j = m-1
            else:
                i = m+1
        return arr[i:i+k]

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Find the closest value and expand
        Time complexity: O(logn + k)
        Space complexity: O(1)
        """
        p = bisect.bisect_left(arr, x)
        i, j = p-1, p
        while j-i <= k:
            if j == len(arr) or (i >= 0 and x - arr[i] <= arr[j] - x):
                i -= 1
            elif i < 0 or (j < len(arr) and x - arr[i] > arr[j] - x):
                j += 1
            else:
                break
        return arr[i+1:j]

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Find start position by bineray search
        Time complexity: O(logn)
        Space complexity: O(1)
        """
        l, r = 0, len(arr)-k
        while l < r:
             m = l + (r-l)//2
             if x-arr[m] <= arr[m+k]-x:
                 r = m
             else:
                 l = m+1
        return arr[l:l+k]


@pytest.mark.parametrize('arr, k, x, expected', [
    ([1,2,3,4,5], 4, 3, [1,2,3,4]),
    ([1,2,3,4,5], 4, -1, [1,2,3,4]),
    ([0,1,1,1,2,3,6,7,8,9], 9, 4, [0,1,1,1,2,3,6,7,8]),
])
def test(arr, k, x, expected):
    assert expected == Solution().findClosestElements(arr, k, x)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
