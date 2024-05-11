#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array nums of positive integers, return the longest possible length of an array prefix of nums, such that it is possible to remove exactly one element from this prefix so that every number that has appeared in it will have the same number of occurrences.

If after removing one element there are no remaining elements, it's still considered that every appeared number has the same number of ocurrences (0).

Example 1:

Input: nums = [2,2,1,1,5,3,3,5]
Output: 7
Explanation: For the subarray [2,2,1,1,5,3,3] of length 7, if we remove nums[4] = 5, we will get [2,2,1,1,3,3], so that each number will appear exactly twice.

Example 2:

Input: nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
Output: 13

Constraints:

	2 <= nums.length <= 105
	1 <= nums[i] <= 105
"""
from collections import defaultdict
from collections import Counter
from typing import List
import pytest
import sys


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        """May 07, 2024 21:50"""
        count_groups = {}
        count_groups[0] = 1
        counter = {}
        ret = 0

        def check(count_groups):
            # count_groups = {k: v for k, v in count_groups.items() if k > 0 and v > 0}
            if len(count_groups) == 2:
                if count_groups.get(1, 0) == 1:  # when 1 : 1
                    return True
                a, b = sorted(count_groups.keys())
                if a + 1 == b and count_groups[b] == 1:  # when one has 1 more
                    return True
            elif len(count_groups) == 1:
                if 1 in count_groups:  # when 1 only
                    return True
                if next(iter(count_groups.values())) == 1:  # when only one
                    return True
            return False

        for i, n in enumerate(nums, 1):
            counter.setdefault(n, 0)
            if counter[n] in count_groups:
                count_groups[counter[n]] -= 1
                if count_groups[counter[n]] == 0:
                    count_groups.pop(counter[n])
            counter.setdefault(n, 0)
            counter[n] += 1
            count_groups.setdefault(counter[n], 0)
            count_groups[counter[n]] += 1
            if check(count_groups):
                ret = i
        return ret


@pytest.mark.parametrize('args', [
    (([2,2,1,1,5,3,3,5], 7)),
    (([1,1,1,2,2,2,3,3,3,4,4,4,5], 13)),
    (([1,1,1,2,2,2], 5)),
    (([10,2,8,9,3,8,1,5,2,3,7,6], 8)),
    (([1,2,3,1,2,3,4,4,4,4,1,2,3,5,6], 13)),
    (([1,1], 2)),
    (([1,1,1,2,2,2,3,3,3], 7)),
])
def test(args):
    assert args[-1] == Solution().maxEqualFreq(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
