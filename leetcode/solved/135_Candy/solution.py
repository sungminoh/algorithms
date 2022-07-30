#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

	Each child must have at least one candy.
	Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

Constraints:

	n == ratings.length
	1 <= n <= 2 * 104
	0 <= ratings[i] <= 2 * 104
"""
from heapq import heappop
from heapq import heapify
from collections import deque
import sys
from typing import List
import pytest


class Solution:
    def candy(self, ratings):
        """10/23/2018 04:52
        Fill from each valley
        Time complexity: O(n)
        Space complexity: O(n)
        """
        def is_valley(i, ratings):
            left = ratings[i-1] if i > 0 else float('inf')
            right = ratings[i+1] if i < len(ratings)-1 else float('inf')
            return left >= ratings[i] <= right

        def fill_left(i, ratings, candies):
            if i == 0 or ratings[i-1] <= ratings[i]:
                return
            if not candies[i-1] or candies[i-1] < candies[i] + 1:
                candies[i-1] = candies[i] + 1
            fill_left(i-1, ratings, candies)

        def fill_right(i, ratings, candies):
            if i == len(ratings)-1 or ratings[i+1] <= ratings[i]:
                return
            if not candies[i+1] or candies[i+1] < candies[i] + 1:
                candies[i+1] = candies[i] + 1
            fill_right(i+1, ratings, candies)

        if len(ratings) == 1:
            return 1
        elif len(ratings) == 2:
            if ratings[0] == ratings[1]:
                return 2
            else:
                return 3
        candies = [0] * len(ratings)
        queue = []
        for i in range(len(ratings)):
            if is_valley(i, ratings):
                candies[i] = 1
                queue.append(i)
        for i in queue:
            if i > 0:
                fill_left(i, ratings, candies)
            if i < len(ratings)-1:
                fill_right(i, ratings, candies)
        return sum(candies)

    def candy(self, ratings: List[int]) -> int:
        """
        Heap
        Time complexity: O(n*logn)
        Space complexity: O(n)
        """
        h = [(r, i) for i, r in enumerate(ratings)]
        candies = [0]*len(ratings)
        heapify(h)
        while h:
            r, i = heappop(h)
            m = 0
            if i > 0 and r > ratings[i-1]:
                m = max(m, candies[i-1])
            if i < len(candies)-1 and r > ratings[i+1]:
                m = max(m, candies[i+1])
            candies[i] = m + 1
        return sum(candies)

    def candy(self, ratings: List[int]) -> int:
        """
        Left and right
        Time complexity: O(n)
        Space complexity: O(n)
        """
        candies = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        return sum(candies)

    def candy(self, ratings: List[int]) -> int:
        """07/26/2022 14:28"""
        if not ratings:
            return 0
        left = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                left[i] = left[i-1]+1
        right = [1]*len(ratings)
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1]+1
        return sum(max(l, r) for l, r in zip(left, right))


@pytest.mark.parametrize('ratings, expected', [
    ([1,0,2], 5),
    ([1,2,2], 4),
    ([1,3,4,5,2], 11),
    ([1,3,2,2,1], 7),
    ([29,51,87,87,72,12], 12),
    ([1,6,10,8,7,3,2], 18),
])
def test(ratings, expected):
    assert expected == Solution().candy(ratings)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
