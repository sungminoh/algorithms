
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""
from collections import defaultdict
import random
from typing import List
import pytest


class Solution:

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


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
def test():
    cnt = defaultdict(int)
    nums = [100, 200, 300]
    s = Solution(nums[:])
    for i in range(10000):
        cnt[tuple(s.shuffle())] += 1
    print(cnt)
    reset = s.reset()
    print(reset)
    assert reset == nums
