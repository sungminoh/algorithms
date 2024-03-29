#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A program was supposed to print an array of integers. The program forgot to print whitespaces and the array is printed as a string of digits s and all we know is that all integers in the array were in the range [1, k] and there are no leading zeros in the array.

Given the string s and the integer k, return the number of the possible arrays that can be printed as s using the mentioned program. Since the answer may be very large, return it modulo 109 + 7.

Example 1:

Input: s = "1000", k = 10000
Output: 1
Explanation: The only possible array is [1000]

Example 2:

Input: s = "1000", k = 10
Output: 0
Explanation: There cannot be an array that was printed this way and has all integer >= 1 and <= 10.

Example 3:

Input: s = "1317", k = 2000
Output: 8
Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]

Constraints:

	1 <= s.length <= 105
	s consists of only digits and does not contain leading zeros.
	1 <= k <= 109
"""
from functools import lru_cache
import pytest
import sys


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        """Sep 04, 2023 11:55"""
        MOD = int(1e9+7)

        @lru_cache(None)
        def dp(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            ret = 0
            n = 0
            for j in range(i, len(s)):
                n = 10*n+int(s[j])
                if n > k:
                    return ret
                ret += dp(j+1)
                ret %= MOD
            return ret

        return dp(0)


@pytest.mark.parametrize('args', [
    (("1000", 10000, 1)),
    (("1000", 10, 0)),
    (("1317", 2000, 8)),
])
def test(args):
    assert args[-1] == Solution().numberOfArrays(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
