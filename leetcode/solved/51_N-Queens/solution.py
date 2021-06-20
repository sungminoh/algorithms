#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:

Input: n = 1
Output: [["Q"]]

Constraints:

	1 <= n <= 9
"""
import sys
from typing import List
import pytest


class Solution:
    def solveNQueens(self, n):
        """
        12/26/2017 20:49
        """
        def dfs(q, d, s):
            i = len(q)
            if i == n:
                ret.append(q[:])
                return None;
            for j in range(n):
                if j in q or i-j in d or i+j in s:
                    continue
                d.add(i-j)
                s.add(i+j)
                q.append(j)
                dfs(q, d, s)
                d.remove(i-j)
                s.remove(i+j)
                q.pop()
        ret = []
        dfs([], set(), set())
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in sol] for sol in ret]

    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        col = set()
        fdig = set()
        bdig = set()
        ret = []

        def dfs(i, backtrack):
            if i == n:
                ret.append(backtrack[:])
            for j in range(n):
                if j not in col and i+j not in bdig and i-j not in fdig:
                    col.add(j)
                    bdig.add(i+j)
                    fdig.add(i-j)
                    backtrack.append('.'*j + 'Q' + '.'*(n-j-1))
                    dfs(i+1, backtrack)
                    col.remove(j)
                    bdig.remove(i+j)
                    fdig.remove(i-j)
                    backtrack.pop()

        dfs(0, [])
        return ret


@pytest.mark.parametrize('n, expected', [
(4, [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]),
(1, [["Q"]]),
])
def test(n, expected):
    assert expected == Solution().solveNQueens(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
