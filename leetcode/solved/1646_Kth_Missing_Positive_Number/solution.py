#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

Constraints:

	1 <= arr.length <= 1000
	1 <= arr[i] <= 1000
	1 <= k <= 1000
	arr[i] < arr[j] for 1 <= i < j <= arr.length

Follow up:

Could you solve this problem in less than O(n) complexity?
"""
from typing import List
import pytest
import sys


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """Apr 04, 2023 23:35"""
        cur = 0
        missing = 0
        for n in arr:
            missing += n-cur-1
            cur = n
            if missing >= k:
                return cur-1-(missing-k)
        return cur + (k-missing)

    def findKthPositive(self, arr: List[int], k: int) -> int:
        """Apr 04, 2023 23:54"""
        l, r = 0, len(arr)-1
        while l <= r:
            m = l + (r-l)//2
            if arr[m]-1 - m < k:
                l = m+1
            else:
                r = m-1
        r += 1
        # missing = arr[r]-1-r
        # return arr[r]-1-(missing-k)
        return r+k


@pytest.mark.parametrize('args', [
    (([2,3,4,7,11], 5, 9)),
    (([1,2,3,4], 2, 6)),
])
def test(args):
    assert args[-1] == Solution().findKthPositive(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
