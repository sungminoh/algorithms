#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

	"a->b" if a != b
	"a" if a == b

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

Constraints:

	0 <= nums.length <= 20
	-231 <= nums[i] <= 231 - 1
	All the values of nums are unique.
	nums is sorted in ascending order.
"""
import sys
from typing import List
import pytest


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """08/22/2019 00:07"""
        def summary_range_by_index(s, e):
            if s == e:
                return []
            if e - s == 1:
                return [(nums[s], )]
            if nums[e - 1] - nums[s] == e - 1 - s:
                return [(nums[s], nums[e - 1])]
            m = s + (e - s) // 2
            left = summary_range_by_index(s, m)
            right = summary_range_by_index(m, e)
            if left and right and left[-1][-1] + 1 == right[0][0]:
                right = [(left[-1][0], right[0][-1]), *right[1:]]
                left = left[:-1]
            return [*left, *right]

        return [str(p[0]) if len(p) == 1
                else '->'.join(str(x) for x in p)
                for p in summary_range_by_index(0, len(nums))]

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        s = nums[0]
        c = s
        ret = []
        for n in nums[1:]:
            if n == c+1:
                c = n
            else:
                ret.append(('%s->%s' % (s, c)) if s < c else ('%s' % s))
                s = c = n
        ret.append(('%s->%s' % (s, c)) if s < c else ('%s' % s))
        return ret


@pytest.mark.parametrize('nums, expected', [
    ([0,1,2,4,5,7], ["0->2","4->5","7"]),
    ([0,2,3,4,6,8,9], ["0","2->4","6","8->9"]),
])
def test(nums, expected):
    assert expected == Solution().summaryRanges(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
