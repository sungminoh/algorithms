#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are 1000 buckets, one and only one of them is poisonous, while the rest are filled with water. They all look identical. If a pig drinks the poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket is poisonous within one hour?

Answer this question, and write an algorithm for the general case.

General case:

If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the poisonous bucket within p minutes? There is exactly one bucket with poison.

Note:

	A pig can be allowed to drink simultaneously on as many buckets as one would like, and the feeding takes no time.
	After a pig has instantly finished drinking buckets, there has to be a cool down time of m minutes. During this time, only observation is allowed and no feedings at all.
	Any given bucket can be sampled an infinite number of times (by an unlimited number of pigs).
"""
import sys
import math
import pytest


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        l = math.log(buckets)/math.log(minutesToTest // minutesToDie + 1)
        if l > int(l):
            l += 1
        return int(l)


@pytest.mark.parametrize('buckets, minutesToDie, minutesToTest, expected', [
    (1000, 15, 60, 5),
    (4, 15, 15, 2)
])
def test(buckets, minutesToDie, minutesToTest, expected):
    assert expected == Solution().poorPigs(buckets, minutesToDie, minutesToTest)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
