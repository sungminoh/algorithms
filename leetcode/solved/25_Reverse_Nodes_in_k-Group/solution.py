#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '%r -> %r' % (self.val, self.next)


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        ret = h = ListNode(None)
        h.next = head
        s = e = head
        cnt = 1
        while e:
            n = e.next
            if cnt == k:
                s_, e_ = self.reverse(s, e)
                h.next = s_
                e_.next = n
                h = e_
                s = n
                cnt = 0
            e = n
            cnt += 1
        return ret.next

    def reverse(self, s, e):
        prev = ListNode(None)
        cur = s
        while prev != e:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return e, s


def main():
    nodes = [ListNode(int(x)) for x in input().split()]
    for i, n in enumerate(nodes[:-1]):
        n.next = nodes[i+1]
    k = int(input())
    print(Solution().reverseKGroup(nodes[0], k))



if __name__ == '__main__':
    main()
