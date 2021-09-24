#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given several boxes with different colors represented by different positive numbers.

You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.

Return the maximum points you can get.

Example 1:

Input: boxes = [1,3,2,2,2,3,4,3,1]
Output: 23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1]
----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
----> [1, 3, 3, 3, 1] (1*1=1 points)
----> [1, 1] (3*3=9 points)
----> [] (2*2=4 points)

Example 2:

Input: boxes = [1,1,1]
Output: 9

Example 3:

Input: boxes = [1]
Output: 1

Constraints:

	1 <= boxes.length <= 100
	1 <= boxes[i] <= 100
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        """11/11/2020 18:49	"""
        @lru_cache(None)
        def dfs(i, j, k):
            if i > j:
                return 0
            s = i
            while s <= j and boxes[i] == boxes[s]:
                s += 1
            cnt = s - i
            ret = dfs(s, j, 0) + (k+cnt)**2
            for m in range(s, j+1):
                if boxes[m] == boxes[i]:
                    ret = max(ret, dfs(s, m-1, 0) + dfs(m, j, k+cnt))
            return ret

        return dfs(0, len(boxes)-1, 0)

    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dfs(boxes):
            i = 0
            ret = 0
            while i < len(boxes):
                j = i
                while j < len(boxes) and boxes[i] == boxes[j]:
                    j += 1
                k = j-i
                ret = max(ret, dfs(boxes[:i] + boxes[j:]) + k*k)
                i = j
            return ret

        return dfs(tuple(boxes))

    def removeBoxes(self, boxes: List[int]) -> int:
        """
        There are two ways of removing the first box
        1. Remove it first with its adjacent same boxex
        2. Merge it with later appearance assumeing that boxex between them
            are removed first

        Time complexity: O(n^3)
        Space complexity: O(n^3)
        """
        @lru_cache(None)
        def dfs(i, j, k):
            if i > j:
                return 0
            s = i
            while s <= j and boxes[i] == boxes[s]:
                s += 1
            k += s-i
            ret = k*k + dfs(s, j, 0)  # case 1
            for h in range(s, j+1):
                if boxes[i] == boxes[h]:
                    ret = max(ret, dfs(s, h-1, 0) + dfs(h, j, k))
            return ret

        return dfs(0, len(boxes)-1, 0)


@pytest.mark.parametrize('boxes, expected', [
    ([1,3,2,2,2,3,4,3,1], 23),
    ([1,1,1], 9),
    ([1], 1),
    ([8,1,2,10,8,5,1,10,8,4], 16),
    ([3,8,8,5,5,3,9,2,4,4,6,5,8,4,8,6,9,6,2,8,6,4,1,9,5,3,10,5,3,3,9,8,8,6,5,3,7,4,9,6,3,9,4,3,5,10,7,6,10,7], 136),
    ([1,1,1,2,1,1,1], 37),
    ([1,1,1,2,1,1,1,3,1,1,1], 83),
    ([1,1,1,2,1,3,1,1,1], 51),
    ([1,2,1,3,1,1,1,1], 38),
    ([1,1,1,1,1,1,1,1,1,1,2,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 9606),
])
def test(boxes, expected):
    assert expected == Solution().removeBoxes(boxes)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
