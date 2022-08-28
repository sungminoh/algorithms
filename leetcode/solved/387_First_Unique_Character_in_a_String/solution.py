#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0
Example 2:
Input: s = "loveleetcode"
Output: 2
Example 3:
Input: s = "aabb"
Output: -1

Constraints:

	1 <= s.length <= 105
	s consists of only lowercase English letters.
"""
import sys
from collections import Counter
from collections import defaultdict
import pytest


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for i, c in enumerate(s):
            if cnt.get(c) == 1:
                return i
        return -1


@pytest.mark.parametrize('s, expected', [
    ("leetcode", 0),
    ("loveleetcode", 2),
    ("aabb", -1),
])
def test(s, expected):
    assert expected == Solution().firstUniqChar(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
