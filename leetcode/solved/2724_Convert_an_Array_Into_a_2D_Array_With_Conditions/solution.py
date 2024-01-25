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
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

	The 2D array should contain only the elements of the array nums.
	Each row in the 2D array contains distinct integers.
	The number of rows in the 2D array should be minimal.

Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.

Example 1:

Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.

Example 2:

Input: nums = [1,2,3,4]
Output: [[4,3,2,1]]
Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.

Constraints:

	1 <= nums.length <= 200
	1 <= nums[i] <= nums.length
"""
import pytest
import sys


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        """Jan 24, 2024 19:34"""
        counter = Counter(nums)
        ret = []
        while counter:
            row = []
            for n in list(counter.keys()):
                row.append(n)
                counter[n] -= 1
                if counter[n] == 0:
                    counter.pop(n)
            ret.append(row)
        return ret


@pytest.mark.parametrize('args', [
    (([1,3,4,1,2,3,1], [[1,3,4,2],[1,3],[1]])),
    (([1,2,3,4], [[4,3,2,1]])),
])
def test(args):
    ans = Solution().findMatrix(*args[:-1])
    assert len(args[-1]) == len(ans)
    assert Counter(itertools.chain(*ans)) == Counter(args[0])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
