#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:

Input: head = [2,1], x = 2
Output: [1,2]

Constraints:

	The number of nodes in the list is in the range [0, 200].
	-100 <= Node.val <= 100
	-200 <= x <= 200
"""
import sys
import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}' + ('' if not self.next else f' -> {self.next!r}')


def build(values):
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    return nodes[0] if nodes else None

def to_list(node: ListNode):
    ret = []
    while node:
        ret.append(node.val)
        node = node.next
    return ret


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        smaller_head = smaller_tail = ListNode(None)
        larger_head = larger_tail = ListNode(None)
        node = head
        while node:
            if node.val < x:
                smaller_tail.next = node
                smaller_tail = node
            else:
                larger_tail.next = node
                larger_tail = node
            node = node.next
        if not smaller_head.next or not larger_head.next:
            return head

        start = smaller_head.next
        tail = smaller_tail
        tail.next = larger_head.next
        tail = larger_tail
        tail.next = None
        return start


@pytest.mark.parametrize('nodes, x, expected', [
    ([1,4,3,2,5,2], 3, [1,2,2,4,3,5]),
    ([2,1], 2, [1,2]),
])
def test(nodes, x, expected):
    head = build(nodes)
    print(head)
    actual = Solution().partition(head, x)
    print(actual)
    assert expected == to_list(actual)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
