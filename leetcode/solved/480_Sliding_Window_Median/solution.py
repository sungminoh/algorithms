#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
Examples:

[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6

Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
Answers within 10^-5 of the actual value will be accepted as correct.
"""
from heapq import heappop
from heapq import heappush
import sys
from typing import List
import pytest


class Node:
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val  # val, count, num subnodes
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        from itertools import zip_longest
        left_lines = repr(self.left).split('\n') if self.left else []
        right_lines = repr(self.right).split('\n') if self.right else []
        node_padding = len(repr(self.val)) + 2
        left_padding = len(left_lines[0]) if left_lines else 0
        right_padding = len(right_lines[0]) if right_lines else 0
        lines = [' '*left_padding + rf'({self.val})' + ' '*right_padding]
        for ll, rl in zip_longest(left_lines, right_lines):
            if ll is not None:
                lines.append(ll + ' '*node_padding + (rl or ''))
            else:
                lines.append(' '*(node_padding + left_padding) + (rl or ''))
        return '\n'.join(lines)


def insert(root: Node, val: int) -> Node:
    if root is None:
        return Node([val, 1, 1])
    if val < root.val[0] :
        root.left = insert(root.left, val)
        root.left.parent = root
    elif val > root.val[0]:
        root.right = insert(root.right, val)
        root.right.parent = root
    else:
        root.val[1] += 1
    root.val[2] += 1
    return root


def delete(root: Node, val: int) -> Node:
    if root is None:
        return None
    if val < root.val[0]:
        l_size = root.left.val[2]
        l = delete(root.left, val)
        root.left = l
        if l:
            l.parent = root
        new_l_size = l.val[2] if l is not None else 0
        root.val[2] += new_l_size - l_size
        return root
    elif val > root.val[0]:
        r_size = root.right.val[2]
        r = delete(root.right, val)
        root.right = r
        if r:
            r.parent = root
        new_r_size = r.val[2] if r is not None else 0
        root.val[2] += new_r_size - r_size
        return root
    else:
        if root.val[1] > 1:
            root.val[1] -= 1
            root.val[2] -= 1
            return root
        else:
            if root.left is None:
                if root.right:
                    root.right.parent = None
                return root.right
            if root.right is None:
                if root.left:
                    root.left.parent = None
                return root.left
            else:
                parents = [root, root.right]
                while parents[-1].left:
                    parents.append(parents[-1].left)
                successor = parents[-1]
                diff = root.val[1] - successor.val[1] - 1
                root.val[0], successor.val[0] = successor.val[0], root.val[0]
                root.val[1], successor.val[1] = successor.val[1], root.val[1]
                for p in parents:
                    p.val[2] += diff
                root.right = delete(root.right, val)
                return root


def find_min(root):
    while root.left:
        root = root.left
    return root


def find_max(root):
    while root.right:
        root = root.right
    return root


def median(root: Node) -> int:
    l = root.left.val[2] if root.left is not None else 0
    r = root.right.val[2] if root.right is not None else 0
    c = root.val[1]
    # print(f'{l} - {root.val}{c} - {r}')
    while l+c < r or l > c+r:
        if l+c < r:
            root = root.right
            diff = root.left.val[2] if root.left is not None else 0
            l += diff + c
            r -= diff + root.val[1]
            c = root.val[1]
        else:
            root = root.left
            diff = root.right.val[2] if root.right is not None else 0
            l -= diff + root.val[1]
            r += diff + c
            c = root.val[1]
        # print(f'{l} - {root.val}{c} - {r}')
    if l+c == r:
        return (root.val[0] + find_min(root.right).val[0]) / 2
    if l == c + r:
        return (root.val[0] + find_max(root.left).val[0]) / 2
    return root.val[0]


class Solution:
    def _medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ret = []
        root = None
        i = 0
        while i < k:
            root = insert(root, nums[i])
            i += 1
        # print(root)
        ret.append(median(root))
        while i < len(nums):
            # print('-------------------------------------------')
            root = insert(root, nums[i])
            # print('-------------insert: ', nums[i])
            # print(root)
            root = delete(root, nums[i-k])
            # print('-------------delete: ', nums[i-k])
            # print(root)
            ret.append(median(root))
            i += 1

        return ret

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        def move(h1, h2):
            n, i = heappop(h1)
            heappush(h2, (-n, i))

        left_max_heap = []
        right_min_heap = []
        i = 0
        while i < k:
            heappush(left_max_heap, (-nums[i], i))
            i += 1
        while len(left_max_heap) > len(right_min_heap):
            move(left_max_heap, right_min_heap)

        def median():
            if k % 2 == 1:
                return right_min_heap[0][0]
            return (-left_max_heap[0][0] + right_min_heap[0][0]) / 2

        ret = []
        ret.append(median())

        while i < len(nums):
            if nums[i] > right_min_heap[0][0]:
                heappush(right_min_heap, (nums[i], i))
                if nums[i-k] <= right_min_heap[0][0]:
                    move(right_min_heap, left_max_heap)
            else:
                heappush(left_max_heap, (-nums[i], i))
                if nums[i-k] >= -left_max_heap[0][0]:
                    move(left_max_heap, right_min_heap)
            while left_max_heap and left_max_heap[0][1] <= i-k:
                heappop(left_max_heap)
            while right_min_heap and right_min_heap[0][1] <= i-k:
                heappop(right_min_heap)
            ret.append(median())
            i += 1
        return ret


@pytest.mark.parametrize('nums, k, expected', [
    ([1,3,-1,-3,5,3,6,7], 3, [1,-1,-1,3,5,6]),
    ([1,2,3,4,2,3,1,4,2], 3, [2,3,3,3,2,3,2]),
    ([5,2,2,7,3,7,9,0,2,3], 9, [3,3]),
    ([5,5,8,1,4,7,1,3,8,4], 8, [4.5,4.5,4]),
    ([9,7,0,3,9,8,6,5,7,6], 2, [8.0, 3.5, 1.5, 6.0, 8.5, 7.0, 5.5, 6.0, 6.5])
])
def test(nums, k, expected):
    print()
    assert expected == Solution().medianSlidingWindow(nums, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
