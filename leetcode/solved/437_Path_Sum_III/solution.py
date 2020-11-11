#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
from collections import defaultdict
import sys
import pytest


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
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

    def __eq__(self, other):
        return other.val == self.val \
            and other.left == self.left \
            and other.right == self.right


def build_tree(lst):
    root = TreeNode(lst[0])
    queue = [root]
    att = ['left', 'right']
    cur = 0
    for x in lst[1:]:
        node = TreeNode(x) if x is not None else None
        setattr(queue[0], att[cur], node)
        if cur:
            queue.pop(0)
        if node:
            queue.append(node)
        cur += 1
        cur %= 2
    return root


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        cnt = 0
        memo = {0: 1}
        def dfs(node, acc):
            nonlocal cnt
            if not node:
                return
            acc += node.val
            cnt += memo.get(acc-sum, 0)
            if acc not in memo:
                memo[acc] = 0
            memo[acc] += 1
            dfs(node.left, acc)
            dfs(node.right, acc)
            memo[acc] -= 1

        dfs(root, 0)
        return cnt

    def _pathSum(self, root: TreeNode, sum: int) -> int:
        cnt = 0
        def rec(node, acc):
            nonlocal cnt
            if not node:
                return
            if 0 not in acc:
                acc[0] = 0
            acc[0] += 1
            cnt += acc.get(sum-node.val, 0)
            rec(node.left, {k+node.val: v for k, v in acc.items()})
            rec(node.right, {k+node.val: v for k, v in acc.items()})

        rec(root, {})
        return cnt


@pytest.mark.parametrize('nodes, sum, expected', [
    ([10,5,-3,3,2,None,11,3,-2,None,1], 8, 3),
    ([1], 1, 1),
    ([-2,None,-3], -5, 1)
])
def test(nodes, sum, expected):
    print()
    tree = build_tree(nodes)
    print(tree)
    assert expected == Solution().pathSum(tree, sum)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))

