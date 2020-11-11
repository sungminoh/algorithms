#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import math


def solve(p, d):
    attack = 1
    damage = 0
    s_cnt = 0
    ci = []
    # build
    for i, c in enumerate(p):
        if c == 'S':
            s_cnt += 1
            damage += attack
        else:
            attack *= 2
            ci.append(i)
    # return simple case
    if damage <= d:
        return 0
    if s_cnt > d:
        return 'IMPOSSIBLE'
    cnt = 0
    # do swap
    last_idx = len(p) - 1
    while damage > d:
        if not ci:
            return 'IMPOSSIBLE'
        idx = ci.pop()
        deduct_amt = pow(2, len(ci))
        can_swap = last_idx - idx
        need_swap = math.ceil((damage - d) / deduct_amt)
        if can_swap >= need_swap:
            return cnt + need_swap
        cnt += can_swap
        damage -= deduct_amt * can_swap
        last_idx -= 1
    return cnt


def main():
    t = int(input())
    for i in range(1, t + 1):
        d, p = input().split()
        d = int(d)
        ans = solve(p, d)
        print('Case #%s: %s' % (i, ans))


if __name__ == '__main__':
    main()
