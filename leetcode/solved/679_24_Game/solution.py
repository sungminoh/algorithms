#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array cards of length 4. You have four cards, each containing a number in the range [1, 9]. You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.

You are restricted with the following rules:

	The division operator '/' represents real division, not integer division.

		For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.

	Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.

		For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.

	You cannot concatenate numbers together

		For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.

Return true if you can get such expression that evaluates to 24, and false otherwise.

Example 1:

Input: cards = [4,1,8,7]
Output: true
Explanation: (8-4) * (7-1) = 24

Example 2:

Input: cards = [1,2,1,2]
Output: false

Constraints:

	cards.length == 4
	1 <= cards[i] <= 9
"""
import math
from functools import lru_cache
from typing import List
import pytest
import sys


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def split(arr, n):
            if n == 0:
                yield tuple(), arr
            else:
                visited = set()
                for i in range(len(arr)):
                    one = arr[i]
                    rest = arr[:i] + arr[i+1:]
                    for l1, l2 in split(rest, n-1):
                        r1, r2 = sorted((*l1, one)), sorted(l2)
                        k = (tuple(r1), tuple(r2))
                        if k not in visited:
                            visited.add(k)
                            yield k

        def make(nums):
            if len(nums) == 1:
                yield nums[0]
            else:
                for i in range(1, len(nums)//2 + 1):
                    for l1, l2 in split(nums, i):
                        for n1 in make(l1):
                            for n2 in make(l2):
                                yield from (n1+n2, n1-n2, n2-n1, n1*n2)
                                if n2 > 0:
                                    yield n1/n2
                                if n1 > 0:
                                    yield n2/n1

        return any(math.isclose(x, 24) for x in make(tuple(cards)))


@pytest.mark.parametrize('cards, expected', [
    ([4,1,8,7], True),
    ([1,2,1,2], False),
    ([3,3,8,8], True),
])
def test(cards, expected):
    assert expected == Solution().judgePoint24(cards)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
