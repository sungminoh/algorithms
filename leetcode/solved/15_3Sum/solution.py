#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

	3 <= nums.length <= 3000
	-105 <= nums[i] <= 105
"""
from collections import defaultdict
from pathlib import Path
import json
from typing import List
import pytest
import sys


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time complexity: O(n^2)
        Space complexity: O(n^3)
        """
        N = len(nums)

        m = defaultdict(list)
        for i, n in enumerate(nums):
            m[n].append(i)

        visited = set()
        ret = []
        for i in range(N-1):
            for j in range(i+1, N):
                target = -(nums[i] + nums[j])
                key = tuple(sorted([nums[i], nums[j], target]))
                if key in visited:
                    continue
                visited.add(key)
                if target in m and m[target][-1] > j:
                    ret.append([nums[i], nums[j], target])

        return ret

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time complexity: O(n^2)
        Space complexity: O(1)  Exclude return
        """
        nums.sort()
        N = len(nums)
        ret = []
        for i in range(N-2):
            l, r = i+1, N-1
            if i != 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ret.append((nums[i], nums[l], nums[r]))
                    while (l < r) and nums[l] == ret[-1][1]:
                        l += 1
                    while (l < r) and nums[r] == ret[-1][2]:
                        r -= 1
        return ret

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Mar 04, 2023 21:53
        TLE
        """
        one = {}
        two = {}
        ret = []
        for n in nums:
            if -n in two:
                ret.extend(l + [n] for l in two[-n])
            for a, ll in one.items():
                two.setdefault(a+n, []).extend(l + [n] for l in ll)
            one.setdefault(n, []).append([n])
        return [list(x) for x in set(tuple(sorted(x)) for x in ret)]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Mar 04, 2023 23:04"""
        nums.sort()
        ret = []
        i = 0
        for i in range(len(nums)):
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                continue
            l = 0
            r = i-1
            while l < r:
                s = nums[l] + nums[r] + nums[i]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    tp = [nums[l], nums[r], nums[i]]
                    ret.append(tp)
                    while l < r and nums[l] == tp[0]:
                        l += 1
                    while r > l and nums[r] == tp[1]:
                        r -= 1
        return ret


@pytest.mark.parametrize('args', [
    (([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]])),
    (([0,1,1], [])),
    (([0,0,0], [[0,0,0]])),
    (([0,0,0,0], [[0,0,0]])),
    (json.load(open(Path(__file__).parent/'testcase.json'))),
])
def test(args):
    actual = Solution().threeSum(*args[:-1])
    print(actual)
    assert sorted(args[-1]) == sorted(actual)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
