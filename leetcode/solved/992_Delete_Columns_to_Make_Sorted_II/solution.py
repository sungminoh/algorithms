
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef","vyz"].

Suppose we chose a set of deletion indices D such that after deletions, the final array has its elements in lexicographic order (A[0] ).

Return the minimum possible value of D.length.

Example 1:

Input: ["ca","bb","ac"]
Output: 1
Explanation:
After deleting the first column, A = ["a", "b", "c"].
Now A is in lexicographic order (ie. A[0] <= A[1] <= A[2]).
We require at least 1 deletion since initially A was not in lexicographic order, so the answer is 1.

Example 2:

Input: ["xc","yb","za"]
Output: 0
Explanation:
A is already in lexicographic order, so we don't need to delete anything.
Note that the rows of A are not necessarily in lexicographic order:
ie. it is NOT necessarily true that (A[0][0] <= A[0][1] <= ...)

Example 3:

Input: ["zyx","wvu","tsr"]
Output: 3
Explanation:
We have to delete every column.

Note:
    1. 1 <= A.length <= 100
    2. 1 <= A[i].length <= 100
"""
import sys
from typing import List
import pytest


def is_lexico_order(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst) - 1))


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        cnt = 0
        okay = set()
        for k in range(len(A[0])):
            temp_okay = set()
            for i in range(1, len(A)):
                if i in okay:
                    continue
                l1, l2 = A[i - 1], A[i]
                c1, c2 = l1[k], l2[k]
                if c1 < c2:
                    temp_okay.add(i)
                elif c1 > c2:
                    cnt += 1
                    break
            else:
                okay.update(temp_okay)
        return cnt


@pytest.mark.parametrize('A, expected', [
    (["ca","bb","ac"], 1),
    (["xc","yb","za"], 0),
    (["zyx","wvu","tsr"], 3),
    (["xga","xfb","yfa"], 1),
    (["doeeqiy","yabhbqe","twckqte"], 3)
])
def test(A, expected):
    assert expected == Solution().minDeletionSize(A)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
