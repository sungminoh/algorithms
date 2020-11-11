#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
174. Dungeon Game
DescriptionHintsSubmissionsDiscussSolution
Pick One
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.



Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)


Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
"""


class Solution:
    def calculateMinimumHP(self, dungeon):
        healths = [float('inf')] * len(dungeon[0])
        healths[-1] = 1
        for row in reversed(dungeon):
            for i in reversed(range(len(dungeon[0]))):
                healths[i] = max(1, min(healths[i:i+2]) - row[i])
        return healths[0]

    def _calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        self.dungeon = dungeon
        self.memo = [[None] * len(dungeon[0]) for _ in dungeon]
        self.memo[-1][-1] = 1 - dungeon[-1][-1] if dungeon[-1][-1] < 0 else 1
        return self.foo(0, 0)

    def foo(self, i, j):
        if self.memo[i][j] is not None:
            return self.memo[i][j]
        sub = []
        if i < len(self.dungeon) - 1:
            sub.append(self.foo(i + 1, j))
        if j < len(self.dungeon[0]) - 1:
            sub.append(self.foo(i, j + 1))
        here = min(sub) - self.dungeon[i][j]
        ret = here if here > 0 else 1
        self.memo[i][j] = ret
        return ret


def main():
    dungeon = []
    row = input()
    while row:
        dungeon.append([int(x) for x in row.split()])
        row = input()
    print(Solution().calculateMinimumHP(dungeon))


if __name__ == '__main__':
    main()
