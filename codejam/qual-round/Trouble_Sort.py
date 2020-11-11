#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""


def solve(v):
    odd_even = [sorted(v[::2]), sorted(v[1::2])]
    p = -1
    for i in range(len(v)):
        x = odd_even[i%2][i//2]
        if x < p:
            return i-1
        p = x
    return 'OK'


def main():
    t = int(input())
    for i in range(1, t + 1):
        input()
        v = [int(x) for x in input().split()]
        print('Case #%s: %s' % (i, solve(v)))


if __name__ == '__main__':
    main()
