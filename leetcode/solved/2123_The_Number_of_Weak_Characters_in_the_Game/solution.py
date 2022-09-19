#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

Return the number of weak characters.

Example 1:

Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.

Example 2:

Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.

Example 3:

Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.

Constraints:

	2 <= properties.length <= 105
	properties[i].length == 2
	1 <= attacki, defensei <= 105
"""
from typing import List
import pytest
import sys


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        """09/18/2022 23:21"""
        if not properties:
            return 0
        properties.sort(key=lambda x: (-x[0], -x[1]))
        cur = None
        bar = -float('inf')
        i = 0
        ret = 0
        while i < len(properties):
            c, m = properties[i]
            while i < len(properties) and properties[i][0] == c:
                if properties[i][1] < bar:
                    ret += 1
                m = max(m, properties[i][1])
                i += 1
            bar = max(bar, m)
        return ret

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        """09/18/2022 23:25"""
        if not properties:
            return 0
        properties.sort(key=lambda x: (-x[0], x[1]))
        bar = -float('inf')
        ret = 0
        for _, d in properties:
            if d < bar:
                ret += 1
            bar = max(bar, d)
        return ret


@pytest.mark.parametrize('properties, expected', [
    ([[5,5],[6,3],[3,6]], 0),
    ([[2,2],[3,3]], 1),
    ([[1,5],[10,4],[4,3]], 1),
])
def test(properties, expected):
    assert expected == Solution().numberOfWeakCharacters(properties)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
