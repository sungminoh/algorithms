#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less = ListNode(None)
        lp = less
        greater = ListNode(None)
        gp = greater
        while head:
            if head.val < x:
                lp.next = head
                lp = lp.next
            else:
                gp.next = head
                gp = gp.next
            head = head.next
        lp.next = greater.next
        gp.next = None
        return less.next


def get_input():
    head = ListNode(None)
    t = head
    for n in (int(x) for x in input()):
        t.next = ListNode(n)
        t = t.next
    ret = head.next
    del(head)
    return ret


def main():
    nodes = get_input()
    n = Solution().partition(nodes, int(input()))
    while n:
        print(n.val)
        n = n.next


if __name__ == '__main__':
    main()
