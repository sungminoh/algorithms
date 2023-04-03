#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.

Return the root of the Quad-Tree representing grid.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

	val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
	isLeaf: True if the node is a leaf node on the tree or False if the node has four children.

class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}

We can construct a Quad-Tree from a two-dimensional area using the following steps:

	If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
	If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
	Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:

You don't need to read this section for solving the problem. This is only if you want to understand the output format here. The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.

Example 1:

Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represnts False and 1 represents True in the photo representing the Quad-Tree.

Example 2:

Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:

Constraints:

	n == grid.length == grid[i].length
	n == 2x where 0 <= x <= 6
"""
from collections import deque
from typing import List
import pytest
import sys


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    def serialize(self):
        queue = deque([self])
        ret = []
        while queue:
            n = queue.popleft()
            if n:
                ret.append([1 if n.isLeaf else 0, n.val])
                queue.extend([n.topLeft, n.topRight, n.bottomLeft, n.bottomRight])
            else:
                ret.append(None)
        while ret and ret[-1] is None:
            ret.pop()
        return ret


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        """Apr 28, 2020 22:55"""
        def build(i1, i2, j1, j2):
            if i1 == i2 and j1 == j2:
                return Node(grid[i1][j1], True, None, None, None, None)
            im = i1 + ((i2 - i1) // 2)
            jm = j1 + ((j2 - j1) // 2)
            lt = build(i1, im, j1, jm)
            lb = build(im + 1, i2, j1, jm)
            rt = build(i1, im, jm + 1, j2)
            rb = build(im + 1, i2, jm + 1, j2)
            leafs = [lt, lb, rt, rb]
            if all(n.isLeaf for n in leafs) \
                    and lt.val == lb.val == rt.val == rb.val:
                return Node(lt.val, True, None, None, None, None)
            return Node(0, False, lt, rt, lb, rb)

        if not grid:
            return []
        root = build(0, len(grid) - 1, 0, len(grid[0]) - 1)
        return root

    def construct(self, grid: List[List[int]]) -> 'Node':
        """Apr 02, 2023 15:21"""
        def build(x1, y1, x2, y2):
            if x1 == x2 and y1 == y2:
                return Node(grid[x1][y1], True, None, None, None, None)
            x = (x1+x2)//2
            y = (y1+y2)//2
            childrend = [
                build(x1, y1, x, y),
                build(x1, y+1, x, y2),
                build(x+1, y1, x2, y),
                build(x+1, y+1, x2, y2)
            ]
            if all(x.isLeaf for x in childrend) and len(set(x.val for x in childrend)) == 1:
                return Node(childrend[0].val, True, None, None, None, None)
            return Node(1, False, *childrend)

        return build(0, 0, len(grid)-1, len(grid[0])-1)


@pytest.mark.parametrize('args', [
    (([[0,1],[1,0]], [[0,1],[1,0],[1,1],[1,1],[1,0]])),
    (([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]], [[0,1],[1,1],[0,1],[1,1],[1,0],None,None,None,None,[1,0],[1,0],[1,1],[1,1]])),
])
def test(args):
    assert args[-1] == Solution().construct(*args[:-1]).serialize()


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
