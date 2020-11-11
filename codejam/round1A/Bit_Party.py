#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""


def main():
    T = int(input())
    for i in range(1, T+1):
        R, B, C = [int(x) for x in input().split()]
        M = []
        S = []
        P = []
        for _ in range(C):
            m, s, p = [int(x) for x in input().split()]
            M.append(m)
            S.append(s)
            P.append(p)
        print('Case #%s: %s' %(i, solve()))


if __name__ == '__main__':
    main()
