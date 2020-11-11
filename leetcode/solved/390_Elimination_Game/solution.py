
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
"""
import pytest


class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 2
        elif n == 4:
            return 2
        elif n == 5:
            return 2
        elif n == 6:
            return 4
        if (2*(n//2)) % 4 == 0:
            return 4 * self.lastRemaining(n // 4) - 2
        else:
            return 4 * self.lastRemaining(n // 4)


    def _lastRemaining(self, n: int) -> int:
        # 1 -> 1
        # 1 2 -> 2
        # 1 2 3 -> 2
        # 1 2 3 4 -> 2
        # 1 2 3 4 5 -> 2
        # 1 2 3 4 5 6  -> 4
        # 1 2 3 4 5 6 7 -> 4
        # 1 2 3 4 5 6 7 8 -> 6
        # 1 2 3 4 5 6 7 8 9 -> 6
        # 1 2 3 4 5 6 7 8 9 10 -> 8
        # 1 2 3 4 5 6 7 8 9 10 11 -> 8
        # 1 2 3 4 5 6 7 8 9 10 11 12 -> 6
        # 1 2 3 4 5 6 7 8 9 10 11 12 13 -> 6
        #
        # 1 2 3 4 5 6 7 ... 28
        # 2 4 6 8 10 12 or 14
        # 2 6 10 14 18 22, 26... or 4 8 12 16 20 24, 28

        # 1 2 3 4 5 6 7
        # 2 4 6
        # 4

        nums = list(range(1, n + 1))
        i = 0
        while len(nums) > 1:
            if i % 2 == 0:
                nums = nums[1::2]
            else:
                nums = nums[len(nums) % 2::2]
            i += 1
        return nums[0]


@pytest.mark.parametrize('n, expected', [
    (1, 1),
    (2, 2),
    (3, 2),
    (4, 2),
    (5, 2),
    (6, 4),
    (7, 4),
    (8, 6),
    (9, 6),
    (10, 8),
    (11, 8),
    (12, 6),
    (13, 6),
    (1047, 344),
    (100000000, 32896342),
])
def test_fixed(n, expected):
    assert expected == Solution().lastRemaining(n)

def test():
    for i in range(1, 100):
        print(i)
        assert Solution()._lastRemaining(i) == Solution().lastRemaining(i)
