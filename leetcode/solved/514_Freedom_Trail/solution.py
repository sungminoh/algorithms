#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring", and use the dial to spell a specific keyword in order to open the door.

Given a string ring, which represents the code engraved on the outer ring and another string key, which represents the keyword needs to be spelled. You need to find the minimum number of steps in order to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at 12:00 direction. You need to spell all the characters in the string key one by one by rotating the ring clockwise or anticlockwise to make each character of the string key aligned at 12:00 direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:

	You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step. The final purpose of the rotation is to align one of the string ring's characters at the 12:00 direction, where this character must equal to the character key[i].
	If the character key[i] has been aligned at the 12:00 direction, you need to press the center button to spell, which also counts as 1 step. After the pressing, you could begin to spell the next character in the key (next stage), otherwise, you've finished all the spelling.

Example:

Input: ring = "godding", key = "gd"
Output: 4
Explanation:
For the first key character 'g', since it is already in place, we just need 1 step to spell this character.
For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
Also, we need 1 more step for spelling.
So the final output is 4.

Note:

	Length of both ring and key will be in range 1 to 100.
	There are only lowercase letters in both strings and might be some duplcate characters in both strings.
	It's guaranteed that string key could always be spelled by rotating the string ring.
"""
from functools import lru_cache
import sys
from collections import defaultdict
import pytest


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # recursion
        n = len(ring)
        index = defaultdict(list)
        for i, c in enumerate(ring):
            index[c].append(i)

        @lru_cache(None)
        def rec(i, cur):
            if i == len(key):
                return 0
            left = (n, cur)
            right = (n, cur)
            for j in index[key[i]]:
                left = min(left, ((n+cur-j) % n, j))
                right = min(right, ((n+j-cur) % n, j))
            return min(rec(i+1, left[1]) + left[0], rec(i+1, right[1]) + right[0])

        return rec(0, 0) + len(key)

    def findRotateSteps(self, ring: str, key: str) -> int:
        # iteration
        n = len(ring)
        index = defaultdict(list)
        for i, c in enumerate(ring):
            index[c].append(i)

        memo = {0: 0}
        for i, c in enumerate(key):
            new_memo = {}
            for cur, cost in memo.items():
                for j in index[c]:
                    steps = min((n+cur-j) % n, (n+j-cur) % n)
                    new_memo[j] = min(new_memo.get(j, float('inf')), cost + steps)
            memo = new_memo

        return min(memo.values()) + len(key)


@pytest.mark.parametrize('ring, key, expected', [
    ("godding", "gd", 4),
    ("caotmcaataijjxi", "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx", 137),
])
def test(ring, key, expected):
    assert expected == Solution().findRotateSteps(ring, key)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
