#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
66. Plus One
DescriptionHintsSubmissionsDiscussSolution
DiscussPick One
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        digits[-1] += 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += carry
            carry = 0
            if digits[i] >= 10:
                carry = digits[i]//10
                digits[i] = digits[i] % 10
        if carry:
            digits.insert(0, carry)
        return digits


def main():
    print(Solution().plusOne(list(map(int, list(input())))))



if __name__ == '__main__':
    main()
