
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
"""
from itertools import zip_longest
import sys
from typing import List
import pytest


class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.cnt = 1
        self.size = 1

    def __repr__(self):
        left = repr(self.left).split('\n') if self.left else ['']
        right = repr(self.right).split('\n') if self.right else ['']
        if not left and not right:
            return str(self.val)
        else:
            lines = [' ' * len(left[0]) + str(self.val)]
            for l, r in zip_longest(left, right):
                lines.append(f'{l or ""}  {r or ""}')
            return '\n'.join(lines)


class SegmentTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        node = self.root
        while node is not None:
            node.size += 1
            if val < node.val:
                if not node.left:
                    node.left = Node(val)
                    break
                else:
                    node = node.left
            elif val > node.val:
                if not node.right:
                    node.right = Node(val)
                    break
                else:
                    node = node.right
            else:
                node.cnt += 1
                return

    def cnt_smaller(self, val, include_equals=False):
        if not self.root:
            return 0
        ret = 0
        node = self.root
        while node:
            if val < node.val:
                node = node.left
            elif val > node.val:
                ret += node.size
                node = node.right
                ret -= node.size if node else 0
            else:
                ret += node.left.size if node.left else 0
                if include_equals:
                    return ret + node.cnt
                else:
                    return ret
        return ret

    def __repr__(self):
        return repr(self.root)


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if not nums:
            return 0
        tree = SegmentTree()
        tree.insert(0)
        ret = 0
        s = 0
        for n in nums:
            s += n
            # lower <= s - x <= upper
            # s - upper <= x <= s - lower
            i = tree.cnt_smaller(s - upper)
            j = tree.cnt_smaller(s - lower, include_equals=True)
            tree.insert(s)
            ret += j-i
        return ret


@pytest.mark.parametrize('nums, lower, upper, expected', [
    ([-2,5,-1], -2, 2, 3),
    ([0,-3,-3,1,1,2], 3, 5, 2),
])
def test(nums, lower, upper, expected):
    assert expected == Solution().countRangeSum(nums, lower, upper)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
