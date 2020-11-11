#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".

Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.

Example 4:

Input: deadends = ["0000"], target = "8888"
Output: -1

Constraints:

	1 <= deadends.length <= 500
	deadends[i].length == 4
	target.length == 4
	target will not be in the list deadends.
	target and deadends[i] consist of digits only.
"""
import sys
from collections import deque
from typing import List
import pytest


class Solution:
    digits = list(range(10))
    def neighbor(self, t):
        for i in range(len(t)):
            r = list(t)
            r[i] = self.digits[(r[i]+1)%len(self.digits)]
            yield tuple(r)
            r[i] = self.digits[(r[i]-2)%len(self.digits)]
            yield tuple(r)

    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque()
        deadends = set(tuple(map(int, deadend)) for deadend in deadends)
        target = tuple(map(int, target))
        if (0,0,0,0) in deadends:
            return -1
        if (0,0,0,0) == target:
            return 0
        q.append(((0,0,0,0), 0))
        visited = set([(0,0,0,0)])
        while q:
            e, d = q.popleft()
            for n in self.neighbor(e):
                if n in deadends or n in visited:
                    continue
                if n == target:
                    return d+1
                q.append((n, d+1))
                visited.add(n)
        return -1


@pytest.mark.parametrize('deadends, target, expected', [
    (["0201","0101","0102","1212","2002"], "0202", 6),
    (["8888"], "0009", 1),
    (["8887","8889","8878","8898","8788","8988","7888","9888"], "8888", -1),
    (["0000"], "8888", -1),
])
def test(deadends, target, expected):
    assert expected == Solution().openLock(deadends, target)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
