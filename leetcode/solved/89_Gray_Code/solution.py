#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
"""


class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        """
        0110011001100110
        0011110000111100
        0000111111110000
        0000000011111111
        j'th status of i'th position:
            0, where j <= 2**i or ((j - 2**i) / (2**(i+1))) % 2 == 1
            1, where ((j - 2**i) / (2**(i+1))) % 2 == 0
        """
        return [sum((2**i) * (((j+(2**i)) // (2**(i+1))) % 2) for i in range(n)) for j in range(2**n)]


def main():
    print(Solution().grayCode(int(input())))


if __name__ == '__main__':
    main()
