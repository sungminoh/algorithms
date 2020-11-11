
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Example:

Input: [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

Output: 2

Explanation:

Note:
	1. The width sum of bricks in different rows are the same and won't exceed INT_MAX.
	2. The number of bricks in each row is in range [1,10,000]. The height of wall is in range [1,10,000]. Total number of bricks of the wall won't exceed 20,000.
"""
import sys
from collections import Counter
from collections import defaultdict
from itertools import accumulate
from typing import List
import pytest


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        if not wall or not wall[0]:
            return 0
        counter = Counter()
        for row in wall:
            for col in accumulate(row[:-1]):
                if col not in counter:
                    counter[col] = 0
                counter[col] += 1
        if not counter:
            return len(wall)
        _, cnt = counter.most_common(1)[0]
        return len(wall) - cnt


@pytest.mark.parametrize('wall, expected', [
    ([[1,2,2,1],
      [3,1,2],
      [1,3,2],
      [2,4],
      [3,1,2],
      [1,3,1,1]], 2),
    ([[1], [1], [1]], 3)
])
def test(wall, expected):
    assert expected == Solution().leastBricks(wall)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
