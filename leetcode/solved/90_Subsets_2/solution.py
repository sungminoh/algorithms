#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        nums.sort()
        nums.append(None)
        ret = []
        n = 0
        for i in range(0, len(nums)-1):
            n += 1
            if nums[i] != nums[i+1]:
                tmp = [[nums[i]] * j for j in range(1, n+1)]
                add = [s + t for s in ret for t in tmp] + tmp
                ret.extend(add)
                n = 0
        ret.append([])
        return ret



def main():
    for s in Solution().subsetsWithDup([int(x) for x in input().split()]):
        print(s)


if __name__ == '__main__':
    main()
