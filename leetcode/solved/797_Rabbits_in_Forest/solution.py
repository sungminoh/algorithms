#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other rabbits have the same color as them. Those answers are placed in an array.

Return the minimum number of rabbits that could be in the forest.

Examples:
Input: answers = [1, 1, 2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Input: answers = [10, 10, 10]
Output: 11

Input: answers = []
Output: 0

Note:

	answers will have length at most 1000.
	Each answers[i] will be an integer in the range [0, 999].
"""
import sys
import math
from collections import Counter
from typing import List
import pytest


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = 0
        for k, v in Counter(answers).items():
            if k == 0:
                cnt += v
            else:
                q, r = divmod(v, k+1)
                cnt += (q + min(r, 1))*(k+1)
        return cnt


@pytest.mark.parametrize('answers, expected', [
    ([1,1,2], 5),
    ([10,10,10], 11),
    ([], 0),
    ([1,0,1,0,0], 5),
    ([0,0,1,1,1], 6),
])
def test(answers, expected):
    assert expected == Solution().numRabbits(answers)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
