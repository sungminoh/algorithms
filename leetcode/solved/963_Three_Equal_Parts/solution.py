#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array arr which consists of only zeros and ones, divide the array into three non-empty parts such that all of these parts represent the same binary value.

If it is possible, return any [i, j] with i + 1 < j, such that:

	arr[0], arr[1], ..., arr[i] is the first part,
	arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
	arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
	All three parts have equal binary values.

If it is not possible, return [-1, -1].

Note that the entire part is used when considering what binary value it represents. For example, [1,1,0] represents 6 in decimal, not 3. Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.

Example 1:
Input: arr = [1,0,1,0,1]
Output: [0,3]
Example 2:
Input: arr = [1,1,0,1,1]
Output: [-1,-1]
Example 3:
Input: arr = [1,1,0,0,1]
Output: [0,2]

Constraints:

	3 <= arr.length <= 3 * 104
	arr[i] is 0 or 1
"""
from pathlib import Path
import json
import sys
from typing import List
import pytest


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        """
        Time complexity: O(n * logn)
        Space complexity: O(1)
        """
        def bisearch(s, e, v, b):
            while s <= e:
                m = s + (e-s)//2
                tail = b % pow(2, (n-m))
                mid = b >> (n-m)
                if tail < v or mid > v:
                    e = m-1
                elif tail > v or mid < v:
                    s = m+1
                else:
                    return m
            return -1
        # calculate decimal value
        n = len(arr)
        b = 0
        two = 1
        for i in range(n):
            if arr[n-1-i]:
                b += two
            two *= 2
        # index: 0 1 2 3
        # power: 3 2 1 0
        # value: 8 4 2 1
        for i in range(n-2):
            val = b >> (n-i-1)
            j = bisearch(i+2, n-1, val, b=b%pow(2, n-i-1))
            if j>0:
                return [i, j]
        return [-1, -1]

    def threeEqualParts(self, arr: List[int]) -> List[int]:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        def decimal(arr):
            """calculate decimal value"""
            n = len(arr)
            b = 0
            two = 1
            for i in range(n):
                if arr[n-1-i]:
                    b += two
                two *= 2
            return b

        def find_splits_having_same_number_of_ones(arr, target):
            splits = []
            # find splits
            cnt = 0
            i = 0
            while cnt < 2*target:
                if arr[i] == 1:
                    cnt += 1
                    if cnt % target == 0:
                        splits.append(i)
                i += 1
            return splits

        n = len(arr)
        num_ones = sum(arr)
        # check invalid case
        if num_ones % 3:
            return [-1, -1]
        m = num_ones // 3
        # check trivial case
        if m == 0:
            return [0, n-1]
        splits = find_splits_having_same_number_of_ones(arr, m)
        # if the last part has trailing zeros,
        #  the first and the second part must have the same tailing zeros
        num_zeros = 0
        while n-1-num_zeros > splits[1] and arr[n-1-num_zeros] == 0:
            num_zeros += 1
        splits[0] += num_zeros
        splits[1] += num_zeros
        # calculate decimal value of each part
        b = decimal(arr)
        first = b >> (n-splits[0]-1)
        mid = (b%pow(2, n-splits[0]-1)) >> (n-splits[1]-1)
        third = b%pow(2, n-splits[1]-1)
        if first == mid == third:
            return [splits[0], splits[1]+1]
        return [-1, -1]


@pytest.mark.parametrize('arr, expected', [
    ([1,0,1,0,1], [0,3]),
    ([1,1,0,1,1], [-1,-1]),
    ([1,1,0,0,1], [0,2]),
    ([0,1,0,1,1], [1,4]),
    ([0,0,0], [0,2]),
    (json.load(open(Path(__file__).parent/'testcase.json')), [-1, -1]),
])
def test(arr, expected):
    assert expected == Solution().threeEqualParts(arr)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
