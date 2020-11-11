#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5

Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3

Example 3:

Input: stones = [[0,0]]
Output: 0

Note:
    1. 1 <= stones.length <= 1000
    2. 0 <= stones[i][j] < 10000
"""
from typing import List
import sys
from collections import defaultdict
import pytest


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        xs = defaultdict(set)
        ys = defaultdict(set)
        for i, (x, y) in enumerate(stones):
            xs[x].add(y)
            ys[y].add(x)

        cnt = 0
        while xs:
            cnt += 1
            x, y = xs.popitem()
            xstack = set([x])
            ystack = set(y)
            while xstack or ystack:
                while xstack:
                    x = xstack.pop()
                    if x not in xs:
                        continue
                    ystack.update(xs.get(x, set()))
                    xs.pop(x)
                while ystack:
                    y = ystack.pop()
                    if y not in ys:
                        continue
                    xstack.update(ys.get(y, set()))
                    ys.pop(y)
        return len(stones) - cnt

    def _removeStones(self, stones: List[List[int]]) -> int:
        stones = {tuple(p) for p in stones}
        def find_min():
            p = None
            m = float('inf')
            for i, (x, y) in enumerate(stones):
                overlaps = len(xp[x].union(yp[y])) - 1
                if 0 < overlaps < m:
                    m = overlaps
                    p = (x, y)
            return p

        def remove_stone(p):
            xp[p[0]].remove(p)
            yp[p[1]].remove(p)
            stones.remove(p)

        xp = defaultdict(set)
        yp = defaultdict(set)

        for i, p in enumerate(stones):
            xp[p[0]].add(p)
            yp[p[1]].add(p)

        cnt = 0
        while True:
            p = find_min()
            print(p)
            if p is None:
                return cnt
            remove_stone(p)
            print('------------------------------------')
            print_stones(list(stones))
            cnt += 1
        return cnt


def print_stones(stones):
    def print_line(line):
        l = [' '] * (line[-1] + 1)
        for x in line:
            l[x] = '*'
        print(''.join(l))

    stones = sorted(stones, key=lambda p: (p[1], p[0]))
    prev_y = None
    line = []
    for x, y in stones:
        if prev_y != y:
            # if prev_y is not None:
                # print('\n' * (y - prev_y - 1), end='')
            if line:
                print_line(line)
            prev_y = y
            line = [x]
        else:
            line.append(x)
    print_line(line)


@pytest.mark.parametrize('stones, expected', [
    ([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]], 5),
    ([[0,0],[0,2],[1,1],[2,0],[2,2]], 3),
    ([[0,0]], 0),
    ([[5,9],[9,0],[0,0],[7,0],[4,3],[8,5],[5,8],[1,1],[0,6],[7,5],[1,6],[1,9],[9,4],[2,8],[1,3],[4,2],[2,5],[4,1],[0,2],[6,5]], 19),
])
def test(stones, expected):
    print()
    print_stones(stones)
    assert expected == Solution().removeStones(stones)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
