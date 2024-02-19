import itertools
from collections import Counter
from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:

Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

Constraints:

	1 <= arr.length <= 10^5
	1 <= arr[i] <= 10^9
	0 <= k <= arr.length
"""
import pytest
import sys


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """Feb 19, 2024 15:19"""
        cnt = Counter(arr)
        for i, c in enumerate(itertools.accumulate(sorted(list(cnt.values())))):
            if c > k:
                return len(cnt)-i
        return 0


@pytest.mark.parametrize('args', [
    (([5,5,4], 1, 1)),
    (([4,3,1,1,3,3,2], 3, 2)),
])
def test(args):
    assert args[-1] == Solution().findLeastNumOfUniqueInts(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
