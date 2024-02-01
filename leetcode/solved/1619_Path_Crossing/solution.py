#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

Example 1:

Input: path = "NES"
Output: false
Explanation: Notice that the path doesn't cross any point more than once.

Example 2:

Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.

Constraints:

	1 <= path.length <= 104
	path[i] is either 'N', 'S', 'E', or 'W'.
"""
import pytest
import sys


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """Jan 31, 2024 23:35"""
        cur = (0, 0)
        visited = set([cur])
        for p in path:
            if p == 'N':
                cur = (cur[0], cur[1] + 1)
            if p == 'S':
                cur = (cur[0], cur[1] - 1)
            if p == 'E':
                cur = (cur[0] + 1, cur[1])
            if p == 'W':
                cur = (cur[0] - 1, cur[1])
            if cur in visited:
                return True
            visited.add(cur)
        return False


@pytest.mark.parametrize('args', [
    (("NES", False)),
    (("NESWW", True)),
])
def test(args):
    assert args[-1] == Solution().isPathCrossing(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
