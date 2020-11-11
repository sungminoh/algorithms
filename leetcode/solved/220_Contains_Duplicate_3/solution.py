#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""
from typing import List
import sys
sys.path.append('../')
from exercise.tree import Tree


class Solution:
    def __containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        tree = Tree(float('inf'))
        for i, n in enumerate(nums):
            node = tree.insert(n)
            pred = node.predecessor()
            if pred and node.val - pred.val <= t:
                return True
            succ = node.successor()
            if succ and succ.val - node.val <= t:
                return True
            if i >= k:
                tree.remove_val(nums[i - k])
        return False

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False
        bucket = {}
        for i, n in enumerate(nums):
            group = n // (t + 1)
            if group in bucket:
                return True
            if group - 1 in bucket and n - bucket[group - 1] <= t:
                return True
            if group + 1 in bucket and bucket[group + 1] - n <= t:
                return True
            bucket[group] = n
            if i >= k:
                del bucket[nums[i - k] // (t + 1)]
        return False


if __name__ == '__main__':
    cases = [
        ([1,2,3,1], 3, 0),
        ([1,0,1,1], 1, 2),
        ([1,5,9,1,5,9], 2, 3),
        ([-1,-1], 1, -1),
    ]
    expecteds = [
        True,
        True,
        False,
        False,
    ]
    for (nums, k, t), expected in zip(cases, expecteds):
        actual = Solution().containsNearbyAlmostDuplicate(nums, k, t)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')

    with open('./example.txt', 'r') as f:
        nums = eval(f.readline())
        k = eval(f.readline())
        t = eval(f.readline())
        actual = Solution().containsNearbyAlmostDuplicate(nums, k, t)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
