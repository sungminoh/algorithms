#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given the root of a binary tree with n nodes, where each node is uniquely assigned a value from 1 to n. You are also given a sequence of n values voyage, which is the desired pre-order traversal of the binary tree.

Any node in the binary tree can be flipped by swapping its left and right subtrees. For example, flipping node 1 will have the following effect:

Flip the smallest number of nodes so that the pre-order traversal of the tree matches voyage.

Return a list of the values of all flipped nodes. You may return the answer in any order. If it is impossible to flip the nodes in the tree to make the pre-order traversal match voyage, return the list [-1].

Example 1:

Input: root = [1,2], voyage = [2,1]
Output: [-1]
Explanation: It is impossible to flip the nodes such that the pre-order traversal matches voyage.

Example 2:

Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]
Explanation: Flipping node 1 swaps nodes 2 and 3, so the pre-order traversal matches voyage.

Example 3:

Input: root = [1,2,3], voyage = [1,2,3]
Output: []
Explanation: The tree's pre-order traversal already matches voyage, so no nodes need to be flipped.

Constraints:

	The number of nodes in the tree is n.
	n == voyage.length
	1 <= n <= 100
	1 <= Node.val, voyage[i] <= n
	All the values in the tree are unique.
	All the values in voyage are unique.
"""
import sys
from typing import Tuple
from typing import List
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
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        """
        Works when
        the values in the tree are not unique
        or the values in voyage are not unique.
        """
        def rec(node, i) -> Tuple[int, List[int]]:
            if not node:
                return 0, []
            print(node.val, i)
            if node.val != voyage[i]:
                return -1, None

            f = []
            success = False
            used, fl = rec(node.left, i+1)
            if used >= 0:
                f.extend(fl)
                ur, fr = rec(node.right, i+1+used)
                if ur >= 0:
                    f.extend(fr)
                    used += ur
                    success = True

            ff = [node.val]
            flip_success = False
            flip_used, ffl = rec(node.right, i+1)
            if flip_used >= 0:
                ff.extend(ffl)
                flip_ur, ffr = rec(node.left, i+1+flip_used)
                if flip_ur >= 0:
                    ff.extend(ffr)
                    flip_used += flip_ur
                    flip_success = True

            if success and flip_success:
                return (1 + used, f) if len(f) < len(ff) else (1 + flip_used, ff)
            if success:
                return (1 + used, f)
            if flip_success:
                return (1 + flip_used, ff)
            return -1, None

        used, flip = rec(root, 0)
        return flip if used >= 0 else [-1]



@pytest.mark.parametrize('nodes, voyage, expected', [
    ([1,2], [2,1], [-1]),
    ([1,2,3], [1,3,2], [1]),
    ([1,2,3], [1,2,3], []),
    ([2,1,None,4,3], [2,1,3,4], [1]),
    ([1,2,None,3], [1,3,2], [-1]),
    ([1,1,1,2,3,4,5], [1,1,5,4,1,3,2], [1,1,1]),
])
def test(nodes, voyage, expected):
    root = build_tree(nodes)
    print()
    print(root)
    print(voyage)
    assert expected == Solution().flipMatchVoyage(root, voyage)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))

