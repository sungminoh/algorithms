
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
On a table are N cards, with a positive integer printed on the front and back of each card (possibly different).

We flip any number of cards, and after we choose one card. 

If the number X on the back of the chosen card is not on the front of any card, then this number X is good.

What is the smallest number that is good?  If no number is good, output 0.

Here, fronts[i] and backs[i] represent the number on the front and back of card i. 

A flip swaps the front and back numbers, so the value on the front is now on the back and vice versa.

Example:

Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
Output: 2
Explanation: If we flip the second card, the fronts are [1,3,4,4,7] and the backs are [1,2,4,1,3].
We choose the second card, which has number 2 on the back, and it isn't on the front of any card, so 2 is good.

Note:
    1. 1 <= fronts.length == backs.length <= 1000.
    2. 1 <= fronts[i] <= 2000.
    3. 1 <= backs[i] <= 2000.
"""
import sys
from typing import List
import pytest


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        banned = set()
        for f, b in zip(fronts, backs):
            if f == b:
                banned.add(f)

        for i in range(len(fronts)):
            if backs[i] in banned or (fronts[i] not in banned and fronts[i] < backs[i]):
                fronts[i], backs[i] = backs[i], fronts[i]

        m = float('inf')
        for b in backs:
            if b not in banned:
                m = min(m, b)
        return m if m < float('inf') else 0


@pytest.mark.parametrize('fronts, backs, expected', [
    ([1,2,4,4,7], [1,3,4,1,3], 2),
    ([1], [1], 0),
    ([1,2], [1,1], 2),
])
def test(fronts, backs, expected):
    assert expected == Solution().flipgame(fronts, backs)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
