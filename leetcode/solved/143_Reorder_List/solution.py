#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return 'ListNode(%r)' % self.val


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        mid = self.get_mid(head)
        left = head
        right = self.reverse(mid)
        self.merge(left, right)

    def get_mid(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        ret = slow.next
        slow.next = None
        return ret

    def reverse(self, head):
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def merge(self, a, b):
        while b:
            an, bn = a.next, b.next
            a.next = b
            b.next = an
            a, b = an, bn


def print_nodes(head):
    while head:
        print(head)
        head = head.next


def main():
    nodes = [ListNode(int(x)) for x in input().split()]
    for i, n in enumerate(nodes[:-1]):
        n.next = nodes[i+1]
    head = nodes[0]
    print('## input ##')
    print_nodes(head)
    Solution().reorderList(head)
    print('## answer ##')
    print_nodes(head)


if __name__ == '__main__':
    main()
