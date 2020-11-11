#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '%r -> %r' % (self.val, self.next)


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        mid = self.get_mid(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        return self.merge(left, right)

    def get_mid(self, head):
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, a, b):
        dummy = ListNode(None)
        cur = dummy
        while a or b:
            if not b or (a and a.val < b.val):
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next
            cur = cur.next
        return dummy.next


def main():
    nodes = [ListNode(int(x)) for x in input().split()]
    for i, n in enumerate(nodes[:-1]):
        n.next = nodes[i+1]
    head = nodes[0]
    print(Solution().sortList(head))


if __name__ == '__main__':
    main()
