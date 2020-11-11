
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a circular array nums of positive and negative integers. If a number k at an index is positive, then move forward k steps. Conversely, if it's negative (-k), move backward k steps. Since the array is circular, you may assume that the last element's next element is the first element, and the first element's previous element is the last element.

Determine if there is a loop (or a cycle) in nums. A cycle must start and end at the same index and the cycle's length > 1. Furthermore, movements in a cycle must all follow a single direction. In other words, a cycle must not consist of both forward and backward movements.

Example 1:

Input: [2,-1,1,2,2]
Output: true
Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length is 3.

Example 2:

Input: [-1,2]
Output: false
Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle, because the cycle's length is 1. By definition the cycle's length must be greater than 1.

Example 3:

Input: [-2,1,-1,-2,-2]
Output: false
Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle, because movement from index 1 -> 2 is a forward movement, but movement from index 2 -> 1 is a backward movement. All movements in a cycle must follow a single direction.

Note:

	-1000 ≤ nums[i] ≤ 1000
	nums[i] ≠ 0
	1 ≤ nums.length ≤ 5000

Follow up:

Could you solve it in O(n) time complexity and O(1) extra space complexity?
"""
import sys
from typing import List
import pytest


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def mod(n, m):
            return -((-n) % m) if n < 0 else n % m

        def check_cycle(i):
            temp = set()
            j = i
            while j not in temp:
                visited.add(j)
                temp.add(j)
                j = (i + nums[i]) % n
                if i == j or nums[i] * nums[j] < 0:
                    return False
                elif j in temp:
                    return True
                if j in visited:
                    return False
                i = j

        n = len(nums)
        visited = set()
        i = 0
        while len(visited) < n:
            while i < n - 1 and i in visited:
                i += 1
            if check_cycle(i):
                return True
        return False


@pytest.mark.parametrize('nums, expected', [
    ([2,-1,1,2,2], True),
    ([-1,2], False),
    ([-2,1,-1,-2,-2], False),
])
def test(nums, expected):
    assert expected == Solution().circularArrayLoop(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
