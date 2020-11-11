#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False
"""
import pytest

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        visited = set()
        init_state = (0, 0)
        queue = [init_state]
        visited.add(init_state)

        def visit(state, visited, queue):
            if state not in visited:
                visited.add(state)
                queue.append(state)

        while queue:
            jug1, jug2 = queue.pop()
            if jug1 != x:
                visit((x, jug2), visited, queue)
            if jug2 != y:
                visit((jug1, y), visited, queue)
            if x - jug1 > jug2:
                visit((jug1 + jug2, 0), visited, queue)
            else:
                visit((0, jug2 - (x - jug1)), visited, queue)
            if jug1 < y - jug2:
                visit((0, jug1 + jug2), visited, queue)
            else:
                visit((jug1 - (y - jug2), 0), visited, queue)

        for jug1, jug2 in visited:
            if jug1 + jug2 == z:
                return True

        return False


@pytest.mark.parametrize('x, y, z, expected', [
    (3, 5, 4, True),
    (2, 6, 5, False),
    (104579, 104593, 12444, True)
])
def test(x, y, z, expected):
    assert expected == Solution().canMeasureWater(x, y, z)
