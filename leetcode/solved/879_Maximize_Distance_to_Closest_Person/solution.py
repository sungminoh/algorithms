#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.

Example 1:

Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

Example 2:

Input: seats = [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.

Example 3:

Input: seats = [0,1]
Output: 1

Constraints:

	2 <= seats.length <= 2 * 104
	seats[i] is 0 or 1.
	At least one seat is empty.
	At least one seat is occupied.
"""
import sys
from typing import List
import pytest


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """02/05/2021 20:18"""
        max_gap = 0
        first = -1
        last = len(seats)
        gap = 1
        for i, x in enumerate(seats):
            if x == 0:
                gap += 1
            else:
                if first < 0:
                    first = i
                last = i
                max_gap = max(max_gap, gap/2)
                gap = 1
        if first != 0:
            max_gap = max(max_gap, first)
        if last != len(seats):
            max_gap = max(max_gap, len(seats)-1 - last)
        return max_gap

    def maxDistToClosest(self, seats: List[int]) -> int:
        prev_i = -1
        ret = 0
        for i, s in enumerate(seats):
            if s == 1:
                ret = max(ret, ((i - prev_i)//2) if prev_i >= 0 else i)
                prev_i = i
        if seats[len(seats)-1] == 0:
            ret = max(ret, len(seats)-1-prev_i)
        return ret


@pytest.mark.parametrize('seats, expected', [
    ([1,0,0,0,1,0,1], 2),
    ([1,0,0,0], 3),
    ([0,1], 1),
])
def test(seats, expected):
    assert expected == Solution().maxDistToClosest(seats)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
