#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state. 

Example 1:

Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."

Example 2:

Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.

Note:

	0 <= N <= 10^5
	String dominoes contains only 'L', 'R' and '.'
"""
import sys
import pytest


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        d = list(dominoes)
        i = 0
        while i < len(d):
            if d[i] == 'R':
                j = i
                while j < len(d) and d[j] != 'L':
                    if d[j] == 'R':
                        d[i:j] = ['R'] * (j-i)
                        i = j
                    j += 1
                if j < len(d):
                    # 0 1 2 3 4
                    # 5 6 7 8 9
                    d[i:i + (j-i+1)//2] = ['R'] * ((j-i+1)//2)
                    d[j+1 - (j-i+1)//2:j+1] = ['L'] * ((j-i+1)//2)
                else:
                    while i in range(len(d)):
                        d[i] = 'R'
                        i +=1
                i = j
            elif d[i] == 'L':
                j = i-1
                while j >= 0 and d[j] == '.':
                    j -= 1
                d[j+1:i] = 'L' * (i-j-1)
            i += 1
        return ''.join(d)


@pytest.mark.parametrize('dominoes, expected', [
    (".L.R...LR..L..", "LL.RR.LLRRLL.."),
    ("RR.L", "RR.L"),
    (".L.R.", "LL.RR")
])
def test(dominoes, expected):
    assert expected == Solution().pushDominoes(dominoes)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
