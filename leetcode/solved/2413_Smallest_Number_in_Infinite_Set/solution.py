#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

	SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
	int popSmallest() Removes and returns the smallest integer contained in the infinite set.
	void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

Example 1:

Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.

Constraints:

	1 <= num <= 1000
	At most 1000 calls will be made in total to popSmallest and addBack.
"""
from heapq import heappop, heappush
import pytest
import sys


class SmallestInfiniteSet:
    """Sep 04, 2023 12:09"""
    def __init__(self):
        self.n = 1
        self.h = []
        self.s = set()

    def popSmallest(self) -> int:
        if self.h:
            n = heappop(self.h)
            self.s.discard(n)
            return n
        ret = self.n
        self.n += 1
        return ret

    def addBack(self, num: int) -> None:
        if num == self.n-1:
            self.n -= 1
        if num < self.n-1 and num not in self.s:
            self.s.add(num)
            heappush(self.h, num)


@pytest.mark.parametrize('args', [
    ((["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"],
      [[], [2], [], [], [], [1], [], [], []],
      [None, None, 1, 2, 3, None, 1, 4, 5])),
])
def test(args):
    obj = SmallestInfiniteSet()
    actual = []
    for cmd, arg in zip(*args[:-1]):
        if cmd == args[0][0]:
            continue
        actual.append(getattr(obj, cmd)(*arg))
    assert args[-1][1:] == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
