#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import sys
import random


def get_comb(total_length, number_of_two):
    if number_of_two == 0:
        return [[1] * total_length]
    elif total_length == number_of_two:
        return [[2] * total_length]
    if total_length-1 == number_of_two:
        ret = []
        for i in range(total_length):
            e = [2]*total_length
            e[i] = 1
            ret.append(e)
        return ret
    ret = []
    ret.extend([comb+[2] for comb in get_comb(total_length-1, number_of_two-1)])
    ret.extend([comb+[1] for comb in get_comb(total_length-1, number_of_two)])
    return ret


def gen_all_type(n):
    for i in range(0, n//2+1):
        total_length = n-i
        for comb_list in get_comb(total_length, i):
            print('get_comb(%d, %d)' % (total_length, i))
            yield comb_list


def divide(n):
    for m in range(0, n//2+1):
        yield (n-m, m)


def gen(lst):
    n = len(lst)
    if n == 1:
        return [lst[0], [[]]]
    if n == 0:
        return [None, [[]]]
    h = lst[0]
    trees = []
    for l, r in divide(n-1):
        lh, ll = gen(lst[1:1+l])
        rh, rl = gen(lst[1+l:])
        for lt in ll:
            for rt in rl:
                tree = []
                if lh is not None:
                    tree.append((h, lh))
                if rh is not None:
                    tree.append((h, rh))
                trees.append(tree + lt + rt)
    return [h, trees]


def main(n):
    head, trees = gen(list(range(1, n+1)))
    print(len(trees))
    for tree in trees:
        print(n)
        for u, v in tree:
            # print(u, v, random.randint(0, 10))
            print(u, v, 10)


if __name__ == '__main__':
    main(int(sys.argv[1]))
    # main(int(14))
