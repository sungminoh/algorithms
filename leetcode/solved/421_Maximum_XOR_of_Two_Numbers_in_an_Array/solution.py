
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""
import sys
from typing import List
import pytest


class Node(object):
    def __init__(self):
        self.chars = {}


class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, n):
        b = '{:032b}'.format(n)
        cur = self.root
        for i in b:
            if i not in cur.chars:
                cur.chars[i] = Node()
            cur = cur.chars[i]


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        s = 0
        for i in range(31, -1, -1):
            digit = (1 << i)
            base = s + (1 << i)
            candidates = {((n // digit) << i) ^ base for n in nums}
            for n in nums:
                if (n // digit) << i in candidates:
                    s = base
                else:
                    s << 2
        return s

    def _findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for n in nums:
            trie.insert(n)

        def get_pair(trie, n):
            b = '{:032b}'.format(n)
            m = ''
            cur = trie.root
            for i in b:
                j = '1' if i == '0' else '0'
                if j in cur.chars:
                    m += j
                    cur = cur.chars[j]
                else:
                    m += i
                    cur = cur.chars[i]
            return int(m, 2)

        ret = 0
        for n in nums:
            m = get_pair(trie, n)
            ret = max(ret, n ^ m)
        return ret



@pytest.mark.parametrize('nums, expected', [
    ([3, 10, 5, 25, 2, 8], 28)
])
def test(nums, expected):
    assert expected == Solution().findMaximumXOR(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
