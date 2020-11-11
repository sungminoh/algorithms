#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""



def solve(m, h, v, rc, cc):
    n = rc[-1]  # same with cc[-1]
    perCell, remain = divmod(n, ((h+1)*(v+1)))
    # trivial case
    if remain:
        return 'IMPOSSIBLE'
    if perCell == 0:
        return 'POSSIBLE'
    # find where to cut
    rd = [0]
    for ri, nrc in enumerate(rc):
        if divmod(nrc, n//(h+1)) == (len(rd), 0):
            rd.append(ri+1)
    cd = [0]
    for ci, ncc in enumerate(cc):
        if divmod(ncc, n//(v+1)) == (len(cd), 0):
            cd.append(ci+1)
    # if it is not divided properly
    if len(rd) != h+2 or len(cd) != v+2:
        return 'IMPOSSIBLE'
    # check number of chips per cell
    for i in range(len(rd)-1):
        for j in range(len(cd)-1):
            s = 0
            for row in m[rd[i]:rd[i+1]]:
                s += sum(row[cd[j]:cd[j+1]])
            if s != perCell:
                return 'IMPOSSIBLE'
    return 'POSSIBLE'




def main():
    t = int(input())
    for t in range(1, t + 1):
        r, c, h, v = [int(x) for x in input().split()]
        rchips = [0] * r
        cchips_ = [0] * c
        mat = []
        for ri in range(r):
            mat.append([1 if x == '@' else 0 for x in input()])
            rchips[ri] = rchips[ri-1] + sum(mat[ri])
            for ci, x in enumerate(mat[ri]):
                cchips_[ci] += x
        cchips = [0] * c
        for ci, x in enumerate(cchips_):
            cchips[ci] += cchips[ci-1] + cchips_[ci]
        print('Case #%s: %s' % (t, solve(mat, h, v, rchips, cchips)))


if __name__ == '__main__':
    main()
