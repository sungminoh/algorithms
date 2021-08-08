#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

	i + 1 where: i + 1 < arr.length.
	i - 1 where: i - 1 >= 0.
	j where: arr[i] == arr[j] and i != j.

Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You don't need to jump.

Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.

Example 4:

Input: arr = [6,1,9]
Output: 2

Example 5:

Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
Output: 3

Constraints:

	1 <= arr.length <= 5 * 104
	-108 <= arr[i] <= 108
"""
from pathlib import Path
import json
from collections import defaultdict
from collections import deque
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """DFS"""
        m = {}
        for i, v in enumerate(arr):
            m.setdefault(v, [])
            m[v].append(i)

        @lru_cache(None)
        def dfs(i, available):
            if i == len(arr)-1:
                return 0
            ret = float('inf')
            if i-1 > 0 and 1<<(i-1) & available:
                ret = min(ret, 1 + dfs(i-1, available^(1<<(i-1))))
            if i+1 < len(arr) and 1<<(i+1) % available:
                ret = min(ret, 1 + dfs(i+1, available^(1<<(i+1))))
            for j in m.get(arr[i], []):
                if 1<<j & available:
                    ret = min(ret, 1 + dfs(j, available^(1<<j)))
            return ret

        return dfs(0, (1<<len(arr))-1)

    def minJumps(self, arr: List[int]) -> int:
        """BFS"""
        def compress(arr):
            """Remove repeating element except the first and the last"""
            ret = []
            for i, n in enumerate(arr):
                if i > 0 and i < len(arr)-1:
                    if arr[i-1] == arr[i] == arr[i+1]:
                        continue
                ret.append(n)
            return ret

        arr = compress(arr)
        m = defaultdict(list)
        for i, v in enumerate(arr):
            m[v].append(i)

        visited = set([0])
        queue = deque([(0, 0)])
        while queue:
            i, cnt = queue.popleft()
            if i == len(arr)-1:
                return cnt
            if i-1 > 0 and i-1 not in visited:
                visited.add(i-1)
                queue.append((i-1, cnt+1))
            if i+1 > 0 and i+1 not in visited:
                visited.add(i+1)
                queue.append((i+1, cnt+1))
            for j in m[arr[i]]:
                if j not in visited:
                    visited.add(j)
                    queue.append((j, cnt+1))
            # Not to iterate the index array twice.
            # If we compress the array, this may not be needed.
            m.pop(arr[i])
        return -1


@pytest.mark.parametrize('arr, expected', [
    ([100,-23,-23,404,100,23,23,23,3,404], 3),
    ([7], 0),
    ([7,6,9,6,9,6,9,7], 1),
    ([6,1,9], 2),
    ([11,22,7,7,7,7,7,7,7,22,13], 3),
    ([-53,97,65,-78,-84,-56,-96,-19,-84,67,-47,-53,-78,65,-62,-81,11,67,-53], 1),
    *json.load(open(Path(__file__).parent/'testcase.json'))
])
def test(arr, expected):
    assert expected == Solution().minJumps(arr)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
