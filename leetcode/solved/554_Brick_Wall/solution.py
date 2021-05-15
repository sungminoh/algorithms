#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

Example 1:

Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
Output: 2

Example 2:

Input: wall = [[1],[1],[1]]
Output: 3

Constraints:

	n == wall.length
	1 <= n <= 104
	1 <= wall[i].length <= 104
	1 <= sum(wall[i].length) <= 2 * 104
	sum(wall[i]) is the same for each row i.
	1 <= wall[i][j] <= 231 - 1
"""
import sys
from collections import defaultdict
from collections import Counter
from itertools import accumulate
from typing import List
import pytest


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        """06/07/2020 22:47"""
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

    def leastBricks(self, wall: List[List[int]]) -> int:
        """
        Find the number of same split position across rows and
        return the number of rows - max number of splits across rows
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        if not wall:
            return 0
        cnt = defaultdict(int)
        for row in wall:
            for split in accumulate(row):
                cnt[split] += 1
        cnt[sum(wall[0])] = 0
        return len(wall) - max(cnt.values())


@pytest.mark.parametrize('wall, expected', [
    ([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]], 2),
    ([[1],[1],[1]], 3),
])
def test(wall, expected):
    assert expected == Solution().leastBricks(wall)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
