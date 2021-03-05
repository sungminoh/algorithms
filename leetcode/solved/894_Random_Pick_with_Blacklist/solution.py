#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a blacklist B containing unique integers from [0, N), write a function to return a uniform random integer from [0, N) which is NOT in B.

Optimize it such that it minimizes the call to system’s Math.random().

Note:

	1 <= N <= 1000000000
	0 <= B.length < min(100000, N)
	[0, N) does NOT include N. See interval notation.

Example 1:

Input:
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
Output: [null,0,0,0]

Example 2:

Input:
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
Output: [null,1,1,1]

Example 3:

Input:
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
Output: [null,0,0,2]

Example 4:

Input:
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
Output: [null,1,3,1]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, N and the blacklist B. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""
from collections import defaultdict
import sys
import random
import bisect
from typing import List
import pytest


class Solution:
    def __init__(self, N: int, blacklist: List[int]):
        self.mp = {b: -1 for b in blacklist}
        self.n = N - len(blacklist)
        for b in blacklist:
            if b >= self.n:
                continue
            while N-1 in self.mp:
                N -= 1
            self.mp[b] = N-1
            N -= 1

    def pick(self) -> int:
        n = random.randrange(0, self.n)
        return self.mp.get(n, n)


@pytest.mark.parametrize('N, blacklist', [
    (1,[]),
    (2,[]),
    (3,[1]),
    (4,[2]),
    (5, [2, 0]),
    (3, [0, 1]),
    (3, [0]),
    (4, [0, 2]),
])
def test(N, blacklist):
    obj = Solution(N, blacklist)
    s = set(blacklist)
    cnt = defaultdict(int)
    print(obj.mp)
    for i in range(10000):
        picked = obj.pick()
        assert picked not in s
        cnt[picked] += 1
    print(cnt)
    assert N - len(blacklist) == len(cnt)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
