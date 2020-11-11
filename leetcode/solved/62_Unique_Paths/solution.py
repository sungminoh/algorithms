#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        l = [1]*m
        for _ in range(n-1):
            for i in range(1, m):
                l[i] += l[i-1]
        return l[-1]


def main():
    m, n = map(int, input().split())
    print(Solution().uniquePaths(m, n))


if __name__ == '__main__':
    main()
