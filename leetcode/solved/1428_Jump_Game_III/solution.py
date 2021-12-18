#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation:
All possible ways to reach at index 3 with value 0 are:
index 5 -> index 4 -> index 1 -> index 3
index 5 -> index 6 -> index 4 -> index 1 -> index 3

Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true
Explanation:
One possible way to reach at index 3 with value 0 is:
index 0 -> index 4 -> index 1 -> index 3

Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.

Constraints:

	1 <= arr.length <= 5 * 104
	0 <= arr[i] < arr.length
	0 <= start < arr.length
"""
import sys
from typing import List
import pytest


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """04/17/2021 21:14"""
        visited = set([start])
        def dfs(arr, i):
            if arr[i] == 0:
                return True
            for j in [i + arr[i], i - arr[i]]:
                if 0 <= j < len(arr) and j not in visited:
                    visited.add(j)
                    if dfs(arr, j):
                        return True
            return False

        return dfs(arr, start)

    def canReach(self, arr: List[int], start: int) -> bool:
        reachable = [False]*len(arr)

        def dfs(i):
            if not (0 <= i < len(arr)) or reachable[i]:
                return
            reachable[i] = True
            dfs(i-arr[i])
            dfs(i+arr[i])

        dfs(start)
        return any(r for n, r in zip(arr, reachable) if n == 0)


@pytest.mark.parametrize('arr, start, expected', [
    ([4,2,3,0,3,1,2], 5, True),
    ([4,2,3,0,3,1,2], 0, True),
    ([3,0,2,1,2], 2, False),
    ([0,3,0,6,3,3,4], 6, True),
])
def test(arr, start, expected):
    assert expected == Solution().canReach(arr, start)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
