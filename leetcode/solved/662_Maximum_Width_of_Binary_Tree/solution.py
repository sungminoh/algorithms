#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary tree, write a function to get the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

Example 1:

Input:

           1
         /   \
        3     2
       / \     \
      5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

Example 2:

Input:

          1
         /
        3
       / \
      5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).

Example 3:

Input:

          1
         / \
        3   2
       /
      5

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).

Example 4:

Input:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).

Constraints:

	The given binary tree will have between 1 and 3000 nodes.
"""
import sys
from collections import deque
from collections import defaultdict
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
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        q = deque([(root, 0, 1)])
        d = 0
        n, m = 1, 1
        ret = 1
        while q:
            node, depth, pos = q.popleft()
            if depth != d:
                ret = max(ret, m-n+1)
                n = m = pos
                d = depth
            else:
                n = min(n, pos)
                m = max(m, pos)
            if node.left:
                q.append((node.left, depth+1, pos*2-1))
            if node.right:
                q.append((node.right, depth+1, pos*2))
        ret = max(ret, m-n+1)
        return ret

    def _widthOfBinaryTree(self, root: TreeNode) -> int:
        minmax = defaultdict(lambda: [float('inf'), -float('inf')])
        def traverse(node, depth, pos):
            if node is None:
                return
            minmax[depth][0] = min(minmax[depth][0], pos)
            minmax[depth][1] = max(minmax[depth][1], pos)
            traverse(node.left, depth+1, pos*2 - 1)
            traverse(node.right, depth+1, pos*2)

        traverse(root, 0, 1)
        return max(m - n + 1 for n, m in minmax.values())


@pytest.mark.parametrize('nodes, expected', [
    ([1,3,2,5,3,None,9], 4),
    ([1,3,None,5,3], 2),
    ([1,3,2,5], 2),
    ([1,3,2,5,None,None,9,6,None,None,7], 8),
])
def test(nodes, expected):
    print()
    root = build_tree(nodes)
    print(root)
    assert expected == Solution().widthOfBinaryTree(root)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
