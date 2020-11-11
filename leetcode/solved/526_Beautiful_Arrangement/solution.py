#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1

	The number at the ith position is divisible by i.
	i is divisible by the number at the ith position.

Now given N, how many beautiful arrangements can you construct?

Example 1:

Input: 2
Output: 2
Explanation:

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.

Note:

	N is a positive integer and will not exceed 15.
"""
import sys
from functools import lru_cache
import pytest


def iter_binary(n):
    while n:
        yield n % 2
        n //= 2


class Solution:
    def countArrangement(self, N: int) -> int:
        @lru_cache(None)
        def count(i, b):
            if i == N:
                return 1
            s = 0
            for j, c in enumerate(iter_binary(b)):
                if c == 0:
                    continue
                if (j+1) % (i+1) == 0 or (i+1) % (j+1) == 0:
                    b ^= 2 ** j
                    s += count(i + 1, b)
                    b |= 2 ** j
            return s

        b = 2**N - 1
        return count(0, b)


@pytest.mark.parametrize('N, expected', [
    (2, 2),
])
def test(N, expected):
    assert expected == Solution().countArrangement(N)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
