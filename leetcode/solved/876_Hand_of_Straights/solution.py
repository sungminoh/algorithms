#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].

Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.

Constraints:

	1 <= hand.length <= 10000
	0 <= hand[i] <= 10^9
	1 <= W <= hand.length

Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
"""
import sys
from collections import defaultdict
from typing import Dict
from typing import List
import pytest


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if W == 1:
            return True
        if len(hand) % W != 0:
            return False
        hand.sort()
        d = defaultdict(list)
        for n in hand:
            if n-1 not in d:
                d[n].append(1)
            else:
                c = d[n-1].pop(0) + 1
                if len(d[n-1]) == 0:
                    d.pop(n-1)
                if c < W:
                    d[n].append(c)
        return not d


@pytest.mark.parametrize('hand, W, expected', [
    ([1,2,3,6,2,3,4,7,8], 3, True),
    ([1,2,3,4,5], 4, False),
    ([1,2,3], 1, True),
])
def test(hand, W, expected):
    assert expected == Solution().isNStraightHand(hand, W)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
