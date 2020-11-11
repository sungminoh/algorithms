#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(k, n, m):
            if k == 1:
                return [[n]] if m <= n <= 9 else []
            ret = []
            for i in range(m, 10):
                ret.extend([[i, *s] for s in dfs(k - 1, n - i, i + 1)])
            return ret
        return dfs(k, n, 1)


class SolutionDp:
    def __init__(self):
        self.memo = {}
        # self.hit = 0
        # self.miss = 0

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ret = self.combination(k, n, 1)
        # print(f'{self.hit} / {self.miss} \t ({self.hit/self.miss})')
        return ret

    def combination(self, k: int, n: int, m: int) -> List[List[int]]:
        if k == 1:
            if m <= n <= 9:
                return [[n]]
            else:
                return []
        if (k, n, m) in self.memo:
            # self.hit += 1
            return self.memo[(k, n, m)]
        ret = []
        for i in range(m, 10):
            ret.extend([[i, *s] for s in self.combination(k - 1, n - i, i + 1)])
        self.memo[(k, n, m)] = ret
        # self.miss += 1
        return ret


if __name__ == '__main__':
    cases = [
        (3, 7),
        (3, 9),
        (4, 24)
    ]
    expecteds = [
        [[1,2,4]],
        [[1,2,6], [1,3,5], [2,3,4]],
        [[1,6,8,9],[2,5,8,9],[2,6,7,9],[3,4,8,9],[3,5,7,9],[3,6,7,8],[4,5,6,9],[4,5,7,8]]
    ]
    for (k, n), expected in zip(cases, expecteds):
        actual = Solution().combinationSum3(k, n)
        result = True
        wrongs = []
        for nums in actual:
            s = sum(nums)
            result &= s == n
            if s != n:
                wrongs.append((nums, s))
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
        print(f'-- {result}\tworng cases: {wrongs}')
