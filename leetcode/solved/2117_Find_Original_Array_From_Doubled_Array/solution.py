#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.

Example 1:

Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].

Example 2:

Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.

Example 3:

Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.

Constraints:

	1 <= changed.length <= 105
	0 <= changed[i] <= 105
"""
import itertools
from collections import defaultdict
from collections import Counter
from typing import List
import pytest
import sys


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ret = []
        counter = dict(Counter(changed))
        required = defaultdict(int)
        ret = []

        if counter.get(0, 0)%2 != 0:
            return []
        ret.extend([0]*(counter.pop(0, 0)//2))

        for n in counter.keys():
            if n%2 != 0:
                cnt = counter[n]
                required[n] += cnt
                required[2*n] += cnt
                if required[n] > counter[n] or required[2*n] > counter.get(2*n, 0):
                    return []
                else:
                    ret.extend([n]*cnt)

        for n in sorted(counter.keys()):
            if n%2 == 0 and required[n] < counter[n]:
                cnt = counter[n] - required[n]
                required[n] += cnt
                required[2*n] += cnt
                if required[2*n] > counter.get(2*n, 0):
                    return []
                else:
                    ret.extend([n]*cnt)

        return ret


@pytest.mark.parametrize('changed, expected', [
    ([1,3,4,2,6,8], [1,3,4]),
    ([6,3,0,1], []),
    ([1], []),
    ([0,0,0,0], [0, 0]),
    ([2,1,2,4,2,4], [1,2,2]),
    ([2,2,1,1], [1,1]),
    ([4,2], [2]),
])
def test(changed, expected):
    assert expected == Solution().findOriginalArray(changed)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
