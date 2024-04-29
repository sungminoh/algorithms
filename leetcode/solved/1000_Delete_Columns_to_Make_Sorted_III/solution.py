#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of n strings strs, all of the same length.

We may choose any deletion indices, and we delete all the characters in those indices for each string.

For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"].

Suppose we chose a set of deletion indices answer such that after deletions, the final array has every string (row) in lexicographic order. (i.e., (strs[0][0] <= strs[0][1] <= ... <= strs[0][strs[0].length - 1]), and (strs[1][0] <= strs[1][1] <= ... <= strs[1][strs[1].length - 1]), and so on). Return the minimum possible value of answer.length.

Example 1:

Input: strs = ["babca","bbazb"]
Output: 3
Explanation: After deleting columns 0, 1, and 4, the final array is strs = ["bc", "az"].
Both these rows are individually in lexicographic order (ie. strs[0][0] <= strs[0][1] and strs[1][0]  strs[1] - the array strs is not necessarily in lexicographic order.

Example 2:

Input: strs = ["edcba"]
Output: 4
Explanation: If we delete less than 4 columns, the only row will not be lexicographically sorted.

Example 3:

Input: strs = ["ghi","def","abc"]
Output: 0
Explanation: All rows are already lexicographically sorted.

Constraints:

	n == strs.length
	1 <= n <= 100
	1 <= strs[i].length <= 100
	strs[i] consists of lowercase English letters.
"""
from functools import lru_cache
from typing import List
import pytest
import sys


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """Apr 28, 2024 15:31"""
        N = len(strs[0])

        @lru_cache(None)
        def dp(i):
            if i == 0:
                return 0
            ret = i
            for j in range(i-1, -1, -1):
                if all(s[j] <= s[i] for s in strs):
                    ret = min(ret, dp(j) + i-j-1)
            return ret

        return min(dp(i) + N-i-1 for i in range(N))


@pytest.mark.parametrize('args', [
    ((["babca","bbazb"], 3)),
    ((["edcba"], 4)),
    ((["ghi","def","abc"], 0)),
    ((["baabab"], 2)),
])
def test(args):
    assert args[-1] == Solution().minDeletionSize(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
