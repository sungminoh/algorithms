#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '' if numerator * denominator >= 0 else '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        dr = divmod(numerator, denominator)
        if not dr[1]:
            return '%s%s' % (sign, dr[0])
        num = dr[0]
        fractions = []
        position = dict()
        while dr[1]:
            dr = divmod(10*dr[1], denominator)
            if dr in position:
                fractions.insert(position[dr], '(')
                fractions.append(')')
                break
            else:
                fractions.append(dr[0])
                position[dr] = len(fractions)-1
        return '%s%s.%s' % (sign, num, ''.join(str(x) for x in fractions))


def main():
    n, d = [int(x) for x in input().split()]
    print('%r' % Solution().fractionToDecimal(n, d))


if __name__ == '__main__':
    main()
