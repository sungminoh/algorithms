#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
             received 3, 0, 6, 1, 5 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        m = 0
        for i, n in enumerate(reversed(sorted(citations))):
            if n >= i + 1:
                m = max(m, i + 1)
        return m


def main():
    cases = [
        ([3,0,6,1,5], 3),
        ([3,3,3,3,3], 3),
        ([0], 0)
    ]
    for case, expected in cases:
        actual = Solution().hIndex(case)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')


if __name__ == '__main__':
    main()

