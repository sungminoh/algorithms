#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from itertools import product


def gen(chars_per_position, i):
    if i == len(chars_per_position)-1:
        for c in chars_per_position[i]:
            yield c
    else:
        for c in chars_per_position[i]:
            for sub in gen(chars_per_position, i+1):
                yield c + sub


def solve(words, n):
    chars_per_position = [set(x) for x in zip(*words)]
    for i, w in enumerate(gen(chars_per_position, 0)):
        if w not in words:
            return w
        if i > 2000:
            break
    return '-'



def solve2(words, n):
    if n <= 1:
        return '-'
    possibles = {''.join(e) for e in product(*zip(*words))} - words
    if len(possibles) == 0:
        return '-'
    else:
        return possibles.pop()


def main():
    T = int(input())
    for i in range(1, T+1):
        N, L = [int(x) for x in input().split()]
        words = {input() for _ in range(N)}
        print('Case #%s: %s' %(i, solve(words, L)))


if __name__ == '__main__':
    main()
