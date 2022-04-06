#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

Example 1:

Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation:
In this case, it is not possible to rotate the dominoes to make one row of values equal.

Constraints:

	2 <= tops.length <= 2 * 104
	bottoms.length == tops.length
	1 <= tops[i], bottoms[i] <= 6
"""
import sys
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if not tops or not bottoms:
            return 0
        N = len(tops)
        cnt = defaultdict(int)
        for t, b in zip(tops, bottoms):
            cnt[t] += 1
            if t != b:
                cnt[b] += 1
        vals = [k for k, v in cnt.items() if v == N]
        if not vals:
            return -1

        same = 0
        ret = 0
        for t, b in zip(tops, bottoms):
            if t == b:
                same += 1
            if t != vals[0]:
                ret += 1
        return min(ret, N-ret-same)


@pytest.mark.parametrize('tops, bottoms, expected', [
    ([2,1,2,4,2,2], [5,2,6,2,3,2], 2),
    ([5,2,6,2,3,2], [2,1,2,4,2,2], 2),
    ([3,5,1,2,3], [3,6,3,3,4], -1),
    ([1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2], 1),
    ([2,1,2,2,2,2,2,2], [1,2,1,1,1,2,2,2], 1),
])
def test(tops, bottoms, expected):
    assert expected == Solution().minDominoRotations(tops, bottoms)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
