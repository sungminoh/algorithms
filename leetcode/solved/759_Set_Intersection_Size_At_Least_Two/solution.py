#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a 2D integer array intervals where intervals[i] = [starti, endi] represents all the integers from starti to endi inclusively.

A containing set is an array nums where each interval from intervals has at least two integers in nums.

	For example, if intervals = [[1,3], [3,7], [8,9]], then [1,2,4,7,8,9] and [2,3,4,8,9] are containing sets.

Return the minimum possible size of a containing set.

Example 1:

Input: intervals = [[1,3],[3,7],[8,9]]
Output: 5
Explanation: let nums = [2, 3, 4, 8, 9].
It can be shown that there cannot be any containing array of size 4.

Example 2:

Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
Output: 3
Explanation: let nums = [2, 3, 4].
It can be shown that there cannot be any containing array of size 2.

Example 3:

Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
Output: 5
Explanation: let nums = [1, 2, 3, 4, 5].
It can be shown that there cannot be any containing array of size 4.

Constraints:

	1 <= intervals.length <= 3000
	intervals[i].length == 2
	0 <= starti < endi <= 108
"""
from typing import List
from heapq import heapify, heappop, heappush
import pytest
import sys


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        """Apr 13, 2024 17:14"""
        intervals.sort(key=lambda x: x[1])

        ps = -1
        pe = -1
        ret = 0
        for s, e in intervals:
            if pe < s:  # no overlap
                ret += 2
                ps = e-1
                pe = e
            else:
                if ps >= s:  # overlap
                    pass  # no-op
                else:
                    if pe == e:
                        ps = e-1
                        pe = e
                    else:
                        ps = pe
                        pe = e
                    ret += 1
        return ret


@pytest.mark.parametrize('args', [
    (([[1,3],[3,7],[8,9]], 5)),
    (([[1,3],[1,4],[2,5],[3,5]], 3)),
    (([[1,2],[2,3],[2,4],[4,5]], 5)),
    (([[1,3],[3,7],[5,7],[7,8]], 5)),
    (([[1,3],[1,2],[0,1]], 3)),
])
def test(args):
    assert args[-1] == Solution().intersectionSizeTwo(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
