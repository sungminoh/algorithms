
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

	age[B] <= 0.5 * age[A] + 7
	age[B] > age[A]
	age[B] > 100 && age[A] < 100

Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.

Example 2:

Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.

Example 3:

Input: [20,30,100,110,120]
Output:
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.

Notes:
    1. 1 <= ages.length <= 20000.
    2. 1 <= ages[i] <= 120.
"""
import sys
from typing import List
import pytest


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages = sorted(ages)
        i, j = 0, 1
        cnt = 0
        same = 0
        while j < len(ages):
            if ages[j] == ages[j-1] and ages[j] > 0.5 * ages[j] + 7:
                same += 1
            else:
                same = 0
            while i < j and ages[i] <= 0.5 * ages[j] + 7:
                i += 1
            cnt += same + j - i
            j += 1
        print(ages)
        return cnt


@pytest.mark.parametrize('ages, expected', [
    ([16,16], 2),
    ([16,17,18], 2),
    ([73,106,39,6,26,15,30,100,71,35,46,112,6,60,110], 29),
])
def test(ages, expected):
    assert expected == Solution().numFriendRequests(ages)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))


