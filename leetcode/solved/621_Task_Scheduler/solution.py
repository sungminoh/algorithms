
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

Constraints:

	The number of tasks is in the range [1, 10000].
	The integer n is in the range [0, 100].
"""
import sys
from heapq import heappush
from heapq import heappop
from heapq import heapify
from collections import Counter
from typing import List
import pytest


class Solution:
    def _leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-c for c in Counter(tasks).values()]
        heapify(heap)
        ret = 0
        while True:
            i = 0
            cnt = len(heap)
            poped = []
            while i < cnt and i <= n:
                poped.append(heappop(heap))
                i += 1
            for nc in poped:
                if nc + 1 != 0:
                    heappush(heap, nc + 1)
            if not heap:
                ret += i
                break
            else:
                ret += n + 1
        return ret

    def leastInterval(self, tasks: List[str], n: int) -> int:
        v = list(Counter(tasks).values())
        m = max(v)
        return max((m-1)*(n+1) + v.count(m), len(tasks))


@pytest.mark.parametrize('tasks, n, expected', [
    (["A","A","A","B","B","B"], 2, 8),
    (["A","A","A","B","B","B","C","C","C","D","D","D","D","D","D"], 1, 15),
])
def test(tasks, n, expected):
    assert expected == Solution().leastInterval(tasks, n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
