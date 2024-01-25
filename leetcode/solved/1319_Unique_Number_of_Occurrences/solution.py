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
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:

Input: arr = [1,2]
Output: false

Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Constraints:

	1 <= arr.length <= 1000
	-1000 <= arr[i] <= 1000
"""
import pytest
import sys


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        return len(set(counter.values())) == len(counter)


@pytest.mark.parametrize('args', [
    (([1,2,2,1,1,3], True)),
    (([1,2], False)),
    (([-3,0,1,-3,1,1,1,-3,10,0], True)),
])
def test(args):
    assert args[-1] == Solution().uniqueOccurrences(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
