#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

	0 <= nums.length <= 105
	-109 <= nums[i] <= 109
"""
import sys
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def longestConsecutive(self, nums):
        """08/18/2018 18:52
        Keep the group number of start and end point of each interval
        and each group's start and end
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not nums:
            return 0
        group_idx = 0
        group = dict()
        group_min_max = dict()
        m = 1
        for n in set(nums):
            if n+1 not in group and n-1 not in group:
                group[n] = group_idx
                group_min_max[group_idx] = (n, n)
                group_idx += 1
            else:
                group_min = group_max = n
                gs = []
                if n-1 in group:
                    gs.append(group.pop(n-1))
                if n+1 in group:
                    gs.append(group.pop(n+1))
                group_min = min(n, *[group_min_max[g][0] for g in gs])
                group_max = max(n, *[group_min_max[g][1] for g in gs])
                group[group_min] = gs[0]
                group[group_max] = gs[0]
                group_min_max[gs[0]] = (group_min, group_max)
                m = max(m, group_max - group_min + 1)
        return m

    def longestConsecutive(self, nums: List[int]) -> int:
        """Union-find
        Keep the representative of each num
        Time complexity: O(nlogn)
        Space complexity: O(n)
        """
        if not nums:
            return 0
        m = {}
        for n in nums:
            rep = n
            if n-1 in m:
                rep = m[n-1]
                while rep != m[rep]:
                    rep = m[rep]
            m[n] = rep
            if n+1 in m:
                rep = m[n+1]
                m[n+1] = m[n]
                while rep != m[rep]:
                    rep = m[rep]
                    m[rep] = m[n]
        cnt = defaultdict(int)
        for k, v in m.items():
            rep = m[k]
            while rep != m[rep]:
                rep = m[rep]
            cnt[rep] += 1
        return max(cnt.values())


@pytest.mark.parametrize('nums, expected', [
([100,4,200,1,3,2], 4),
([0,3,7,2,5,8,4,6,0,1], 9),
])
def test(nums, expected):
    assert expected == Solution().longestConsecutive(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
