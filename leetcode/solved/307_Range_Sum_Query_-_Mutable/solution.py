#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, handle multiple queries of the following types:

	Update the value of an element in nums.
	Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

	NumArray(int[] nums) Initializes the object with the integer array nums.
	void update(int index, int val) Updates the value of nums[index] to be val.
	int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

Constraints:

	1 <= nums.length <= 3 * 104
	-100 <= nums[i] <= 100
	0 <= index < nums.length
	-100 <= val <= 100
	0 <= left <= right < nums.length
	At most 3 * 104 calls will be made to update and sumRange.
"""
import operator
import sys
from typing import List
import pytest
from dataclasses import dataclass


class NumArray:
    """12/10/2019 00:22"""
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


class SegmentTree(object):
    @dataclass
    class Node(object):
        v: int

        def __repr__(self):
            return str(self.v)

    def __init__(self, nums: List[int], func=lambda l, r: sum(l, r)):
        self.func = func
        self.size = len(nums)
        if not nums:
            self.arr = []
            self.depth = -1
            return
        self.depth = 0
        while 2 ** self.depth < len(nums):
            self.depth += 1
        self.arr = [self.Node(None) for _ in range(pow(2, self.depth + 1) - 1)]

        def _rec(root, l, r, i, j):
            if l == r:
                self.arr[root].v = nums[l]
                return
            m = l + ((r - l) // 2)
            v = None
            if i <= m:
                _rec(self.left(root), l, m, i, min(j, m))
            if j > m:
                _rec(self.right(root), m + 1, r, m + 1, j)
            v = None
            if i <= m:
                v = self.arr[self.left(root)].v
            if j > m:
                if v is None:
                    v = self.arr[self.right(root)].v
                else:
                    v = self.func(v, self.arr[self.right(root)].v)
            self.arr[root].v = v

        _rec(0, 0, pow(2, self.depth) - 1, 0, len(nums) - 1)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2

    def update(self, i: int, val: int) -> None:
        def _rec(root, l, r, i, val):
            if l == r == i:
                self.arr[root].v = val
                return
            m = l + ((r - l) // 2)
            if i <= m:
                _rec(self.left(root), l, m, i, val)
                if m + 1 <= self.size - 1:
                    self.arr[root].v = self.func(self.arr[self.left(root)].v, self.arr[self.right(root)].v)
                else:
                    self.arr[root].v = self.arr[self.left(root)].v
            else:
                _rec(self.right(root), m + 1, r, i, val)
                self.arr[root].v = self.func(self.arr[self.left(root)].v, self.arr[self.right(root)].v)
        _rec(0, 0, pow(2, self.depth) - 1, i, val)

    def getRange(self, i: int, j: int) -> int:
        def _rec(root, l, r, i, j):
            if l >= i and r <= j:
                return self.arr[root].v
            m = l + ((r - l) // 2)
            if i <= m and j <= m:
                return _rec(self.left(root), l, m, i, j)
            elif m < i and m < j:
                return _rec(self.right(root), m + 1, r, i, j)
            else:
                return self.func(_rec(self.left(root), l, m, i, m),
                                 _rec(self.right(root), m + 1, r, m + 1, j))
        return _rec(0, 0, pow(2, self.depth) - 1, i, j)


class NumArray(SegmentTree):
    """04/16/2020 00:14"""
    def __init__(self, nums: List[int]):
        super().__init__(nums, lambda x, y: x + y)

    def update(self, i: int, val: int) -> None:
        super().update(i, val)

    def sumRange(self, i: int, j: int) -> int:
        return super().getRange(i, j)


class NumArray:
    """07/17/2021 19:43"""
    def __init__(self, nums: List[int]):
        self.size = len(nums)

        def build(l, r):
            if l == r:
                return [nums[l], None, None]
            m = l + (r-l)//2
            left = build(l, m)
            right = build(m+1, r)
            return [left[0] + right[0], left, right]

        self.tree = build(0, self.size-1)

    def update(self, index: int, val: int) -> None:
        def change_val(l, r, node):
            nval, lnode, rnode = node
            if l == r == index:
                diff = val - nval
            else:
                m = l + (r-l)//2
                if index <= m:
                    diff = change_val(l, m, lnode)
                else:
                    diff = change_val(m+1, r, rnode)
            node[0] += diff
            return diff

        change_val(0, self.size-1, self.tree)

    def sumRange(self, left: int, right: int) -> int:
        def query(l, r, left, right, node):
            nval, lnode, rnode = node
            if l == left and r == right:
                return nval
            m = l + (r-l)//2
            if right <= m:
                return query(l, m, left, right, lnode)
            if left > m:
                return query(m+1, r, left, right, rnode)
            return query(l, m, left, m, lnode) + query(m+1, r, m+1, right, rnode)

        return query(0, self.size-1, left, right, self.tree)


class NumArray:
    """08/14/2022 16:14
    Binary indexed tree
    """
    def __init__(self, nums: List[int]):
        self.nums = [0] * len(nums)
        self.tree = [0] * (len(nums)+1)
        for i, n in enumerate(nums):
            self.update(i, n)

    def update(self, index: int, val: int) -> None:
        val, self.nums[index] = val - self.nums[index], val
        index += 1
        while index < len(self.tree):
            self.tree[index] += val
            index += index&-index

    def sumRange(self, left: int, right: int) -> int:
        def query(i):
            idx = i
            ret = 0
            i += 1
            while i>0:
                ret += self.tree[i]
                i -= i&-i
            return ret

        return query(right) - query(left-1)


class NumArray:
    """08/14/2022 17:13
    Segment tree
    """
    def __init__(self, nums: List[int]):
        def build(i, j):
            """ Returns [value, acc, left, right] """
            if j < i:
                return None
            m = i + (j-i)//2
            left = build(i, m-1)
            right = build(m+1, j)
            acc = self.agg(
                nums[m],
                self.agg(
                    left[1] if left else self.identity,
                    right[1] if right else self.identity
                ))
            return [nums[m], acc, left, right]

        self.agg = operator.add
        self.identity = 0
        self.size = len(nums)
        self.tree = build(0, self.size-1)

    def update(self, index: int, val: int) -> None:
        def change(i, v, l, r, branch):
            m = l + (r-l)//2
            left = branch[2][1] if branch[2] else self.identity
            right = branch[3][1] if branch[3] else self.identity
            if i < m:
                left = change(i, v, l, m-1, branch[2])
            elif i > m:
                right = change(i, v, m+1, r, branch[3])
            else:
                branch[0] = v
            branch[1] = self.agg(
                branch[0],
                self.agg(left, right))
            return branch[1]

        change(index, val, 0, self.size-1, self.tree)

    def sumRange(self, left: int, right: int) -> int:
        def query(i, j, l, r, branch):
            if j < i:
                return self.identity
            if i == l and j == r:
                return branch[1]
            m = l + (r-l)//2
            if m < i:
                return query(i, j, m+1, r, branch[3])
            if j < m:
                return query(i, j, l, m-1, branch[2])
            # i<=m<=j:
            return self.agg(
                branch[0],
                self.agg(
                    query(i, m-1, l, m-1, branch[2]),
                    query(m+1, j, m+1, r, branch[3])
                ))

        return query(left, right, 0, self.size-1, self.tree)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["NumArray", "sumRange", "update", "sumRange"],
     [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]],
     [None, 9, None, 8]),
    (["NumArray","update","sumRange","sumRange","update","sumRange"],
     [[[9,-8]],[0,3],[1,1],[0,1],[1,-3],[0,1]],
     [None,None,-8,-5,None,0]),
    (["NumArray","sumRange","update","update","update","update","sumRange"],
     [[[5,18,13]],[0,2],[1,-1],[2,3],[0,5],[0,-4],[0,2]],
     [None,36,None,None,None,None,-2]),
    (["NumArray","sumRange","sumRange","sumRange","update","update","update","sumRange","update","sumRange","update"],
     [[[0,9,5,7,3]],[4,4],[2,4],[3,3],[4,5],[1,7],[0,8],[1,2],[1,9],[4,4],[3,4]],
     [None, 3, 15, 7, None, None, None, 12, None, 5, None])
])
def test(commands, arguments, expecteds):
    obj = globals()[commands.pop(0)](*arguments.pop(0))
    actual = []
    for cmd, arg in zip(commands, arguments):
        actual.append(getattr(obj, cmd)(*arg))
    assert expecteds[1:] == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))

