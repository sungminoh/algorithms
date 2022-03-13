#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:

	0 <= n <= 105

Follow up:

	It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
	Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""
import sys
from typing import List
import pytest


class Solution:
    def countBits(self, num: int) -> List[int]:
        """04/08/2020 22:44"""
        if num == 0:
            return [0]
        elif num == 1:
            return [0, 1]
        ret = [0, 1]
        k = 0
        for i in range(2, num + 1):
            if i & (i - 1) == 0:
                k = 0
            ret.append(ret[k] + 1)
            k += 1
        return ret

    def countBits(self, n: int) -> List[int]:
        ret = [0]
        #      0
        #      1
        #     10
        #     11
        #    100
        #    101
        #    110
        #    111
        j = 0
        for i in range(1, n+1):
            if i == i & ~(i-1): # if i is power of 2
                j = 0
            ret.append(1+ret[j])
            j += 1
        return ret


@pytest.mark.parametrize('n, expected', [
    (2, [0,1,1]),
    (5, [0,1,1,2,1,2]),
])
def test(n, expected):
    assert expected == Solution().countBits(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
