#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:

Input: s = "eccbbbbdec"
Output: [10]

Constraints:

	1 <= s.length <= 500
	s consists of lowercase English letters.
"""
from collections import defaultdict
import sys
from typing import List
import pytest


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        """09/10/2020 00:40"""
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

    def partitionLabels(self, S: str) -> List[int]:
        """09/10/2020 00:51"""
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

    def partitionLabels(self, s: str) -> List[int]:
        index = {}
        for i, c in enumerate(s):
            index.setdefault(c, [i, i])
            index[c][1] = i

        ret = []
        l = 0
        r = 0
        for i, j in sorted(index.values()):
            if i > r:
                ret.append(r-l+1)
                l = i
            r = max(r, j)
        ret.append(len(s)-l)
        return ret


@pytest.mark.parametrize('s, expected', [
    ("ababcbacadefegdehijhklij", [9,7,8]),
    ("eccbbbbdec", [10]),
])
def test(s, expected):
    assert expected == Solution().partitionLabels(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
