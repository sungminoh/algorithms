#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
import random


class Solution():
    def binary_search(self, arr, n):
        l, r = 0, len(arr) - 1
        while l <= r:
            k = l + (r - l) // 2
            if arr[k] < n:
                l = k + 1
            elif arr[k] > n:
                r = k - 1
            else:
                return k
        return -1


def gen_case():
    arr = list(range(random.randint(0, 50) + 1))
    n = random.randint(0, 50)
    try:
        i = arr.index(n)
    except ValueError:
        i = -1
    return (arr, n), i


if __name__ == "__main__":
    cases = [
        gen_case(),
        gen_case(),
        gen_case(),
        gen_case(),
        gen_case(),
        gen_case(),
        gen_case()
    ]
    for case, expected in cases:
        print(case, expected)
        actual = Solution().binary_search(*case)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
