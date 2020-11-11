#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

	S will have length in range [1, 500].
	S will consist of lowercase English letters ('a' to 'z') only.
"""
from collections import defaultdict
import sys
from typing import List
import pytest


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return []

        m = defaultdict(int)
        for i, c in enumerate(S):
            m[c] = max(m[c], i)

        s = 0
        e = 0
        ret = []
        for i, c in enumerate(S):
            if i > e:
                ret.append(i-s)
                s = i
                e = m[c]
            else:
                e = max(e, m[c])
        ret.append(len(S)-s)
        return ret

    def _partitionLabels(self, S: str) -> List[int]:
        minmax = dict()
        for i, c in enumerate(S):
            minmax.setdefault(c, [i, i])
            minmax[c][0] = min(minmax[c][0], i)
            minmax[c][1] = max(minmax[c][1], i)

        intervals = list(sorted(minmax.values()))
        ret = [intervals[0]]
        for interval in intervals[1:]:
            if ret and ret[-1][1] > interval[0]:
                ret[-1][1] = max(ret[-1][1], interval[1])
            else:
                ret.append(interval)
        return [e-s+1 for s, e in ret]


@pytest.mark.parametrize('S, expected', [
    ("ababcbacadefegdehijhklij", [9,7,8]),
])
def test(S, expected):
    assert expected == Solution().partitionLabels(S)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
