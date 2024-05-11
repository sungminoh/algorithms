#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

	For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.

Example 2:

Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.

Constraints:

	1 <= w.length <= 104
	1 <= w[i] <= 105
	pickIndex will be called at most 104 times.
"""
import bisect
import random
import itertools
from typing import List
import pytest
import sys


def binsearch(arr, v):
    s, e = 0, len(arr) - 1
    while s <= e:
        m = s + ((e-s)//2)
        if v < arr[m]:
            e = m - 1
        elif v > arr[m]:
            s = m + 1
        else:
            return m
    return e


class Solution:
    """Jun 01, 2020 13:04"""
    def __init__(self, w: List[int]):
        self.cumsum = [0]
        for v in w:
            self.cumsum.append(self.cumsum[-1] + v)

    def pickIndex(self) -> int:
        return binsearch(self.cumsum, random.randrange(0, self.cumsum[-1]))


class Solution:
    """May 11, 2024 17:43"""
    def __init__(self, w: List[int]):
        self.weights = list(itertools.accumulate(w))

    def pickIndex(self) -> int:
        v = random.randint(1, self.weights[-1])
        return bisect.bisect_left(self.weights, v)


@pytest.mark.parametrize('args', [
    ((["Solution","pickIndex"],
      [[[1]],[]],
      [None,0])),
    ((["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"],
      [[[1,3]],[],[],[],[],[]],
      [None,1,1,1,1,0])),
])
def test(args):
    commands, arguments, expecteds = args
    obj = globals()[commands.pop(0)](*arguments.pop(0))
    actual = [None]
    for cmd, arg in zip(commands, arguments):
        actual.append(getattr(obj, cmd)(*arg))
    assert expecteds == actual



if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
