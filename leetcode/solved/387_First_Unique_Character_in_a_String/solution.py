from collections import Counter

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
import pytest
import sys


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """Aug 28, 2022 14:09"""
        cnt = Counter(s)
        for i, c in enumerate(s):
            if cnt.get(c) == 1:
                return i
        return -1

    def firstUniqChar(self, s: str) -> int:
        """Feb 19, 2024 12:25"""
        seen = {}
        for i, c in enumerate(s):
            if c in seen:
                seen[c] = float('inf')
            else:
                seen[c] = i
        ret = min(seen.values())
        return ret if ret != float('inf') else -1


@pytest.mark.parametrize('args', [
    (("leetcode", 0)),
    (("loveleetcode", 2)),
    (("aabb", -1)),
])
def test(args):
    assert args[-1] == Solution().firstUniqChar(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
