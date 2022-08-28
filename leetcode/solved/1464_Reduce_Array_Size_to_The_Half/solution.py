#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.

Example 2:

Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.

Constraints:

	2 <= arr.length <= 105
	arr.length is even.
	1 <= arr[i] <= 105
"""
import sys
from collections import Counter
from typing import List
import pytest


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        ret = 0
        s = 0
        for _, c in cnt.most_common(n=len(arr)):
            s += c
            ret += 1
            if s >= (len(arr)+1)//2:
                break
        return ret

    def minSetSize(self, arr: List[int]) -> int:
        """08/11/2021 13:30"""
        n = len(arr)
        cnt = Counter(arr)
        ret = 0
        s = 0
        for _, ct in cnt.most_common():
            s += ct
            ret += 1
            if n <= 2*s:
                break
        return ret


@pytest.mark.parametrize('arr, expected', [
    ([3,3,3,3,5,5,5,2,2,7], 2),
    ([7,7,7,7,7,7], 1),
    ([1,9], 1),
    ([1000,1000,3,7], 1),
    ([1,2,3,4,5,6,7,8,9,10], 5),
])
def test(arr, expected):
    assert expected == Solution().minSetSize(arr)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
