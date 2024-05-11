#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

Example 1:

Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation: Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".

Example 2:

Input: s1 = "xy", s2 = "yx"
Output: 2
Explanation: Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
Note that you cannot swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.

Example 3:

Input: s1 = "xx", s2 = "xy"
Output: -1

Constraints:

	1 <= s1.length, s2.length <= 1000
	s1.length == s2.length
	s1, s2 only contain 'x' or 'y'.
"""
from collections import defaultdict
import pytest
import sys


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        """May 11, 2024 17:22"""
        c_counts = defaultdict(int)
        p_counts = defaultdict(int)
        for c1, c2 in zip(s1, s2):
            if c1 == c2:
                continue
            c_counts[c1] += 1
            c_counts[c2] += 1
            p_counts[c1, c2] += 1
        if not all(x%2 == 0 for x in c_counts.values()):
            return -1
        return sum((x+1)//2 for x in p_counts.values())


@pytest.mark.parametrize('args', [
    (("xx", "yy", 1)),
    (("xy", "yx", 2)),
    (("xx", "xy", -1)),
    (("xxyyxyxyxx",
      "xyyxyxxxyx", 4)),
    (("xyxyyx",
      "yxyxxy", 4)),
])
def test(args):
    assert args[-1] == Solution().minimumSwap(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
