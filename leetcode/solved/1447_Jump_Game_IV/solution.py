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
Explanation: Start index is the last index. You do not need to jump.

Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.

Constraints:

	1 <= arr.length <= 5 * 104
	-108 <= arr[i] <= 108
"""
from collections import defaultdict
from collections import deque
from functools import lru_cache
from pathlib import Path
import json
from typing import List
import pytest
import sys


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """Aug 08, 2021 15:17 TLE
        DFS"""
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
        """Aug 08, 2021 15:55
        BFS"""
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

    def minJumps(self, arr: List[int]) -> int:
        """Jan 30, 2022 19:38"""
        warp = defaultdict(set)
        for i, x in enumerate(arr):
            warp[x].add(i)

        visited = set([0])
        queue = [0]

        def visit_if_not_visited(i, queue):
            if 0<= i < len(arr) and i not in visited:
                visited.add(i)
                queue.append(i)

        ret = 0
        while queue:
            new_queue = []
            for i in queue:
                if i == len(arr)-1:
                    return ret
                visit_if_not_visited(i-1, new_queue)
                visit_if_not_visited(i+1, new_queue)
                for j in warp[arr[i]]:
                    visit_if_not_visited(j, new_queue)
                # This is not to iterate the above for loop ever again
                warp.pop(arr[i])
            queue = new_queue
            ret += 1

        return -1

    def minJumps(self, arr: List[int]) -> int:
        """Apr 04, 2023 23:24"""
        N = len(arr)
        groups = {}
        for i in range(N):
            groups.setdefault(arr[i], set()).add(i)

        q = [0]
        visited = set()
        ret = 0
        while q:
            _q = []
            for i in q:
                if i == N-1:
                    return ret
                if i+1 < N and i+1 not in visited:
                    visited.add(i+1)
                    _q.append(i+1)
                if i-1 >= 0 and i-1 not in visited:
                    visited.add(-1)
                    _q.append(i-1)
                for j in groups[arr[i]]:
                    if j not in visited:
                        visited.add(j)
                        _q.append(j)
                groups[arr[i]] = set()
            ret += 1
            q = _q
        return -1

    def minJumps(self, arr: List[int]) -> int:
        """practice 2025/08/06"""
        groups = defaultdict(set)
        for i in range(len(arr)):
            groups[arr[i]].add(i)

        step = 0
        visited = set()
        queue = [0]
        while queue:
            _queue = []
            for i in queue:
                if i == len(arr)-1:
                    return step
                if i-1>=0 and i-1 not in visited:
                    visited.add(i-1)
                    _queue.append(i-1)
                if i+1<len(arr) and i+1 not in visited:
                    visited.add(i+1)
                    _queue.append(i+1)
                for j in groups[arr[i]]:
                    if j not in visited:
                        visited.add(j)
                        _queue.append(j)
                groups[arr[i]] = set()  # all visited. no need to iterate again
            queue = _queue
            step += 1

        return -1


@pytest.mark.parametrize('args', [
    (([100,-23,-23,404,100,23,23,23,3,404], 3)),
    (([7], 0)),
    (([7,6,9,6,9,6,9,7], 1)),
    (([68,-94,-44,-18,-1,18,-87,29,-6,-87,-27,37,-57,7,18,68,-59,29,7,53,-27,-59,18,-1,18,-18,-59,-1,-18,-84,-20,7,7,-87,-18,-84,-20,-27], 5)),
    (([6,1,9], 2)),
    (([11,22,7,7,7,7,7,7,7,22,13], 3)),
    ((json.load(open(Path(__file__).parent/'testcase.json')), 4)),
    ((json.load(open(Path(__file__).parent/'testcase2.json')), 4)),
    ((json.load(open(Path(__file__).parent/'testcase3.json')), 30)),
])
def test(args):
    assert args[-1] == Solution().minJumps(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
