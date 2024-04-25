#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns.

The graph is given as follows: graph[a] is a list of all nodes b such that ab is an edge of the graph.

The mouse starts at node 1 and goes first, the cat starts at node 2 and goes second, and there is a hole at node 0.

During each player's turn, they must travel along one edge of the graph that meets where they are.  For example, if the Mouse is at node 1, it must travel to any node in graph[1].

Additionally, it is not allowed for the Cat to travel to the Hole (node 0).

Then, the game can end in three ways:

	If ever the Cat occupies the same node as the Mouse, the Cat wins.
	If ever the Mouse reaches the Hole, the Mouse wins.
	If ever a position is repeated (i.e., the players are in the same position as a previous turn, and it is the same player's turn to move), the game is a draw.

Given a graph, and assuming both players play optimally, return

	1 if the mouse wins the game,
	2 if the cat wins the game, or
	0 if the game is a draw.

Example 1:

Input: graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
Output: 0

Example 2:

Input: graph = [[1,3],[0],[3],[0,2]]
Output: 1

Constraints:

	3 <= graph.length <= 50
	1 <= graph[i].length < graph.length
	0 <= graph[i][j] < graph.length
	graph[i][j] != i
	graph[i] is unique.
	The mouse and the cat can always move.
"""
from collections import defaultdict
import collections
from collections import deque
from typing import List
import pytest
import sys


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        """Wrong"""
        visited = set()
        def dp(m, c, t):
            """
            Return 1 when player t wins, -1 when player t loses, o.w. 0
            """
            if m == c:
                return 1 if t == 1 else -1
            if m == 0:
                return 1 if t == 0 else -1
            if (m, c, t) in visited:
                return 0
            visited.add((m, c, t))
            if t == 0:
                return -min(dp(x, c, 1) for x in graph[m])
            else:
                return -min(dp(m, x, 0) for x in graph[c] if x != 0)

        mouse_win = dp(1, 2, 0)
        if mouse_win == -1:
            return 2
        return mouse_win

    def catMouseGame(self, graph: List[List[int]]) -> int:
        """Apr 24, 2024 22:48"""
        CAT, MOUSE, DRAW = 2, 1, 0
        N = len(graph)

        def iter_parents(m, c, t):
            if t == MOUSE:
                for x in graph[c]:
                    if x > 0:
                        yield m, x, CAT
            else:
                for x in graph[m]:
                    yield x, c, MOUSE

        degree = {}
        for m in range(N):
            for c in range(N):
                degree[(m, c, MOUSE)] = len(graph[m])
                degree[(m, c, CAT)] = len(graph[c]) - (1 if 0 in graph[c] else 0)

        result = {}
        for i in range(1, N):
            result[(i, i, CAT)] = result[(i, i, MOUSE)] = CAT
            result[(0, i, CAT)] = result[(0, i, MOUSE)] = MOUSE

        queue = deque(result.keys())

        while queue:
            m, c, t = queue.popleft()
            for _m, _c, _t in iter_parents(m, c, t):
                if result.get((_m, _c, _t), DRAW) == DRAW:
                    if result.get((m, c, t), DRAW) == _t:  # can move to winning case
                        result[(_m, _c, _t)] = _t
                        queue.append((_m, _c, _t))
                    else:
                        degree[(_m, _c, _t)] -= 1
                        if degree[(_m, _c, _t)] == 0:
                            result[(_m, _c, _t)] = 3-_t
                            queue.append((_m, _c, _t))

        return result.get((1, 2, MOUSE), DRAW)


@pytest.mark.parametrize('args', [
    (([[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]], 0)),
    (([[1,3],[0],[3],[0,2]], 1)),
    (([[2,6],[2,4,5,6],[0,1,3,5,6],[2],[1,5,6],[1,2,4],[0,1,2,4]], 2)),
])
def test(args):
    assert args[-1] == Solution().catMouseGame(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
