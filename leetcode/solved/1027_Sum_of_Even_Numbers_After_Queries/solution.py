#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array nums and an array queries where queries[i] = [vali, indexi].

For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the even values of nums.

Return an integer array answer where answer[i] is the answer to the ith query.

Example 1:

Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation: At the beginning, the array is [1,2,3,4].
After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.

Example 2:

Input: nums = [1], queries = [[4,0]]
Output: [0]

Constraints:

	1 <= nums.length <= 104
	-104 <= nums[i] <= 104
	1 <= queries.length <= 104
	-104 <= vali <= 104
	0 <= indexi < nums.length
"""
from typing import List
import pytest
import sys


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for n in nums:
            if n%2 == 0:
                even_sum += n

        ret = []
        for v, i in queries:
            if nums[i]%2 == 0:
                even_sum -= nums[i]
            nums[i] += v
            if nums[i]%2 == 0:
                even_sum += nums[i]
            ret.append(even_sum)
        return ret


@pytest.mark.parametrize('nums, queries, expected', [
    ([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]], [8,6,2,4]),
    ([1], [[4,0]], [0]),
])
def test(nums, queries, expected):
    assert expected == Solution().sumEvenAfterQueries(nums, queries)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
