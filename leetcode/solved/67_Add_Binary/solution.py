#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
67. Add Binary(https://leetcode.com/problems/add-binary/description/)
DescriptionHintsSubmissionsDiscussSolution
DiscussPick One
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return '{0:b}'.format(int(a, 2)+int(b, 2))


def main():
    print(Solution().addBinary(input(), input()))


if __name__ == '__main__':
    main()
