#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are two types of soup: type A and type B. Initially we have N ml of each type of soup. There are four kinds of operations:

	Serve 100 ml of soup A and 0 ml of soup B
	Serve 75 ml of soup A and 25 ml of soup B
	Serve 50 ml of soup A and 50 ml of soup B
	Serve 25 ml of soup A and 75 ml of soup B

When we serve some soup, we give it to someone and we no longer have it.  Each turn, we will choose from the four operations with equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as we can.  We stop once we no longer have some quantity of both types of soup.

Note that we do not have the operation where all 100 ml's of soup B are used first.  

Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time.

Example:
Input: N = 50
Output: 0.625
Explanation:
If we choose the first two operations, A will become empty first. For the third operation, A and B will become empty at the same time. For the fourth operation, B will become empty first. So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.

Notes:

	0 <= N <= 10^9. 
	Answers within 10^-6 of the true value will be accepted as correct.
"""
from collections import defaultdict
import sys
from functools import lru_cache
import pytest


class Solution:
    def _soupServings(self, N: int) -> float:
        if N > 12500:
            return 1, 0

        @lru_cache(None)
        def prob(a, b):
            if b > 3*a:
                return (1, 0)
            if a <= 0:
                return (0, 1) if b <= 0 else (1, 0)
            if b <= 0:
                return 0, 0
            a_first = 0
            ab_together = 0
            for use_a, use_b in zip([100, 75, 50, 25], [0, 25, 50, 75]):
                if a <= use_a:
                    if b > use_b:
                        a_first += 0.25
                    else:
                        ab_together += 0.25
                else:
                    _a_first, _ab_together = prob(a-use_a, b-use_b)
                    a_first += _a_first * 0.25
                    ab_together += _ab_together * 0.25
            return a_first, ab_together

        a, b = prob(N, N)
        return a + (b/2)



@pytest.mark.parametrize('N, expected', [
    (50, 0.625),
    (0, 0.5),
    (101, 0.7421875),
    (660295675, 0),
])
def test(N, expected):
    assert expected == Solution().soupServings(N)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
