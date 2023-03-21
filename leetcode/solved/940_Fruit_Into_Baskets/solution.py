#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

	You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
	Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
	Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].

Constraints:

	1 <= fruits.length <= 105
	0 <= fruits[i] < fruits.length
"""
from collections import Counter
from typing import List
import pytest
import sys


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = Counter()
        i = j = 0
        ret = 0
        while i < len(fruits):
            cnt[fruits[i]] += 1
            while len(cnt) > 2:
                cnt[fruits[j]] -= 1
                if cnt[fruits[j]] == 0:
                    cnt.pop(fruits[j])
                j += 1
            ret = max(ret, i-j+1)
            i += 1
        return ret


@pytest.mark.parametrize('args', [
    (([1,2,1], 3)),
    (([0,1,2,2], 3)),
    (([1,2,3,2,2], 4)),
    (([3,3,3,1,2,1,1,2,3,3,4], 5)),
])
def test(args):
    assert args[-1] == Solution().totalFruit(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
