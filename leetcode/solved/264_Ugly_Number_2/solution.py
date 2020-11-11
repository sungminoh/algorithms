#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.
"""


class Solution:
    def nthUglyNumber_(self, n: int) -> int:
        primeIdx = {2: 0, 3: 0, 5: 0}
        size = 1
        nums = [1]
        while size < n:
            m = min(p * nums[i] for p, i in primeIdx.items())
            for p, i in primeIdx.items():
                if p * nums[i] == m:
                    primeIdx[p] += 1
            nums.append(m)
            size += 1
        return nums[-1]

    def nthUglyNumber(self, n: int) -> int:
        primeIdx = {2: 0, 3: 0, 5: 0}
        size = 1
        offset = 0
        nums = [1]
        while size < n:
            m = min(p * nums[i - offset] for p, i in primeIdx.items())
            for p, i in primeIdx.items():
                if p * nums[i - offset] == m:
                    primeIdx[p] += 1
            nums.append(m)
            size += 1
            minIdx = min(primeIdx.values())
            nums = nums[minIdx - offset:]
            offset = minIdx
        return nums[-1]


def main():
    inputs = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ]
    exptecteds = [
        1, 2, 3, 4, 5, 6, 8, 9, 10, 12
    ]
    for n, expected in zip(inputs, exptecteds):
        actual = Solution().nthUglyNumber(n)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')


if __name__ == '__main__':
    main()
