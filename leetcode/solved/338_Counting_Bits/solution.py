#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""

import pytest
from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
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



def count_one(n):
    cnt = 0
    while n:
        if n % 2:
            cnt += 1
        n //= 2
    return cnt


@pytest.mark.parametrize('num', [
    0,1,2,3,4,5,6,7,8,9,10
])
def test(num):
    assert [count_one(i) for i in range(num + 1)] == Solution().countBits(num)
