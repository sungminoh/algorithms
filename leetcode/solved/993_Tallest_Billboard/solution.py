#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are installing a billboard and want it to have the largest height. The billboard will have two steel supports, one on each side. Each steel support must be an equal height.

You are given a collection of rods that can be welded together. For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.

Return the largest possible height of your billboard installation. If you cannot support the billboard, return 0.

Example 1:

Input: rods = [1,2,3,6]
Output: 6
Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.

Example 2:

Input: rods = [1,2,3,4,5,6]
Output: 10
Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.

Example 3:

Input: rods = [1,2]
Output: 0
Explanation: The billboard cannot be supported, so we return 0.

Constraints:

	1 <= rods.length <= 20
	1 <= rods[i] <= 1000
	sum(rods[i]) <= 5000
"""
import itertools
from collections import defaultdict
from collections import deque
from typing import List
import pytest
import sys


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        """Apr 28, 2024 12:18 TLE"""
        ret = 0
        dp = set([(0, 0)])
        for x in rods + [0]:
            _dp = set()
            for l, r in dp:
                if l == r:
                    ret = max(ret, l)
                _dp.update([
                    tuple(sorted([l + x, r])),
                    tuple(sorted([l, r + x])),
                    tuple(sorted([l, r])),
                ])
            dp = _dp
        return ret

    def tallestBillboard(self, rods: List[int]) -> int:
        """Apr 28, 2024 12:32 TLE"""
        S = sum(rods)
        rods += [0]
        suffix_sum = list(itertools.accumulate(reversed(rods)))[::-1] + [0]
        ret = 0
        dp = set([(0, 0)])
        for i, x in enumerate(rods):
            _dp = set()
            for l, r in dp:
                if l == r:
                    ret = max(ret, l)
                a = tuple(sorted([l + x, r]))
                b = tuple(sorted([l, r + x]))
                c = tuple(sorted([l, r]))
                if a[0] <= S//2:
                    _dp.add(a)
                if b[0] <= S//2:
                    _dp.add(b)
                if ret*2 - sum(c) <= suffix_sum[i+1]:
                    _dp.add(c)
            dp = _dp
        return ret

    def tallestBillboard(self, rods: List[int]) -> int:
        """Apr 28, 2024 13:09"""
        ret = 0
        dp = [{0: 0}]
        for i, r in enumerate(rods + [0]):
            _dp = defaultdict(int)
            for d in dp:
                for gap, length in d.items():
                    if gap == 0:
                        ret = max(ret, length)
                    _dp[gap + r] = max(_dp[gap + r], length)
                    if gap >= r:
                        _dp[gap - r] = max(_dp[gap - r], length + r)
                    else:
                        _dp[r - gap] = max(_dp[r - gap], length + gap)
            dp.append(_dp)
        return ret

    def tallestBillboard(self, rods: List[int]) -> int:
        """Apr 28, 2024 13:13"""
        dp = defaultdict(int)
        dp[0] = 0
        for i, r in enumerate(rods + [0]):
            for gap, length in list(dp.items()):
                dp[gap + r] = max(dp[gap + r], length)
                if gap >= r:
                    dp[gap - r] = max(dp[gap - r], length + r)
                else:
                    dp[r - gap] = max(dp[r - gap], length + gap)
        return dp[0]


@pytest.mark.parametrize('args', [
    (([1,2,3,6], 6)),
    (([1,2,3,4,5,6], 10)),
    (([1,2], 0)),
    (([1,2,4,8,16,32,64,128,256,512,50,50,50,150,150,150,100,100,100,123], 1023)),
    (([96,112,101,100,104,93,106,99,114,81,94], 503)),
])
def test(args):
    assert args[-1] == Solution().tallestBillboard(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
