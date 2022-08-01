#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:

	1 <= numRows <= 30
"""
import sys
from typing import List
import pytest


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """07/17/2021 08:17"""
        ret = []
        for i in range(numRows):
            row = [1]
            if ret:
                for i in range(len(ret[-1])-1):
                    row.append(ret[-1][i] + ret[-1][i+1])
                row.append(1)
            ret.append(row)
        return ret

    def generate(self, numRows: int) -> List[List[int]]:
        """07/31/2022 22:48"""
        if numRows == 0:
            return []
        ret = [[1]]
        for i in range(1, numRows):
            row = [1]
            for i in range(len(ret[-1])-1):
                row.append(ret[-1][i] + ret[-1][i+1])
            row.append(1)
            ret.append(row)
        return ret


@pytest.mark.parametrize('numRows, expected', [
    (5, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),
    (1, [[1]]),
])
def test(numRows, expected):
    assert expected == Solution().generate(numRows)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
