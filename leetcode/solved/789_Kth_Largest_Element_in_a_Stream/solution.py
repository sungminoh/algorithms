#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

Implement the KthLargest class:

	KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
	int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.

Example 1:

Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

Output: [null, 4, 5, 5, 8, 8]

Explanation:

KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3); // return 4
kthLargest.add(5); // return 5
kthLargest.add(10); // return 5
kthLargest.add(9); // return 8
kthLargest.add(4); // return 8

Example 2:

Input:
["KthLargest", "add", "add", "add", "add"]
[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

Output: [null, 7, 7, 7, 8]

Explanation:
KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
kthLargest.add(2); // return 7
kthLargest.add(10); // return 7
kthLargest.add(9); // return 7
kthLargest.add(9); // return 8

Constraints:

	0 <= nums.length <= 104
	1 <= k <= nums.length + 1
	-104 <= nums[i] <= 104
	-104 <= val <= 104
	At most 104 calls will be made to add.
"""
from typing import List
import pytest
import sys
from heapq import heapify, heappop, heappush, heappushpop


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


class KthLargest:
    """Nov 06, 2024 15:32"""
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = nums
        heapify(self.h)
        while len(self.h) > self.k:
            heappop(self.h)

    def add(self, val: int) -> int:
        heappush(self.h, val)
        if len(self.h) > self.k:
            heappop(self.h)
        if len(self.h) == self.k:
            return self.h[0]


@pytest.mark.parametrize('args', [
    ((
        ["KthLargest", "add", "add", "add", "add", "add"],
        [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
        [None, 4, 5, 5, 8, 8]
    )),
    ((
        ["KthLargest", "add", "add", "add", "add"],
        [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]],
        [None, 7, 7, 7, 8]
    )),
    ((["KthLargest","add","add","add","add","add"],
      [[1,[]],[-3],[-2],[-4],[0],[4]],
      [None,-3,-2,-2,0,4])),
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
