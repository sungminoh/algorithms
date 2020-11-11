
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""
from copy import deepcopy
import random
import heapq
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
        people.sort(key=lambda p: (-p[0], p[1]))
        ret = []
        for p in people:
            ret.insert(p[1], p)
        return ret

    def _reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        d = dict()
        # n * logn
        for h, k in people:
            if k not in d:
                d.setdefault(k, [])
            heapq.heappush(d[k], [h, 0])

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
            heapq.heappop(d[taller])
            if not d[taller]:
                d.pop(taller)
            else:
                d[taller][0][1] = how_many_taller(ret, d[taller][0][0])
            for k, hs in d.items():
                if k != taller and hs[0][0] <= height:
                    hs[0][1] += 1
        return ret

    def _reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        d = dict()
        for h, k in people:
            if k not in d:
                d.setdefault(k, [])
            heapq.heappush(d[k], h)

        ret = []
        while d:
            candidates = []
            for k, hs in d.items():
                h = hs[0]
                if k == how_many_taller(ret, h):
                    heapq.heappush(candidates, (h, k))
            assert candidates
            h, k = heapq.heappop(candidates)
            ret.append([h, k])
            heapq.heappop(d[k])
            if not d[k]:
                d.pop(k)
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
    ([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]], [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]),
    gen_case(1),
    ([[38, 18], [59, 1], [45, 4], [48, 1], [16, 5], [39, 2], [13, 12], [51, 4], [9, 11], [57, 1], [54, 4], [8, 19], [12, 27], [38, 11], [32, 9], [40, 2], [20, 12], [7, 37], [59, 0], [52, 1], [20, 25], [28, 10], [49, 7], [49, 4], [27, 21], [17, 5], [29, 6], [50, 3], [51, 3], [9, 32], [35, 14], [55, 3], [39, 5], [43, 15], [46, 1], [50, 7], [3, 26], [26, 12], [54, 1], [51, 7]],
     [[59, 0], [46, 1], [39, 2], [40, 2], [48, 1], [16, 5], [17, 5], [39, 5], [29, 6], [52, 1], [45, 4], [9, 11], [54, 1], [13, 12], [28, 10], [32, 9], [20, 12], [26, 12], [50, 3], [8, 19], [49, 4], [38, 11], [51, 3], [51, 4], [35, 14], [49, 7], [3, 26], [57, 1], [50, 7], [27, 21], [12, 27], [59, 1], [20, 25], [38, 18], [9, 32], [51, 7], [43, 15], [54, 4], [7, 37], [55, 3]]),
    gen_case(10),
    gen_case(100),
    gen_case(500),
    gen_case(1000),
])
def test(people, expected):
    # print()
    # print(people)
    # print(expected)
    assert expected == Solution().reconstructQueue(people)
