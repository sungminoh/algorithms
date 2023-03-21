#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The array-form of an integer num is an array representing its digits in left to right order.

	For example, for num = 1321, the array form is [1,3,2,1].

Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Example 2:

Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Example 3:

Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021

Constraints:

	1 <= num.length <= 104
	0 <= num[i] <= 9
	num does not contain any leading zeros except for the zero itself.
	1 <= k <= 104
"""
from typing import List
import pytest
import sys


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        """Mar 20, 2023 23:25"""
        c = 0
        i = len(num)-1
        while i >= 0 or k:
            c, x = divmod((num[i] if i>=0 else 0) + k%10 + c, 10)
            print(x)
            if i >= 0:
                num[i] = x
            else:
                num.insert(0, x)
            k //= 10
            i -= 1
        if c:
            num.insert(0, c)
        return num


@pytest.mark.parametrize('args', [
    (([1,2,0,0], 34, [1,2,3,4])),
    (([2,7,4], 181, [4,5,5])),
    (([2,1,5], 806, [1,0,2,1])),
    (([9,9,9,9,9,9,9,9,9,9], 1, [1,0,0,0,0,0,0,0,0,0,0])),
    (([0], 23, [2,3])),
    (([9,3], 636, [7,2,9])),
])
def test(args):
    assert args[-1] == Solution().addToArrayForm(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
