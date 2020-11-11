#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        return len(self.solveNQueens(n))

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
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


def main():
    n = int(input())
    print(Solution().totalNQueens(n))


if __name__ == '__main__':
    main()
