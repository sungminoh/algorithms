#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a 0-indexed integer array mapping which represents the mapping rule of a shuffled decimal system. mapping[i] = j means digit i should be mapped to digit j in this system.

The mapped value of an integer is the new integer obtained by replacing each occurrence of digit i in the integer with mapping[i] for all 0 <= i <= 9.

You are also given another integer array nums. Return the array nums sorted in non-decreasing order based on the mapped values of its elements.

Notes:

	Elements with the same mapped values should appear in the same relative order as in the input.
	The elements of nums should only be sorted based on their mapped values and not be replaced by them.

Example 1:

Input: mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]
Output: [338,38,991]
Explanation:
Map the number 991 as follows:
1. mapping[9] = 6, so all occurrences of the digit 9 will become 6.
2. mapping[1] = 9, so all occurrences of the digit 1 will become 9.
Therefore, the mapped value of 991 is 669.
338 maps to 007, or 7 after removing the leading zeros.
38 maps to 07, which is also 7 after removing leading zeros.
Since 338 and 38 share the same mapped value, they should remain in the same relative order, so 338 comes before 38.
Thus, the sorted array is [338,38,991].

Example 2:

Input: mapping = [0,1,2,3,4,5,6,7,8,9], nums = [789,456,123]
Output: [123,456,789]
Explanation: 789 maps to 789, 456 maps to 456, and 123 maps to 123. Thus, the sorted array is [123,456,789].

Constraints:

	mapping.length == 10
	0 <= mapping[i] <= 9
	All the values of mapping[i] are unique.
	1 <= nums.length <= 3 * 104
	0 <= nums[i] < 109
"""
from typing import List
import pytest
import sys


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        """Jul 28, 2024 19:07"""
        def convert(v):
            if v == 0:
                return mapping[0]
            ret = 0
            p = 1
            while v:
                v, r = divmod(v, 10)
                ret += p * mapping[r]
                p *= 10
            return ret

        return [x for _, x in sorted(enumerate(nums), key=lambda x: (convert(x[1]), x[0]))]


@pytest.mark.parametrize('args', [
    (([8,9,4,0,2,1,3,5,7,6], [991,338,38], [338,38,991])),
    (([0,1,2,3,4,5,6,7,8,9], [789,456,123], [123,456,789])),
    (([9,8,7,6,5,4,3,2,1,0], [0,1,2,3,4,5,6,7,8,9], [9,8,7,6,5,4,3,2,1,0])),
])
def test(args):
    assert args[-1] == Solution().sortJumbled(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
