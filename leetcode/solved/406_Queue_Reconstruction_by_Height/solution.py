#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

Example 1:

Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.

Example 2:

Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

Constraints:

	1 <= people.length <= 2000
	0 <= hi <= 106
	0 <= ki < people.length
	It is guaranteed that the queue can be reconstructed.
"""
from copy import deepcopy
import random
from pip._internal.resolution.resolvelib import candidates
from heapq import heappush
from heapq import heappop
import sys
from typing import List
import pytest


def how_many_taller(people, height):
    cnt = 0
    for h, k in people:
        if h >= height:
            cnt += 1
    return cnt


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """04/25/2020 17:33"""
        d = dict()
        # n * logn
        for h, k in people:
            if k not in d:
                d.setdefault(k, [])
            heappush(d[k], [h, 0])

        ret = []
        # n * n
        while d:
            height, taller = float('inf'), None
            for k, hs in d.items():
                if k == hs[0][1]:
                    if hs[0][0] < height:
                        height, taller = hs[0][0], k
            assert taller is not None
            ret.append([height, taller])
            heappop(d[taller])
            if not d[taller]:
                d.pop(taller)
            else:
                d[taller][0][1] = how_many_taller(ret, d[taller][0][0])
            for k, hs in d.items():
                if k != taller and hs[0][0] <= height:
                    hs[0][1] += 1
        return ret

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        d = dict()
        for h, k in people:
            if k not in d:
                d.setdefault(k, [])
            heappush(d[k], h)

        ret = []
        while d:
            candidates = []
            for k, hs in d.items():
                h = hs[0]
                if k == how_many_taller(ret, h):
                    heappush(candidates, (h, k))
            assert candidates
            h, k = heappop(candidates)
            ret.append([h, k])
            heappop(d[k])
            if not d[k]:
                d.pop(k)
        return ret

    def _reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ret = []
        # sort by height desc and the number of taller
        for p in sorted(people, key=lambda x: (-x[0], x[1])):
            ret.insert(p[1], p)
        return ret


def gen_case(n):
    expected = []
    for _ in range(n):
        h = random.randint(1, int(1.5 * n))
        expected.append([h, how_many_taller(expected, h)])
    people = deepcopy(expected)
    random.shuffle(people)
    return people, expected


@pytest.mark.parametrize('people, expected', [
    ([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]], [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]),
    ([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]], [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]),
    ([[38, 18], [59, 1], [45, 4], [48, 1], [16, 5], [39, 2], [13, 12], [51, 4], [9, 11], [57, 1], [54, 4], [8, 19], [12, 27], [38, 11], [32, 9], [40, 2], [20, 12], [7, 37], [59, 0], [52, 1], [20, 25], [28, 10], [49, 7], [49, 4], [27, 21], [17, 5], [29, 6], [50, 3], [51, 3], [9, 32], [35, 14], [55, 3], [39, 5], [43, 15], [46, 1], [50, 7], [3, 26], [26, 12], [54, 1], [51, 7]],
     [[59, 0], [46, 1], [39, 2], [40, 2], [48, 1], [16, 5], [17, 5], [39, 5], [29, 6], [52, 1], [45, 4], [9, 11], [54, 1], [13, 12], [28, 10], [32, 9], [20, 12], [26, 12], [50, 3], [8, 19], [49, 4], [38, 11], [51, 3], [51, 4], [35, 14], [49, 7], [3, 26], [57, 1], [50, 7], [27, 21], [12, 27], [59, 1], [20, 25], [38, 18], [9, 32], [51, 7], [43, 15], [54, 4], [7, 37], [55, 3]]),
])
def test(people, expected):
    assert expected == Solution().reconstructQueue(people)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
