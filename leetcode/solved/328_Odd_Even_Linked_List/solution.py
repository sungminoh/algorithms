#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...|
"""
import random
import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        even, odd = head, head.next
        even_tail, odd_tail = even, odd
        i = 2
        node = head.next.next
        while node:
            if i % 2 == 0:
                even_tail.next = node
                even_tail = node
            else:
                odd_tail.next = node
                odd_tail = node
            i += 1
            node = node.next
        even_tail.next = odd
        odd_tail.next = None
        return even


def gen_case():
    n = random.randint(0, 10)
    head = ListNode(random.randint(0, 100))
    node = head
    for _ in range(n):
        new_node = ListNode(random.randint(0, 100))
        node.next = new_node
        node = new_node
    return head


@pytest.mark.parametrize('node', [
    gen_case(),
    gen_case(),
    gen_case(),
    gen_case(),
])
def test(node):
    vals = node_to_list(node)
    print(vals)
    ans = node_to_list(Solution().oddEvenList(node))
    assert vals[0::2] + vals[1::2] == ans


def node_to_list(node):
    vals = []
    while node:
        vals.append(node.val)
        node = node.next
    return vals
