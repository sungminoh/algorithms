#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m >= n:
            return head
        parent = None
        p = head
        for _ in range(m-1):
            parent = p
            p = p.next
        t = p
        tmp = p.next
        child = tmp
        for _ in range(n-m):
            child = tmp
            if child:
                tmp = child.next
                child.next = p
                p = child
            else:
                break
        t.next = tmp
        if parent:
            parent.next = p
            return head
        else:
            return child


def main():
    nodes = [ListNode(int(x)) for x in input().split()]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    head = nodes[0]
    m, n = [int(x) for x in input().split()]
    h = Solution().reverseBetween(head, m, n)
    while h:
        print(h.val, end=' ')
        h = h.next



if __name__ == '__main__':
    main()
