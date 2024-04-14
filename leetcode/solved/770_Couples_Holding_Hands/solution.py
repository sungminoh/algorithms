#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are n couples sitting in 2n seats arranged in a row and want to hold hands.

The people and seats are represented by an integer array row where row[i] is the ID of the person sitting in the ith seat. The couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2n - 2, 2n - 1).

Return the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

Example 1:

Input: row = [0,2,1,3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.

Example 2:

Input: row = [3,2,0,1]
Output: 0
Explanation: All couples are already seated side by side.

Constraints:

	2n == row.length
	2 <= n <= 30
	n is even.
	0 <= row[i] < 2n
	All the elements of row are unique.
"""
from typing import List
import pytest
import sys


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        pos = {c: i for i, c in enumerate(row)}

        def is_couple(a, b):
            if a > b:
                return is_couple(b, a)
            return a%2 == 0 and b == a+1

        def find_couple(a):
            return (a+1) if a%2 == 0 else (a-1)

        memo = {}
        def dfs(i):
            k = tuple(row[i:])
            if k in memo:
                return memo[k]
            if i == len(row):
                ret = 0
            elif is_couple(row[i], row[i+1]):
                ret = dfs(i+2)
            else:
                ret = float('inf')
                # swap i+1
                p = pos[find_couple(row[i])]
                row[i+1], row[p] = row[p], row[i+1]
                ret = min(ret, 1 + dfs(i+2))
                row[i+1], row[p] = row[p], row[i+1]
                # swap i
                p = pos[find_couple(row[i+1])]
                row[i], row[p] = row[p], row[i]
                ret = min(ret, 1 + dfs(i+2))
                row[i], row[p] = row[p], row[i]
            memo[k] = ret
            return ret

        return dfs(0)

    def minSwapsCouples(self, row: List[int]) -> int:
        """Apr 13, 2024 19:22"""
        def is_couple(a, b):
            if a > b:
                return is_couple(b, a)
            return a%2 == 0 and b == a+1

        def find_couple(a):
            return (a+1) if a%2 == 0 else (a-1)

        seat_map = {}
        seats = []
        graph = {}

        for i in range(0, len(row), 2):
            a, b = sorted([row[i], row[i+1]])
            if not is_couple(a, b):
                sn = len(seats)
                seat_map[a] = seat_map[b] = sn
                seats.append((a, b))
                for p in [a, b]:
                    q = find_couple(p)
                    if q in seat_map:
                        snq = seat_map[q]
                        graph.setdefault(sn, set()).add(snq)
                        graph.setdefault(snq, set()).add(sn)

        visited = set()
        def dfs(i):
            for j in graph[i]:
                if j not in visited:
                    visited.add(j)
                    return 1 + dfs(j)
            return 0

        return sum(dfs(x)-1 for x in list(graph.keys()) if x not in visited)


@pytest.mark.parametrize('args', [
    (([0,2,1,3], 1)),
    (([3,2,0,1], 0)),
    (([5,4,2,6,3,1,0,7], 2)),
    (([28,4,37,54,35,41,43,42,45,38,19,51,49,17,47,25,12,53,57,20,2,1,9,27,31,55,32,48,59,15,14,8,3,7,58,23,10,52,22,30,6,21,24,16,46,5,33,56,18,50,39,34,29,36,26,40,44,0,11,13], 26)),
    (([2,53,34,52,58,27,42,26,17,32,48,39,4,3,55,11,54,6,1,20,7,23,45,56,30,18,44,38,33,10,19,36,29,40,43,13,24,50,0,15,21,35,12,46,37,51,49,5,57,22,14,59,41,28,25,31,8,16,47,9], 27)),
])
def test(args):
    assert args[-1] == Solution().minSwapsCouples(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
