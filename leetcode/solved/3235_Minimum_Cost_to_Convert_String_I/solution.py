#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].

You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

Example 1:

Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
Output: 28
Explanation: To convert the string "abcd" to string "acbe":
- Change value at index 1 from 'b' to 'c' at a cost of 5.
- Change value at index 2 from 'c' to 'e' at a cost of 1.
- Change value at index 2 from 'e' to 'b' at a cost of 2.
- Change value at index 3 from 'd' to 'e' at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28.
It can be shown that this is the minimum possible cost.

Example 2:

Input: source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]
Output: 12
Explanation: To change the character 'a' to 'b' change the character 'a' to 'c' at a cost of 1, followed by changing the character 'c' to 'b' at a cost of 2, for a total cost of 1 + 2 = 3. To change all occurrences of 'a' to 'b', a total cost of 3 * 4 = 12 is incurred.

Example 3:

Input: source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]
Output: -1
Explanation: It is impossible to convert source to target because the value at index 3 cannot be changed from 'd' to 'e'.

Constraints:

	1 <= source.length == target.length <= 105
	source, target consist of lowercase English letters.
	1 <= cost.length == original.length == changed.length <= 2000
	original[i], changed[i] are lowercase English letters.
	1 <= cost[i] <= 106
	original[i] != changed[i]
"""
from typing import List
import pytest
import sys


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        """Jul 28, 2024 23:48"""
        chars = set()
        costs = {}
        for a, b, c in zip(original, changed, cost):
            chars.add(a)
            chars.add(b)
            costs[(a, b)] = min(costs.setdefault((a, b), float('inf')), c)

        for k in chars:
            for a in chars:
                costs[(a, a)] = 0
                for b in chars:
                    costs[(a, b)] = min(
                        costs.get((a, b), float('inf')),
                        costs.get((a, k), float('inf')) + costs.get((k, b), float('inf')))

        ret = 0
        for a, b in zip(source, target):
            if a != b:
                ret += costs.get((a, b), float('inf'))
        return ret if ret < float('inf') else -1


@pytest.mark.parametrize('args', [
    (("abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20], 28)),
    (("aaaa", "bbbb", ["a","c"], ["c","b"], [1,2], 12)),
    (("abcd", "abce", ["a"], ["e"], [10000], -1)),
    (("aabbddccbc", "abbbaabaca", ["a","b","c","b","a","d"], ["d","c","b","d","b","b"], [3,8,7,6,7,10], -1))
])
def test(args):
    assert args[-1] == Solution().minimumCost(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
