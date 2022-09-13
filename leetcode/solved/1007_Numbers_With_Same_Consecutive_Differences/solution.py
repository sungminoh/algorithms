#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.

Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:

Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Constraints:

	2 <= n <= 9
	0 <= k <= 9
"""
from collections import deque
from typing import List
import pytest
import sys


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # bfs
        nums = list(range(1, 10))
        for _ in range(n-1):
            _nums = []
            for v in nums:
                if v%10 + k < 10:
                    _nums.append(v*10 + v%10+k)
                if k>0 and v%10 - k >= 0:
                    _nums.append(v*10 + v%10-k)
            nums = _nums
        return nums


@pytest.mark.parametrize('n, k, expected', [
    (3, 7, [181,292,707,818,929]),
    (2, 1, [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]),
    (2, 0, [11,22,33,44,55,66,77,88,99]),
])
def test(n, k, expected):
    assert sorted(expected) == sorted(Solution().numsSameConsecDiff(n, k))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
