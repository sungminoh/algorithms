#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [0,1,3,5,6]
Output: 3
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had
             received 0, 1, 3, 5, 6 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
Note:

If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:

This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
Could you solve it in logarithmic time complexity?
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        s, e = 0, len(citations) - 1
        m = 0
        while s <= e:
            i = (s + e) // 2
            if citations[i] >= len(citations) - i:
                m = max(m, len(citations) - i)
                e = i - 1
            else:
                s = i + 1
        return m


def main():
    cases = [
        ([0,1,3,5,6], 3),
        ([3,3,3,3,3], 3),
        ([], 0),
        ([5,5,5,5,5], 5),
        ([4,4,4,4,4], 4),
        ([1,1,1,1,1], 1),
    ]
    for case, expected in cases:
        actual = Solution().hIndex(case)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')


if __name__ == '__main__':
    main()
