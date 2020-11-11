#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return 'ListNode(%s)' % self.val


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        if head.next == head:
            return head
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                while head is not slow:
                    slow = slow.next
                    head = head.next
                return head


def main():
    xs = [int(x) for x in input().split()]
    nodes = {x: ListNode(x) for x in xs}
    for i, x in enumerate(xs[:-1]):
        nodes[x].next = nodes[xs[i+1]]
    print(Solution().detectCycle(nodes[xs[0]]))


if __name__ == '__main__':
    main()
