#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

"""


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
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
                    gs.append(group[n-1])
                if n+1 in group:
                    gs.append(group[n+1])
                group_min = min(group_min, *[group_min_max[g][0] for g in gs])
                group_max = max(group_max, *[group_min_max[g][1] for g in gs])
                group[group_min] = gs[0]
                group[group_max] = gs[0]
                group_min_max[gs[0]] = (group_min, group_max)
                m = max(m, group_max - group_min + 1)
        return m


def main():
    # nums = [int(x) for x in input().split()]
    nums = [-1,9,-3,-6,7,-8,-6,2,9,2,3,-2,4,-1,0,6,1,-9,6,8,6,5,2]
    nums = [2147483646,-2147483647,0,2,2147483644,-2147483645,2147483645]
    print(Solution().longestConsecutive(nums))


if __name__ == '__main__':
    main()
