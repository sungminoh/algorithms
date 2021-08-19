#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

	Solution(int[] nums) Initializes the object with the integer array nums.
	int[] reset() Resets the array to its original configuration and returns it.
	int[] shuffle() Returns a random shuffling of the array.

Example 1:

Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
                       // Any permutation of [1,2,3] must be equally likely to be returned.
                       // Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

Constraints:

	1 <= nums.length <= 200
	-106 <= nums[i] <= 106
	All the elements of nums are unique.
	At most 5 * 104 calls in total will be made to reset and shuffle.
"""
import sys
from collections import defaultdict
import random
from typing import List
import pytest


class Solution:
    """04/17/2020 22:20"""
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.perm = list(range(len(nums)))

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        def _circle(idx, num):
            if self.perm[idx] == idx:
                return
            next_idx = self.perm[idx]
            next_num = self.nums[idx]
            self.perm[idx] = idx
            self.nums[idx] = num
            _circle(next_idx, next_num)

        for idx, num in zip(self.perm, self.nums):
            _circle(idx, num)
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        last = len(self.nums) - 1
        for i in range(len(self.nums)):
            idx = random.randint(0, last - i)
            self.nums[idx], self.nums[last - i] = self.nums[last - i], self.nums[idx]
            self.perm[idx], self.perm[last - i] = self.perm[last - i], self.perm[idx]
        return self.nums


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.perm = list(range(len(nums)))

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        def rotate(i):
            while self.perm[i] != i:
                j = self.perm[i]
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
                self.perm[i], self.perm[j] = self.perm[j], self.perm[i]

        for i in range(len(self.nums)):
            rotate(i)
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.nums)-1):
            j = random.randint(i, len(self.nums)-1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
            self.perm[i], self.perm[j] = self.perm[j], self.perm[i]
        return self.nums


@pytest.mark.parametrize('nums, n', [
    ([1,2,3], 1000000),
    ([1,2,3,4], 1000000),
])
def test(nums, n):
    cnt = defaultdict(int)
    s = Solution(nums[:])
    for i in range(n):
        cnt[tuple(s.shuffle())] += 1
    print(cnt)
    avg = sum(cnt.values()) / len(cnt)
    for k, c in cnt.items():
        assert avg*0.95 < c < avg*1.05
    reset = s.reset()
    assert reset == nums


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
