#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            n1 = nums[i]
            for j in range(i+1, len(nums)):
                n2 = nums[j]
                if n1 + n2 == target:
                    return [i, j]
        return None


def main():
    print(Solution().twoSum([2,7,11,15], 9))


if __name__ == '__main__':
    main()
