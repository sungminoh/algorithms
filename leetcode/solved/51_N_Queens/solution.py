#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

class Solution:
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
    for sol in Solution().solveNQueens(n):
        for line in sol:
            print(line)
        print()


if __name__ == '__main__':
    main()
