
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:
    1. 1 <= w.length <= 10000
    2. 1 <= w[i] <= 10^5
    3. pickIndex will be called at most 10000 times.

Example 1:

Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]

Example 2:

Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""
from pathlib import Path
import json
import sys
from collections import Counter
import random
from typing import List
import pytest


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
    def __init__(self, w: List[int]):
        self.cumsum = [0]
        for v in w:
            self.cumsum.append(self.cumsum[-1] + v)

    def pickIndex(self) -> int:
        return binsearch(self.cumsum, random.randrange(0, self.cumsum[-1]))



def read_testcase(fname):
    with open(fname, 'r') as f:
        return json.load(f)[1][0][0]



@pytest.mark.parametrize('w', [
    ([1]),
    ([1,3]),
    (read_testcase(Path(__file__).parent/'testcase.json'))
])
def test(w):
    print()
    s = Solution(w)
    cnt = Counter(s.pickIndex() for _ in range(100000))
    print(cnt)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
