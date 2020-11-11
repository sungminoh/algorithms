#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from math import sqrt
from heapq import heapify, heappop, heappush


def solve(heap, m, M, N, q):
    v, (d, u) = heappop(heap)
    cnt = d
    if q < v:
        return 0
    while heap:
        nv, (nd, nu) = heap[0]
        if v <= q <= nv:
            if cnt == 0:
                return v
            else:
                return q
        if cnt == 1 and d == 1:
            for i in range(N):
                if i not in u:
                    heappush(heap, (v + m[i], (1, u | {i})))
        elif cnt == 0:
            for i in range(N):
                if i not in u:
                    heappush(heap, (v + M[i], (-1, u | {i})))
        v, (d, u) = heappop(heap)
        cnt += d
    return v


def main():
    T = int(input())
    for t in range(1, T + 1):
        N, P = [int(x) for x in input().split()]
        base = 0
        M = []
        m = []
        heap = []
        for _ in range(N):
            w, h = [int(x) for x in input().split()]
            base += 2 * (w + h)
            m.append(2 * min(w, h))
            M.append(2 * sqrt(pow(w, 2) + pow(h, 2)))
        for i in range(N):
            heappush(heap, (m[i], (1, set([i]))))
            heappush(heap, (M[i], (-1, set([i]))))
        print('Case #%s: %s' % (t, base + solve(heap, m, M, N, P - base)))


if __name__ == '__main__':
    main()
