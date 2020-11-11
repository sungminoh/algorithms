#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
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


if __name__ == "__main__":
    cases = [
        ([0,1,2,4,5,7], ["0->2","4->5","7"]),
        ([0,2,3,4,6,8,9], ["0","2->4","6","8->9"])
    ]
    for case, expected in cases:
        actual = Solution().summaryRanges(case)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')

