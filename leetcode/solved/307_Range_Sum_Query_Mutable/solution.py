#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""
from typing import List


class NumArray:
    class Node(object):
        def __init__(self):
            self.left_index = -1
            self.right_index = -1
            self.left = None
            self.right = None
            self.summation = 0

    def print_tree(self):
        def str_tree(node):
            if not node:
                return ['']
            left_lines = str_tree(node.left)
            right_lines = str_tree(node.right)
            cur = f'{node.summation} ({node.left_index}, {node.right_index})'
            lines = [' ' * len(left_lines[0]) + cur + ' ' * len(right_lines[0])]
            lines.extend([l + ' ' * len(cur) + r for l, r in zip(left_lines, right_lines)])
            return lines

        lines = str_tree(self.root)
        for l in lines:
            print(l)

    def build_tree(self, i, j):
        mid = (i + j) // 2
        root = self.Node()
        root.left_index = mid
        root.right_index = mid
        if i == j:
            root.summation = self.nums[i]
            return root
        root.left = self.build_tree(i, mid)
        root.right = self.build_tree(mid + 1, j)
        if root.left:
            root.left_index = root.left.left_index
            root.summation += root.left.summation
        if root.right:
            root.right_index = root.right.right_index
            root.summation += root.right.summation
        return root

    def __init__(self, nums: List[int]):
        self.nums = nums
        if nums:
            self.root = self.build_tree(0, len(nums) - 1)
        else:
            self.root = None

    def update(self, i: int, val: int) -> None:
        change = val - self.nums[i]
        self.nums[i] = val
        node = self.root
        while node:
            if node.left_index == i and node.right_index == i:
                node.summation = val
                break
            node.summation += change
            if i > node.left.right_index:
                node = node.right
            else:
                node = node.left

    def sumRange(self, i: int, j: int) -> int:
        def sum_range(node, i, j):
            if node.left_index == i and node.right_index == j:
                return node.summation
            if node.left.right_index >= j:
                return sum_range(node.left, i, j)
            elif node.right.left_index <= i:
                return sum_range(node.right, i, j)
            else:
                return sum_range(node.left, i, node.left.right_index) \
                    + sum_range(node.right, node.right.left_index, j)
        return sum_range(self.root, i, j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

if __name__ == '__main__':
    num_array = NumArray([1,3,5,6,7,8,9,10])
    print(num_array.sumRange(0, 2), 9)
    num_array.update(1, 2)
    print(num_array.sumRange(0, 2), 8)
    cases = [
        ((["NumArray"], [[[]]]), []),
        ((["NumArray","update","update","update","sumRange","update","sumRange","update","sumRange","sumRange","update"]
          ,[[[7,2,7,2,0]],[4,6],[0,2],[0,9],[4,4],[3,8],[0,4],[4,1],[0,3],[0,4],[0,4]]),
         [None,None,None,None,6,None,32,None,26,27,None])
    ]
    for (commands, args), expected in cases:
        actual = [None]
        num_array = globals()[commands[0]](*args[0])
        num_array.print_tree()
        for cmd, arg in zip(commands[1:], args[1:]):
            ret = getattr(num_array, cmd)(*arg)
            print(cmd, arg, ret)
            if cmd == 'update':
                num_array.print_tree()
            actual.append(ret)

        print(f'{all(x == y for x, y in zip(expected, actual))}\texpected: {expected}\tactual: {actual}')
