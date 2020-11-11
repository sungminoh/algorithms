
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A magical string S consists of only '1' and '2' and obeys the following rules:

The string S is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string S itself.

The first few elements of string S is the following:
S = "1221121221221121122……"

If we group the consecutive '1's and '2's in S, it will be:

1   22  11  2  1  22  1  22  11  2  11  22 ......

and the occurrences of '1's or '2's in each group are:

1   2	   2    1   1    2     1    2     2    1    2    2 ......

You can see that the occurrence sequence above is the S itself.

Given an integer N as input, return the number of '1's in the first N number in the magical string S.

Note:
N will not exceed 100,000.

Example 1:

Input: 6
Output: 3
Explanation: The first 6 elements of magical string S is "12211" and it contains three 1's, so return 3.
"""
import sys
from collections import deque
import pytest


class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        ret = 1
        s = deque([1])
        count = 1
        for _ in range(1, n):
            if count < s[0]:
                count += 1
                s.append(s[-1])
            else:
                count = 1
                s.append((s[-1] % 2) + 1)
                s.popleft()
            if s[-1] == 1:
                ret += 1
        return ret


@pytest.mark.parametrize('n, expected', [
    (0, 0),
    (6, 3),
    (10,5)
])
def test(n, expected):
    print()
    assert expected == Solution().magicalString(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
