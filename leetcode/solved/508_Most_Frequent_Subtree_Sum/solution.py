
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3

return [2, -3, 4], since all the values happen only once, return all of them in any order.

Examples 2
Input:

  5
 /  \
2   -5

return [2], since 2 happens twice, however -5 only occur once.

Note:
You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
"""
import sys
from collections import defaultdict
from collections import Counter
from typing import List
import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return '(%r)' % self.val


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



class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        max_cnt = -float('inf')
        cnt = defaultdict(int)  # sum to count
        rev = defaultdict(set)  # count to sum
        def dfs(n):
            nonlocal max_cnt
            if n is None:
                return 0
            s = n.val + dfs(n.left) + dfs(n.right)
            if cnt[s] > 0:
                rev[cnt[s]].remove(s)
            cnt[s] += 1
            rev[cnt[s]].add(s)
            max_cnt = max(max_cnt, cnt[s])
            return s
        dfs(root)
        return rev[max_cnt]


@pytest.mark.parametrize('nodes, expected', [
    ([5,2,-3], [2,-3,4]),
    ([5,2,-5], [2]),
])
def test(nodes, expected):
    print()
    tree = build_tree(nodes)
    print_tree(tree)
    assert set(expected) == set(Solution().findFrequentTreeSum(tree))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
