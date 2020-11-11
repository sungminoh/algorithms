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
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        digits = list(range(1, n+1))
        ret = []
        k -= 1
        while digits:
            m = 1
            for i in range(1, len(digits)):
                m *= i
            p = k // m
            ret.append(digits[p])
            del digits[p]
            k -= m*p
        return ''.join(map(str, ret))


def main():
    n, k = map(int, input().split())
    print(Solution().getPermutation(n, k))
    pass


if __name__ == '__main__':
    main()
