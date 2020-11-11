
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:

Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

Note:

Elements of the given array are in the range of 0  to 10^9
Length of the array will not exceed 10^4.
"""
import sys
from typing import List
import pytest


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        positions = []
        for n in nums:
            for i, b in enumerate(reversed(bin(n)[2:])):
                if i >= len(positions):
                    positions.append(0)
                positions[i] += int(b)
        print(positions)
        return sum(p * (size - p) for p in positions)


@pytest.mark.parametrize('nums, expected', [
    ([4, 14, 2], 6),
])
def test(nums, expected):
    assert expected == Solution().totalHammingDistance(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
