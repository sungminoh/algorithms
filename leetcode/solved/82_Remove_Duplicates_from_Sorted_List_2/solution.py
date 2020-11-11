#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        c = dummy
        while c:
            if not c.next or not c.next.next:
                return dummy.next
            n = c.next
            nn = n.next
            deduped = False
            while nn and n.val == nn.val:
                deduped = True
                nn = nn.next
            if deduped:
                c.next = nn
            else:
                c = c.next
        return dummy.next


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
    n = Solution().deleteDuplicates(nodes)
    while n:
        print(n.val)
        n = n.next


if __name__ == '__main__':
    main()
