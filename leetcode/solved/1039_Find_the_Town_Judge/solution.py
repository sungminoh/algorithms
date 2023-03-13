#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

	The town judge trusts nobody.
	Everybody (except for the town judge) trusts the town judge.
	There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Constraints:

	1 <= n <= 1000
	0 <= trust.length <= 104
	trust[i].length == 2
	All the pairs of trust are unique.
	ai != bi
	1 <= ai, bi <= n
"""
from typing import List
import pytest
import sys


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """Jan 28, 2022 23:23"""
        cnt = {i: 0 for i in range(1, n+1)}
        for a, b in trust:
            if a in cnt:
                cnt.pop(a)
            if b in cnt:
                cnt[b] += 1
        # if len(cnt) == 1:
            # return next(iter(cnt.keys()))
        for k, v in cnt.items():
            if v == n-1:
                return k
        return -1

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """Mar 11, 2023 14:42"""
        judge = [True]*n
        counter = [0]*n
        for a, b in trust:
            judge[a-1] = False
            counter[b-1] += 1
        for i, (j, c) in enumerate(zip(judge, counter), 1):
            if j and c == n-1:
                return i
        return -1


@pytest.mark.parametrize('args', [
    ((2, [[1,2]], 2)),
    ((3, [[1,3],[2,3]], 3)),
    ((3, [[1,3],[2,3],[3,1]], -1)),
    ((3, [[1,2],[2,3]], -1)),
])
def test(args):
    assert args[-1] == Solution().findJudge(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
