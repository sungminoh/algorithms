
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:

Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. The 2nd student himself is in a friend circle. So return 2.

Example 2:

Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

Note:

N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
"""
import sys
from typing import List
import pytest


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(i):
            if M[i][i] == 0:
                return 0
            M[i][i] = 0
            for j_, v in enumerate(M[i]):
                if j_ == i or v <= 0:
                    continue
                dfs(j_)
            return 1

        cnt = 0
        if not M or not M[0]:
            return cnt
        for i in range(len(M)):
            cnt += dfs(i)
        return cnt


@pytest.mark.parametrize('M, expected', [
    ([[1,1,0],
      [1,1,0],
      [0,0,1]], 2),
    ([[1,1,0],
      [1,1,1],
      [0,1,1]], 1),
    ([[1,0,0,1],
      [0,1,1,0],
      [0,1,1,1],
      [1,0,1,1]], 1)
])
def test(M, expected):
    assert expected == Solution().findCircleNum(M)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
