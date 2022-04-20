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
import sys
from heapq import heappop
from heapq import heappush
from typing import List
import pytest


class KthLargest:
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


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["KthLargest", "add", "add", "add", "add", "add"],
     [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
     [None, 4, 5, 5, 8, 8]),
])
def test(commands, arguments, expecteds):
    obj = globals()[commands[0]](*arguments[0])
    for cmd, arg, exp in zip(commands[1:], arguments[1:], expecteds[1:]):
        assert exp == getattr(obj, cmd)(*arg)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
