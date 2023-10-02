#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

	KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
	int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

Constraints:

	1 <= k <= 104
	0 <= nums.length <= 104
	-104 <= nums[i] <= 104
	-104 <= val <= 104
	At most 104 calls will be made to add.
	It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""
from heapq import heappop, heappush, heappushpop
from typing import List
import pytest
import sys


class KthLargest:
    """Apr 19, 2022 12:13"""
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.capacity = k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        while len(self.heap) > self.capacity:
            heappop(self.heap)
        return self.heap[0]


class KthLargest:
    """Sep 22, 2023 18:35"""
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = []
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heappush(self.h, val)
        else:
            if self.h[0] < val:
                heappushpop(self.h, val)
        return self.h[0]


@pytest.mark.parametrize('args', [
    ((["KthLargest", "add", "add", "add", "add", "add"],
      [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
      [None, 4, 5, 5, 8, 8])),
])
def test(args):
    commands, arguments, expecteds = args
    obj = globals()[commands.pop(0)](*arguments.pop(0))
    actual = []
    for cmd, arg in zip(commands, arguments):
        actual.append(getattr(obj, cmd)(*arg))
    assert expecteds[1:] == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
