#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import defaultdict

class Solution:
    def generateTrees(self, n):
        memo = defaultdict(dict)
        def generateTreesDP(n, add):
            if n == 0:
                return [None]
            if n == 1:
                return [TreeNode(1 + add)]
            if n in memo and add in memo[n]:
                return memo[n][add]
            ret = []
            for i in range(1, n+1):
                left_trees = generateTreesDP(i-1, add)
                right_trees = generateTreesDP(n-i, add+i)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(add+i)
                        root.left = left
                        root.right = right
                        ret.append(root)
            memo[n][add] = ret
            return ret

        if n == 0:
            return []
        return self.generateTreesDP(n, 0)


for_print = defaultdict(list)
def tree2list(root, depth=0):
    if depth == 0:
        for_print.clear()
    if not root:
        return for_print[depth].append(None)
    for_print[depth].append(root.val)
    tree2list(root.left, depth+1)
    tree2list(root.right, depth+1)
    ret = []
    for d in sorted(for_print.keys()):
        l = for_print[d]
        for i, v in enumerate(l):
            if v is not None:
                ret.extend(l[max(0, i-1):])
                break
    while ret and not ret[-1]:
        ret.pop()
    return ret


def main():
    n = int(input())
    trees = Solution().generateTrees(n)
    for t in trees:
        print(tree2list(t))


if __name__ == '__main__':
    main()
