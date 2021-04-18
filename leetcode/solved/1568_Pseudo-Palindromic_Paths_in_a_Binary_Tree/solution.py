#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Example 1:

Input: root = [2,3,1,3,1,null,1]
Output: 2
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 2:

Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:

Input: root = [9]
Output: 1

Constraints:

	The number of nodes in the tree is in the range [1, 105].
	1 <= Node.val <= 9
"""
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


def is_leaf(node):
    return node.left is None and node.right is None



class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def toggle(s, v):
            if v in s:
                s.remove(v)
            else:
                s.add(v)

        def dfs(node, odd):
            if is_leaf(node):
                toggle(odd, node.val)
                ret = 1 if len(odd) <= 1 else 0
                toggle(odd, node.val)
                return ret
            cnt = 0
            toggle(odd, node.val)
            if node.left:
                cnt += dfs(node.left, odd)
            if node.right:
                cnt += dfs(node.right, odd)
            toggle(odd, node.val)
            return cnt

        return dfs(root, set())


@pytest.mark.parametrize('nodes, expected', [
    ([2,3,1,3,1,None,1], 2),
    ([2,1,1,1,3,None,None,None,None,None,1], 1),
    ([9], 1),

])
def test(nodes, expected):
    tree = build_tree(nodes)
    print()
    print(tree)
    assert expected == Solution().pseudoPalindromicPaths(tree)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
