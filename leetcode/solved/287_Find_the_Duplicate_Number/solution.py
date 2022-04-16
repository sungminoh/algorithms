#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3

Constraints:

	1 <= n <= 105
	nums.length == n + 1
	1 <= nums[i] <= n
	All the integers in nums appear only once except for precisely one integer which appears two or more times.

Follow up:

	How can we prove that at least one duplicate number must exist in nums?
	Can you solve the problem in linear runtime complexity?
"""
import random
import sys
from typing import List
import pytest


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """03/28/2020 11:28"""
        l, r = 1, len(nums) - 1
        while l <= r:
            k = l + (r - l) // 2
            smaller = 0
            larger = 0
            found = False
            for n in nums:
                if n > r or n < l:
                    continue
                if n < k:
                    smaller += 1
                elif n > k:
                    larger += 1
                elif found:
                    return k
                else:
                    found = True
            if smaller < larger:
                l = k + 1
            else:
                r = k - 1
        return -1

    def findDuplicate(self, nums: List[int]) -> int:
        """
        If we consider `nums` is a graph with a cycle. The problem is how to
        find the start of the cycle.
        For example, [1,3,4,2,2] can be considered as a graph like
        0 -> 1 -> 3 -> 2 -> 4 -> 2

        Let's say the cycle starte after l and the length of the cycle is k.
        If a fast pointer moved 2v and a slow pointer moved v when they met,
        v = l + xk + r
        2v = 2l + xk + 2r
        Thus, l = zk - r

        While a new pointer starting from zero moves l to the start of the
        cylce, a pointer from l+r can also go l to l + (r+l)%k.
        Since l = zk - r, (r+l)%k = 0.

        This means that the new pointer from zero and a pointer from l+r will
        meet at l
        """
        slow = nums[0]
        fast = nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        new = 0
        while new != slow:
            slow = nums[slow]
            new = nums[new]
        return new


def gen_case():
    n = random.randint(2, 10)
    nums = list(range(1, n + 1))
    duplicate = random.randint(1, n - 1)
    nums[-1] = duplicate
    random.shuffle(nums)
    return nums, duplicate


@pytest.mark.parametrize('nums, expected', [
    ([1,3,4,2,2], 2),
    ([3,1,3,4,2], 3),
    ([2,2,2,2,2], 2),
    ([3,2,2,2,4], 2),
    gen_case(),
    gen_case(),
    gen_case(),
])
def test(nums, expected):
    assert expected == Solution().findDuplicate(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
