
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:

Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; The number 2 can't find next greater number; The second 1's next greater number needs to search circularly, which is also 2.

Note:
The length of given array won't exceed 10000.
"""
import sys
from typing import List
import pytest


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ret = [None] * len(nums)
        stack = []
        for j in range(len(nums) * 2):
            i = j % len(nums)
            n = nums[i]
            while stack and stack[-1][1] < n:
                idx, num = stack.pop()
                if ret[idx] is None:
                    ret[idx] = n
            if ret[i] is None:
                stack.append((i, n))
        while stack:
            i, n = stack.pop()
            ret[i] = -1
        return ret


@pytest.mark.parametrize('nums, expected', [
    ([1,2,1], [2,-1,2]),
])
def test(nums, expected):
    assert expected == Solution().nextGreaterElements(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
