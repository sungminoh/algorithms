
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""
from pathlib import Path
import json
import sys
from collections import defaultdict
from typing import List
import pytest


def binsearch(nums, n):
    i, j = 0, len(nums)-1
    while i <= j:
        m = i + (j-i)//2
        if n <= nums[m]:
            j = m - 1
        else:
            i = m + 1
    return i


class TreeNode:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None
        self.cnt = 1


def insert(root, n):
    while root :
        root.cnt += 1
        if n < root.val:
            if root.left is None:
                root.left = TreeNode(n)
                break
            else:
                root = root.left
        else:
            if root.right is None:
                root.right = TreeNode(n)
                break
            else:
                root = root.right


def cnt_smaller(root, n):
    ret = 0
    while root:
        if root.val < n:
            ret += 1
            if root.left:
                ret += root.left.cnt
            root = root.right
        else:
            root = root.left
    return ret


class Solution:
    def _countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        root = TreeNode(nums[-1])
        ret = [0]
        for i in range(len(nums)-2, -1, -1):
            insert(root, nums[i])
            ret.append(cnt_smaller(root, nums[i]))
        return list(reversed(ret))


    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        ret = [0]
        ordered = [nums[-1]]
        for n in nums[-2::-1]:
            i = binsearch(ordered, n)
            ordered.insert(i, n)
            ret.append(i)
        return ret[::-1]


@pytest.mark.parametrize('nums, expected', [
    ([5,2,6,1], [2,1,1,0]),
    json.load(open(f'{Path(__file__).parent}/testcase.json')),
])
def test(nums, expected):
    assert expected == Solution().countSmaller(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
