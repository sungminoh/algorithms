#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""


def solve(W):
    memo = {0: 0, 1: W[0]}
    n = len(W)
    for i in range(1, n):
        new_memo = {}
        for n, s in memo.items():
            new_s = s + W[i]
            if s <= 6*W[i] and new_s < memo.get(n+1, float('inf')):
                new_memo[n+1] = new_s
        memo.update(new_memo)
    return max(memo.items(), key=lambda x: x[0])[0]


# def solve(W):
    # size = len(W)
    # memo = [float('inf')] * (size+1)
    # memo[0] = 0
    # memo[1] = W[0]
    # for i in range(1, size):
        # for n in range(i+1):
            # s = memo[n]
            # new_s = s + W[i]
            # if s <= 6*W[i] and new_s < memo[n+1]:
                # memo[n+1] = new_s
    # for i in range(size, -1, -1):
        # if memo[i] < float('inf'):
            # return i



def main():
    T = int(input())
    for i in range(1, T+1):
        N = int(input())
        W = [int(x) for x in input().split()]
        print('Case #%s: %s' %(i, solve(W)))


if __name__ == '__main__':
    main()
