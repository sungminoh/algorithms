#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)
        accum = 1
        for i, n in enumerate(nums):
            ret[i] *= accum
            accum *= n
        accum = 1
        for i, n in enumerate(nums[-1::-1]):
            ret[len(nums) - 1 - i] *= accum
            accum *= n
        return ret


if __name__ == '__main__':
    cases = [
        ([1,2,3,4], [24,12,8,6]),
        ([2], [1])
    ]
    for case, expected in cases:
        actual = Solution().productExceptSelf(case)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
