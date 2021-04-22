#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).

In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.

Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements of arr equal.

Example 1:

Input: n = 3
Output: 2
Explanation: arr = [1, 3, 5]
First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].

Example 2:

Input: n = 6
Output: 9

Constraints:

	1 <= n <= 10^4
"""
import sys
import pytest


class Solution:
    def minOperations(self, n: int) -> int:
        """
        Time complexity: O(1)
        Space complexity: O(1)
        If n is odd, \sum_{k=1}^{(n-1)/2}{2k}
        else, \sum_{k=1}^{n/2}{2k-1}
        """
        pairs = n//2
        return pairs * (pairs+1) - (0 if n%2 else pairs)


@pytest.mark.parametrize('n, expected', [
    (3, 2),
    (6, 9),
])
def test(n, expected):
    assert expected == Solution().minOperations(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
