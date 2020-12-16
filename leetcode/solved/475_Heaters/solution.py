#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius range. 

Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

Notice that all the heaters follow your radius standard, and the warm radius will the same.

Example 1:

Input: houses = [1,2,3], heaters = [2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

Example 2:

Input: houses = [1,2,3,4], heaters = [1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.

Example 3:

Input: houses = [1,5], heaters = [2]
Output: 3

Constraints:

	1 <= houses.length, heaters.length <= 3 * 104
	1 <= houses[i], heaters[i] <= 109
"""
import sys
from pip._internal.req.req_file import handle_option_line
from typing import List
import pytest


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        i, j = 0, 0
        r = -float('inf')
        while i < len(houses):
            while j < len(heaters) and heaters[j] < houses[i]:
                j += 1
            r = max(r,
                    min(abs(houses[i] - heaters[j%len(heaters)]),
                        abs(houses[i] - heaters[j-1])))
            i += 1
        return r



@pytest.mark.parametrize('houses, heaters, expected', [
    ([1,2,3], [2], 1),
    ([1,2,3,4], [1,4], 1),
    ([1,5], [2], 3),
])
def test(houses, heaters, expected):
    assert expected == Solution().findRadius(houses, heaters)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
