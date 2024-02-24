import itertools
from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

Example 1:

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.

Example 2:

Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

Example 3:

Input: nums = [3,9,6], k = 2
Output: 1

Constraints:

	1 <= nums.length <= 105
	1 <= nums[i] <= 105
	1 <= k <= 105
"""
import pytest
import sys


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """Feb 24, 2024 14:11
        Binary Search O(nlogn)
        """
        nums.sort()
        cumsum = list(itertools.accumulate(nums))

        def required(s, e):
            bar = (e-s+1) * nums[e]
            cur = cumsum[e] - (cumsum[s-1] if s>0 else 0)
            return bar-cur

        def bisearch(s, e):
            _e = e
            while s <= e:
                m = s + (e-s)//2
                if required(m, _e) <= k:
                    e = m-1
                else:
                    s = m+1
            return e+1

        ret = 0
        for i in range(len(nums)):
            j = bisearch(0, i)
            ret = max(ret, i-j+1)
        return ret

    def maxFrequency(self, nums: List[int], k: int) -> int:
        """Feb 24, 2024 14:15
        Two Pointer O(n)
        """
        nums.sort()
        acc = 0
        j = 0
        ret = 1
        for i, n in enumerate(nums):
            acc += n
            while j < i and acc+k < (i-j+1)*n:
                acc -= nums[j]
                j += 1
            ret = max(ret, i-j+1)
        return ret




@pytest.mark.parametrize('args', [
    (([1,2,4], 5, 3)),
    (([1,4,8,13], 5, 2)),
    (([3,9,6], 2, 1)),
    (([9954,9937,9948,9997,9995,9943,9949,9960,9930,9960,9979,9976,9967,9970,9968,9910,9928,9916,9919,9938,9961,9929,9975,9955,9951,9900,9936,9984,9998,9925,9904,9951,9929,9907,9958,9987,9918,9909,9936,9973,9906,9903,9908,9993,9917,9988,9956,9992,9997,9979,9996,9960,9921,9909,9948,9900,9916,9984,9929,9971,9941,9978,9923,9917,9948,9959,9951,9983,9979,9989,9971,9999,9906,9965,9934,9952,9936,9938,9932,9999,9901,9979,9920,9966,9964,9964,9939,9988,9933,9911,9915,9996,9913,9945,9939,9977,9991,9967,9980,9986,9988,9985,9959,9983,9932,9982,9969,9998,9940,9961,9981,9954,9920,9979,9992,9963,9907,9930,9954,9913,9945,9965,9926,9973,9980,9986,9929,9998,9953,9953,9944,9949,9949,9949,9980,9990,9922,9924,9956,9982,9951,9969,9908,9964,9981,9961,9982,9997,9929,9947,9917,9964,9902,9971,9925,9997,9901,9931,9908,9955,9901,9927,9934,9964,9927,9908,9910,9983,9994,9996,9946,9923,9918,9960,9900,9911,9989,9991,9976,9919,9935,9953,9944,9954,9969,9991,9954,9949,9995,10000,9901,9965,9946,9972,9980,9961,9948,9960,9964,9963,9940,9922,9937,9999,9924,9903,9921,9956,9997,9979], 2541, 110)),
])
def test(args):
    assert args[-1] == Solution().maxFrequency(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
