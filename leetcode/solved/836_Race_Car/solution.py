#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

	When you get an instruction 'A', your car does the following:

		position += speed
		speed *= 2

	When you get an instruction 'R', your car does the following:

		If your speed is positive then speed = -1
		otherwise speed = 1

	Your position stays the same.

For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.

Given a target position target, return the length of the shortest sequence of instructions to get there.

Example 1:

Input: target = 3
Output: 2
Explanation:
The shortest instruction sequence is "AA".
Your position goes from 0 --> 1 --> 3.

Example 2:

Input: target = 6
Output: 5
Explanation:
The shortest instruction sequence is "AAARA".
Your position goes from 0 --> 1 --> 3 --> 7 --> 7 --> 6.

Constraints:

	1 <= target <= 104
"""
from collections import deque
import pytest
import sys


class Solution:
    def racecar(self, target: int) -> int:
        """Apr 15, 2024 22:57"""
        ret = 0
        q = deque([(0, 1)])
        seen = set()
        while q:
            for i in range(len(q)):
                pos, speed = q.popleft()
                if pos == target:
                    return ret
                for ps in [(pos+speed, speed*2), (pos, -1 if speed > 0 else 1)]:
                    if ps not in seen:
                        seen.add(ps)
                        q.append(ps)
            ret += 1
        return ret


@pytest.mark.parametrize('args', [
    ((3, 2)),
    ((6, 5)),
])
def test(args):
    assert args[-1] == Solution().racecar(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
