#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

	numberOfBoxesi is the number of boxes of type i.
	numberOfUnitsPerBoxi is the number of units in each box of the type i.

You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

Example 1:

Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

Example 2:

Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91

Constraints:

	1 <= boxTypes.length <= 1000
	1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
	1 <= truckSize <= 106
"""
import sys
from typing import List
import pytest


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """06/25/2021 20:52"""
        cnt = 0
        ret = 0
        for c, u in sorted(boxTypes, key=lambda x: x[1], reverse=True):
            n = min(truckSize-cnt, c)
            cnt += n
            ret += n*u
            if cnt >= truckSize:
                break
        return ret

    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """07/21/2022 21:50"""
        ret = 0
        for box_cnt, unit_cnt in sorted(boxTypes, key=lambda x: x[1], reverse=True):
            if truckSize == 0:
                break
            cnt = min(box_cnt, truckSize)
            ret += cnt * unit_cnt
            truckSize -= cnt
        return ret


@pytest.mark.parametrize('boxTypes, truckSize, expected', [
    ([[1,3],[2,2],[3,1]], 4, 8),
    ([[5,10],[2,5],[4,7],[3,9]], 10, 91),
])
def test(boxTypes, truckSize, expected):
    assert expected == Solution().maximumUnits(boxTypes, truckSize)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
