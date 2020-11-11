#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Print a binary tree in an m*n 2D string array following these rules:

The row number m should be equal to the height of the given binary tree.
The column number n should always be an odd number.
The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
Each unused space should contain an empty string "".
Print the subtrees following the same rules.

Example 1:

Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]

Example 2:

Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]

Example 3:

Input:
      1
     / \
    2   5
   /
  3
 /
4
Output:

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]

Note:
The height of binary tree is in the range of [1, 10].
"""
from astroid.util import lazy_import
import sys
from itertools import zip_longest
from typing import List
import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def get_depth(node):
            if not node:
                return 0
            return 1 + max(get_depth(node.left), get_depth(node.right))

        depth = get_depth(root)
        width = 2 ** depth - 1
        lines = [[""] * width for _ in range(depth)]

        if not lines:
            return lines

        def fill(node, d, i, j):
            if not node:
                return
            m = (i + j) // 2
            lines[d][m] = str(node.val)
            fill(node.left, d+1, i, m-1)
            fill(node.right, d+1, m+1, j)

        fill(root, 0, 0, len(lines[0])-1)
        return lines


@pytest.mark.parametrize('nodes, expected', [
    ([1, 2],
     [["", "1", ""],
      ["2", "", ""]]),
    ([1,2,3,None,4],
     [["", "", "", "1", "", "", ""],
      ["", "2", "", "", "", "3", ""],
      ["", "", "4", "", "", "", ""]]),
    ([1,2,5,3,None,None,None,4],
     [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""],
      ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""],
      ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""],
      ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]),
    ([3,1,5,0,2,4,6,None,None,None,3],
     [["","","","","","","",   "3", "","","","","","",""],
      ["","","","1","","","",  "",  "","","","5","","",""],
      ["","0","","","","2","", "",  "","4","","","","6",""],
      ["","","","","","","3",  "",  "","","","","","",""]])
])
def test(nodes, expected):
    print()
    actual = Solution().printTree(build_tree(nodes))
    for l in actual:
        print(l)
    assert expected == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
