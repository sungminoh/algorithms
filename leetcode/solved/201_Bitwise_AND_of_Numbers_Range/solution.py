#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
"""


class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def find_last_diff_idx(m, n):
            idx = -1
            for i in range(32):
                if m % 2 != n % 2:
                    idx = i
                m //= 2
                n //= 2
            return idx

        last_diff_idx = find_last_diff_idx(m, n)
        m -= m % pow(2, last_diff_idx + 1)
        return m


def main():
    inputs = []
    inputs.append(([5,7], 4))
    inputs.append(([0,1], 0))
    for (m, n), expected in inputs:
        actual = Solution().rangeBitwiseAnd(m, n)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')


if __name__ == '__main__':
    main()
