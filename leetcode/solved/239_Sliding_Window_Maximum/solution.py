
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Constraints:
    1. 1 <= nums.length <= 10^5
    2. -10^4 <= nums[i] <= 10^4
    3. 1 <= k <= nums.length
"""
from collections import deque
import sys
from typing import List
import pytest


def print_tree(root):
    from itertools import zip_longest
    def build_lines(root):
        if not root:
            return [''], 0
        left, lw = build_lines(root.left)
        lp = ' '*lw
        right, rw = build_lines(root.right)
        rp = ' '*rw
        s = str(root)
        subs = [(l if l else lp) + ' '*len(s) + (r if r else rp) for l, r in zip_longest(left, right)]
        first_line = lp + s + rp
        return [first_line] + subs, len(first_line)
    lines, _ = build_lines(root)
    print('\n'.join(lines))


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return '(%r)' % self.val


def insert(root, node):
    if node.val < root.val:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)
    else:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)


def max_val(root):
    if root.right is None:
        return root.val
    else:
        return max_val(root.right)


def remove(root, val):
    if not root:
        return None
    elif root.val == val:
        if root.right is None:
            return root.left
        else:
            n = root.right
            while n.left:
                n = n.left
            root.val, n.val = n.val, root.val
            root.right = remove(root.right, n.val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        root.right = remove(root.right, val)
    return root


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        queue = deque()
        ret = []
        for i, n in enumerate(nums):
            if queue and queue[0] <= i - k:
                queue.popleft()
            while queue and nums[queue[-1]] < n:
                queue.pop()
            queue.append(i)
            if i >= k-1:
                ret.append(nums[queue[0]])
        return ret

    def _maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        root = Node(nums[0])
        for i in range(1, min(k, len(nums))):
            insert(root, Node(nums[i]))
        ret = [max_val(root)]
        for i in range(len(nums) - k):
            j = i + k
            insert(root, Node(nums[j]))
            root = remove(root, nums[i])
            ret.append(max_val(root))
        return ret


@pytest.mark.parametrize('nums, k, expected', [
    ([1,3,-1,-3,5,3,6,7], 3, [3,3,5,5,6,7]),
    ([1,-1], 1, [1, -1])
])
def test(nums, k, expected):
    assert expected == Solution().maxSlidingWindow(nums, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
