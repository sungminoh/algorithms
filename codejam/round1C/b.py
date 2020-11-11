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
    for t in range(1, T+1):
        N = int(input())
        appears = [0] * N
        used = [False] * N
        for _ in range(N):
            D, *flavors = [int(x) for x in input().split()]
            if D == 0:
                continue
            for f in flavors:
                appears[f] += 1
            success = False
            for f in sorted(flavors, key=lambda x: appears[x]):
                if not used[f]:
                    print(f)
                    used[f] = True
                    success = True
                    break
            if not success:
                print(-1)


if __name__ == '__main__':
    main()
