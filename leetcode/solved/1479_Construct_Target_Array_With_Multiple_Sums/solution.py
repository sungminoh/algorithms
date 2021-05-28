#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array target of n integers. From a starting array arr consisting of n 1's, you may perform the following procedure :

	let x be the sum of all elements currently in your array.
	choose index i, such that 0 <= i < n and set the value of arr at index i to x.
	You may repeat this procedure as many times as needed.

Return true if it is possible to construct the target array from arr, otherwise, return false.

Example 1:

Input: target = [9,3,5]
Output: true
Explanation: Start with arr = [1, 1, 1]
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done

Example 2:

Input: target = [1,1,1,2]
Output: false
Explanation: Impossible to create target array from [1,1,1,1].

Example 3:

Input: target = [8,5]
Output: true

Constraints:

	n == target.length
	1 <= n <= 5 * 104
	1 <= target[i] <= 109
"""
import math
import sys
from heapq import heappush
from heapq import heappop
from heapq import heapify
from typing import List
import pytest


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        """
        Think reversely
        Time complexity: O(log(n) * m)
            where n = len(target), m = size of each num
        Space complexity: O(n)
        """
        # an edge case
        if len(target) == 1:
            return target[0] == 1
        s = sum(target)
        h = [-x for x in target]
        heapify(h)
        while -h[0] > 1:
            # pop the biggest
            x = -heappop(h)
            s -= x
            # deduct as much as possible making sure that
            # x becomes smaller than the next biggest
            gap = x+h[0]
            if gap == 0:
                return False
            x -= s*(math.ceil(gap/s))
            if x < 1:
                return False
            # add back
            s += x
            heappush(h, -x)
        return True


@pytest.mark.parametrize('target, expected', [
    ([9,3,5], True),
    ([1,1,1,2], False),
    ([8,5], True),
    ([1,1000000000], True),
    ([9,9,9], False),
])
def test(target, expected):
    assert expected == Solution().isPossible(target)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
