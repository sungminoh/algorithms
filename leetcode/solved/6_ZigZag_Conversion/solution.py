#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
n=numRows
Δ=2n-2    1                           2n-1                         4n-3
Δ=        2                     2n-2  2n                    4n-4   4n-2
Δ=        3               2n-3        2n+1              4n-5       .
Δ=        .           .               .               .            .
Δ=        .       n+2                 .           3n               .
Δ=        n-1 n+1                     3n-3    3n-1                 5n-5
Δ=2n-2    n                           3n-2                         5n-4
"""


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        stride = 2*numRows - 2
        ret = list(s[::stride])
        for i in range(1, numRows-1):
            j = i
            while j < len(s):
                ret.append(s[j])
                diag_position = j + stride - (2*i)
                if diag_position < len(s):
                    ret.append(s[diag_position])
                j += stride
        ret.extend(s[numRows-1::stride])
        return ''.join(ret)


def main():
    print(Solution().convert(input(), int(input())))


if __name__ == '__main__':
    main()
