#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
"""

class Solution:
    def is_valley(self, i, ratings):
        left = ratings[i-1] if i > 0 else float('inf')
        right = ratings[i+1] if i < len(ratings)-1 else float('inf')
        return left >= ratings[i] <= right

    def fill_left(self, i, ratings, candies):
        if i == 0 or ratings[i-1] <= ratings[i]:
            return
        if not candies[i-1] or candies[i-1] < candies[i] + 1:
            candies[i-1] = candies[i] + 1
        self.fill_left(i-1, ratings, candies)

    def fill_right(self, i, ratings, candies):
        if i == len(ratings)-1 or ratings[i+1] <= ratings[i]:
            return
        if not candies[i+1] or candies[i+1] < candies[i] + 1:
            candies[i+1] = candies[i] + 1
        self.fill_right(i+1, ratings, candies)

    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
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
            if self.is_valley(i, ratings):
                candies[i] = 1
                queue.append(i)
        for i in queue:
            if i > 0:
                self.fill_left(i, ratings, candies)
            if i < len(ratings)-1:
                self.fill_right(i, ratings, candies)
        return sum(candies)


def main():
    # ratings = [int(x) for x in input().split()]
    examples = [
        ([1,0,2], 5),
        ([1,2,2], 4),
        ([1,3,2,2,1], 7), # -> 1 2 1 2 1 -> 7
        ([1,2,87,87,87,2,1], 13)  # -> 1 2 3 1 3 2 1: 13
    ]
    for e, a in examples:
        print('Input: ', e)
        s = Solution().candy(e)
        print(s, '==' if s == a else '!=', a)


if __name__ == '__main__':
    main()
