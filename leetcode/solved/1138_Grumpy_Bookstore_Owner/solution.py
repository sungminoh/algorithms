#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

Example 2:

Input: customers = [1], grumpy = [0], minutes = 1
Output: 1

Constraints:

	n == customers.length == grumpy.length
	1 <= minutes <= n <= 2 * 104
	0 <= customers[i] <= 1000
	grumpy[i] is either 0 or 1.
"""
from typing import List
import pytest
import sys


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        """Jun 26, 2024 23:37"""
        dissatisfaction = [c if g == 1 else 0 for c, g in zip(customers, grumpy)]
        saved = 0
        acc = 0
        i = 0
        for i in range(len(dissatisfaction)):
            acc += dissatisfaction[i]
            if i-minutes >= 0:
                acc -= dissatisfaction[i-minutes]
            saved = max(saved, acc)
        return sum(customers) - sum(dissatisfaction) + saved


@pytest.mark.parametrize('args', [
    (([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3, 16)),
    (([1], [0], 1, 1)),
    (([9,10,4,5], [1,0,1,1], 1, 19)),
])
def test(args):
    assert args[-1] == Solution().maxSatisfied(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
