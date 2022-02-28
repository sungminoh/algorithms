#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

	If the element is even, divide it by 2.

		For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].

	If the element is odd, multiply it by 2.

		For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].

The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

Example 1:

Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.

Example 2:

Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.

Example 3:

Input: nums = [2,10,8]
Output: 3

Constraints:

	n == nums.length
	2 <= n <= 105
	1 <= nums[i] <= 109
"""
from heapq import heappush
from heapq import heappop
from heapq import heapify
from pathlib import Path
import json
import sys
from typing import List
import pytest


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        def possibles(n):
            yield n
            if n%2 == 1:
                yield 2*n
            else:
                while n%2 == 0:
                    n //= 2
                    yield n

        # keep possible min max boundaries
        queue = [(n, n) for n in possibles(nums[0])]

        for n in nums[1:]:
            new_queue = []
            for mn, mx in queue:
                _mn = -float('inf')
                _mx = float('inf')
                for m in possibles(n):
                    if mn <= m <= mx:
                        # if new value is between [mn, mx],
                        # no need to consider other variance of n
                        new_queue.append((mn, mx))
                        break
                    elif m < mn:
                        _mn = max(_mn, m)
                    elif m > mx:
                        _mx = min(_mx, m)
                else:  # only if the for loop did not break
                    if _mn != -float('inf'):
                        # if new lower bound is found
                        new_queue.append((_mn, mx))
                    if _mx != float('inf'):
                        # if new upper bound is found
                        new_queue.append((mn, _mx))
            queue = new_queue

        return min(mx-mn for mn, mx in queue)

    def minimumDeviation(self, nums: List[int]) -> int:
        nums = set(n if n%2==0 else (n*2) for n in nums)
        mn = min(nums)
        mx = max(nums)
        ret = mx-mn

        heap = [-n for n in nums]  # max heap
        heapify(heap)
        # upper bound can only be updated when the max is even
        while heap and heap[0]%2 == 0:
            n = -heappop(heap)
            heappush(heap, -(n//2))
            mx = min(mx, -heap[0])  # new upper bound
            mn = min(mn, n//2)  # new lower bound
            ret = min(ret, mx-mn)
        return ret


@pytest.mark.parametrize('nums, expected', [
    ([1,2,3,4], 1),
    ([4,1,5,20,3], 3),
    ([2,10,8], 3),
    (json.load(open(Path(__file__).parent/'testcase.json')), 891887),
])
def test(nums, expected):
    assert expected == Solution().minimumDeviation(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
