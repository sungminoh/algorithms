#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution:
    def combine(self, n, k):
        ret = []
        def dfs(s, e, arr):
            if len(arr) == k:
                ret.append(arr.copy())
                return
            if len(arr) + (e-s+1) < k:
                return
            for i in range(s, e+1):
                arr.append(i)
                dfs(i+1, e, arr)
                arr.pop()
        dfs(1, n, [])
        return ret

    def combine3(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        memo = [[None] * (n+1) for _ in range(n+1)]
        def _combine(a, b):
            if memo[a][b]:
                return memo[a][b]
            if b == 1:
                return [[i] for i in range(1, a+1)]
            elif b == a:
                return [[i for i in range(1, a+1)]]
            else:
                ret = _combine(a-1, b)
                sub = _combine(a-1, b-1)
                for l in sub:
                    l.append(a)
                ret += sub
                return ret
        return _combine(n, k)


    def combine2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = list(range(1, n+1))
        ret = []
        candidates = []
        for num in list(range(1, n+1)):
            i = 0
            new_candidates = []
            del_index = []
            while i < len(candidates):
                if len(candidates[i]) == k:
                    ret.append(candidates[i])
                    del_index.append(i)
                elif len(candidates[i]) + (n-num+1) >= k:
                    new_candidates.append(candidates[i] + [num])
                i += 1
            for i in reversed(del_index):
                del(candidates[i])
            del_index = []
            candidates.extend(new_candidates)
            candidates.append([num])
        for c in candidates:
            if len(c) == k:
                ret.append(c)
        return ret


def main():
    for l in Solution().combine(*[int(x) for x in input().split()]):
        print(l)


if __name__ == '__main__':
    main()
