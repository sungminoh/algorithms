from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)

Constraints:

	1 <= people.length <= 5 * 104
	1 <= people[i] <= limit <= 3 * 104
"""
import pytest
import sys


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """Apr 05, 2022 21:51"""
        people.sort(reverse=True)
        l, r = 0, len(people)-1
        ret = 0
        while l <= r:
            if l != r and people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                l += 1
            ret += 1
        return ret

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """Aug 26, 2023 12:32"""
        people.sort()
        i = 0
        j = len(people)-1
        ret = 0
        while i < j:
            if people[j] > limit:
                return -1
            elif people[i] + people[j] <= limit:
                i += 1
            j -=1
            ret += 1
        if i == j:
            ret += 1
        return ret


@pytest.mark.parametrize('args', [
    (([1,2], 3, 1)),
    (([3,2,2,1], 3, 3)),
    (([3,5,3,4], 5, 4)),
])
def test(args):
    assert args[-1] == Solution().numRescueBoats(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
