#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

Constraints:

	1 <= nums.length <= 5 * 104
	-5 * 104 <= nums[i] <= 5 * 104
"""
from heapq import heapify, heappop
from typing import List
import pytest
import sys


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """Apr 02, 2023 19:37
        TLE"""
        def quicksort(i, j):
            if i >= j:
                return
            s = i
            e = j-1
            while s <= e:
                if nums[s]<=nums[j]:
                    s += 1
                elif nums[e]>nums[j]:
                    e -= 1
                else:
                    nums[s], nums[e] = nums[e], nums[s]
                    s += 1
                    e -= 1
            nums[s], nums[j] = nums[j], nums[s]
            quicksort(i, s-1)
            quicksort(s+1, j)

        quicksort(0, len(nums)-1)
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        """Apr 02, 2023 19:39"""
        heapify(nums)
        ret = []
        while nums:
            ret.append(heappop(nums))
        return ret


@pytest.mark.parametrize('args', [
    (([5,2,3,1], [1,2,3,5])),
    (([5,1,1,2,0,0], [0,0,1,1,2,5])),
    (([3,-1], [-1,3])),
    (([-1,2,-8,-10], [-10,-8,-1,2])),
])
def test(args):
    assert args[-1] == Solution().sortArray(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
