#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001

Note:

	N will be an integer in the range [1, 30].
	K will be an integer in the range [1, 2^(N-1)].
"""
import sys
import pytest


class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        cnt = 0
        K -= 1
        while K:
            cnt += K%2
            K >>= 1
        return 0 if cnt % 2 == 0 else 1


@pytest.mark.parametrize('N, K, expected', [
    (1, 1, 0),
    (2, 1, 0),
    (2, 2, 1),
    (4, 5, 1),
    (3, 3, 1)
])
def test(N, K, expected):
    assert expected == Solution().kthGrammar(N, K)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
