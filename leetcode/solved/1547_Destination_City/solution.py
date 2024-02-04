from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".

Example 3:

Input: paths = [["A","Z"]]
Output: "Z"

Constraints:

	1 <= paths.length <= 100
	paths[i].length == 2
	1 <= cityAi.length, cityBi.length <= 10
	cityAi != cityBi
	All strings consist of lowercase and uppercase English letters and the space character.
"""
import pytest
import sys


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        """Feb 03, 2024 18:42"""
        return (set(p[1] for p in paths) - set(p[0] for p in paths)).pop()


@pytest.mark.parametrize('args', [
    (([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]], "Sao Paulo")),
    (([["B","C"],["D","B"],["C","A"]], "A")),
    (([["A","Z"]], "Z")),
])
def test(args):
    assert args[-1] == Solution().destCity(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
