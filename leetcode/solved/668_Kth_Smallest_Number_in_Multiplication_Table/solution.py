#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.

Example 1:

Input: m = 3, n = 3, k = 5
Output: 3
Explanation: The 5th smallest number is 3.

Example 2:

Input: m = 2, n = 3, k = 6
Output: 6
Explanation: The 6th smallest number is 6.

Constraints:

	1 <= m, n <= 3 * 104
	1 <= k <= m * n
"""
import sys
from heapq import heappush
import pytest


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        """
        Time complexity: O(min(m, n) * log(n*m))
        Space complexity: O(1)
        """
        if n < m:
            return self.findKthNumber(n, m, k)

        def count_smaller_and_equal(v):
            smaller = 0
            equal = 0
            for _i in range(1, m+1):
                _j, r = divmod(v, _i)
                if _j > n:
                    smaller += n
                else:
                    if r == 0:
                        equal += 1
                        _j -= 1
                    smaller += _j
            return smaller, equal

        def binsearch(s, e):
            while s <= e:
                i = s + (e-s)//2
                smaller, equal = count_smaller_and_equal(i)
                if smaller < k <= smaller+equal:
                    return i
                elif k <= smaller:
                    e = i-1
                else:
                    s = i+1
            return 0  # Should not be reached

        return binsearch(1, m*n)


@pytest.mark.parametrize('m, n, k, expected', [
    (3, 3, 5, 3),
    (2, 3, 6, 6),
    (9, 9, 81, 81),
])
def test(m, n, k, expected):
    assert expected == Solution().findKthNumber(m, n, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
