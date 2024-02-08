#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

Example 1:

Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]

Example 2:

Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

Constraints:

	1 <= nums.length <= 105
	1 <= nums[i].length <= 105
	1 <= sum(nums[i].length) <= 105
	1 <= nums[i][j] <= 105
"""
from collections import deque
from typing import List
import pytest
import sys


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """Feb 07, 2024 21:53"""
        ret = []
        queues = []

        def update(queues):
            for i in range(len(queues)-1, -1, -1):
                ret.append(queues[i].popleft())
            return [q for q in queues if q]

        for arr in nums:
            queues.append(deque(arr))
            queues = update(queues)
        while queues:
            queues = update(queues)
        return ret


@pytest.mark.parametrize('args', [
    (([[1,2,3],[4,5,6],[7,8,9]], [1,4,2,7,5,3,8,6,9])),
    (([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]], [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16])),
])
def test(args):
    assert args[-1] == Solution().findDiagonalOrder(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
