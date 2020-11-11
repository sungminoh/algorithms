#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement:

Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:

Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.

Example 2:

Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.

Note:

The n and k are in the range 1 <= k < n <= 104.
"""
import sys
from typing import List
import pytest


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        assert n > k
        ret = [1]
        sign = 1
        stride = k
        while stride:
            ret.append(ret[-1] + sign*stride)
            sign *= -1
            stride -= 1
        ret.extend(range(k+2, n+1))
        return ret


@pytest.mark.parametrize('n, k', [
    (3, 1),
    (3, 2),
    (100, 7),
])
def test(n, k):
    actual = Solution().constructArray(n, k)
    assert k == len(set(abs(actual[i] - actual[i+1]) for i in range(len(actual)-1)))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
