#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design a data structure that efficiently finds the majority element of a given subarray.

The majority element of a subarray is an element that occurs threshold times or more in the subarray.

Implementing the MajorityChecker class:

	MajorityChecker(int[] arr) Initializes the instance of the class with the given array arr.
	int query(int left, int right, int threshold) returns the element in the subarray arr[left...right] that occurs at least threshold times, or -1 if no such element exists.

Example 1:

Input
["MajorityChecker", "query", "query", "query"]
[[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
Output
[null, 1, -1, 2]

Explanation
MajorityChecker majorityChecker = new MajorityChecker([1, 1, 2, 2, 1, 1]);
majorityChecker.query(0, 5, 4); // return 1
majorityChecker.query(0, 3, 3); // return -1
majorityChecker.query(2, 3, 2); // return 2

Constraints:

	1 <= arr.length <= 2 * 104
	1 <= arr[i] <= 2 * 104
	0 <= left <= right < arr.length
	threshold <= right - left + 1
	2 * threshold > right - left + 1
	At most 104 calls will be made to query.
"""
from functools import lru_cache
from pathlib import Path
import json
import bisect
from collections import defaultdict
from typing import List
import pytest
import sys


class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.value_pos = defaultdict(list)
        for i, n in enumerate(arr):
            self.value_pos[n].append(i)

    @lru_cache(None)
    def query(self, left: int, right: int, threshold: int) -> int:
        for v, pos in self.value_pos.items():
            j = bisect.bisect_right(pos, right)
            i = bisect.bisect_left(pos, left)
            cnt =  j - i + 1
            if cnt > threshold:
                return v
        return -1


@pytest.mark.parametrize('args', [
    ((
        ["MajorityChecker", "query", "query", "query"],
        [[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]],
        [None, 1, -1, 2],
    )),
    ((
        *json.load(open(Path(__file__).parent/'testcase.json')),
    ))
])
def test(args):
    commands, arguments, expecteds = args
    obj = globals()[commands[0]](*arguments[0])
    actual = [None]
    for cmd, arg in zip(commands[1:], arguments[1:]):
        actual.append(getattr(obj, cmd)(*arg))
    assert expecteds == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
