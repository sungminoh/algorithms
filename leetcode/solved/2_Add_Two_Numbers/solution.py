#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(-1)
        p = head
        s = 0
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            s += (n1 + n2)
            r = s % 10
            s //= 10
            p.next = ListNode(r)
            p = p.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if s:
            p.next = ListNode(s)
        return head.next


def get_input():
    ret = ListNode(-1)
    p = ret
    for i in map(int, input().split()):
        p.next = ListNode(i)
        p = p.next
    return ret.next


def print_list(l):
    while l:
        print(l.val, end=' ')
        l = l.next
    print()


def main():
    a = get_input()
    b = get_input()
    c = Solution().addTwoNumbers(a, b)
    print_list(c)


if __name__ == '__main__':
    main()
