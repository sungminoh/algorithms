#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        i = 1
        n = head
        while n.next is not None:
            i += 1
            n = n.next
        n.next = head
        n = head
        for _ in range(i-(k%i)-1):
            n = n.next
        head = n.next
        n.next = None
        return head


def main():
    nodes = [ListNode(int(x)) for x in input().split()]
    k = int(input())
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    head = Solution().rotateRight(nodes[0], k)
    while head is not None:
        print(head.val, end=' ')
        head = head.next


if __name__ == '__main__':
    main()
