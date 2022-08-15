#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are buckets buckets of liquid, where exactly one of the buckets is poisonous. To figure out which one is poisonous, you feed some number of (poor) pigs the liquid to see whether they will die or not. Unfortunately, you only have minutesToTest minutes to determine which bucket is poisonous.

You can feed the pigs according to these steps:

	Choose some live pigs to feed.
	For each pig, choose which buckets to feed it. The pig will consume all the chosen buckets simultaneously and will take no time.
	Wait for minutesToDie minutes. You may not feed any other pigs during this time.
	After minutesToDie minutes have passed, any pigs that have been fed the poisonous bucket will die, and all others will survive.
	Repeat this process until you run out of time.

Given buckets, minutesToDie, and minutesToTest, return the minimum number of pigs needed to figure out which bucket is poisonous within the allotted time.

Example 1:
Input: buckets = 1000, minutesToDie = 15, minutesToTest = 60
Output: 5
Example 2:
Input: buckets = 4, minutesToDie = 15, minutesToTest = 15
Output: 2
Example 3:
Input: buckets = 4, minutesToDie = 15, minutesToTest = 30
Output: 2

Constraints:

	1 <= buckets <= 1000
	1 <= minutesToDie <= minutesToTest <= 100
"""
from functools import lru_cache
import sys
import math
import pytest


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        """10/24/2020 20:58
        Each pig can find from steps+1 groups
        Time Complexity: O(log(buckets))
        Space Complexity: O(1)
        """
        t = minutesToTest // minutesToDie + 1
        i = 0
        c = 1
        while c < buckets:
            c *= t
            i += 1
        return i

    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        """10/24/2020 20:59
        Each pig can find from steps+1 groups
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        l = math.log(buckets)/math.log(minutesToTest // minutesToDie + 1)
        if l > int(l):
            l += 1
        return int(l)

    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        """08/15/2022 10:21
        Time Complexity: O(log(bucket)*steps)
            bisearch: O(log(log(bucket)) * tc(max_bucket cached))
            max_bucket: O(log(bucket)*steps)
        Space Complexity: O(log(bucket)*steps)
        """
        @lru_cache(None)
        def max_buckets(pigs, steps):
            if steps == 1:
                return 2**pigs
            ret = 0
            for n in range(pigs+1):
                comb = math.comb(pigs, n)
                ret += comb * max_buckets(pigs-n, steps-1)
            return ret

        steps = minutesToTest//minutesToDie
        def bisearch(s, e, func):
            while s<=e:
                m = s + (e-s)//2
                if func(m):
                    s = m+1
                else:
                    e = m-1
            return s-1

        return bisearch(0, int(math.log2(buckets))+1, lambda x: max_buckets(x, steps) < buckets) + 1


@pytest.mark.parametrize('buckets, minutesToDie, minutesToTest, expected', [
    (1000, 15, 60, 5),
    (4, 15, 15, 2),
    (4, 15, 30, 2),
])
def test(buckets, minutesToDie, minutesToTest, expected):
    assert expected == Solution().poorPigs(buckets, minutesToDie, minutesToTest)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
