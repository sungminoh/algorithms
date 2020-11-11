#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
55. Jump Game(https://leetcode.com/problems/jump-game/description/)
DescriptionHintsSubmissionsDiscussSolution
DiscussPick One
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

"""


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = 0
        for i, n in enumerate(nums):
            if m == len(nums)-1:
                return True
            if n == 0 and m <= i:
                return False
            m = max(m, i+n)
        return True


def main():
    print(Solution().canJump(list(map(int, input().split()))))


if __name__ == '__main__':
    main()
