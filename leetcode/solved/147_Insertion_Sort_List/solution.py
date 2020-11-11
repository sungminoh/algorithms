#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list


Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

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
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        prev = head
        cur = head.next
        while cur:
            if prev.val <= cur.val:
                prev = cur
                cur = cur.next
                continue
            n = self.pop(prev)
            if n.val < head.val:
                n.next = head
                head = n
                cur = prev.next
            else:
                position = self.find(n, head)
                n.next = position.next
                position.next = n
                cur = prev.next
        return head


    def find(self, node, head):
        if head.val <= node.val and (head.next == node.next or node.val <= head.next.val):
            return head
        else:
            return self.find(node, head.next)


    def pop(self, prev, cur=None):
        cur = cur or prev.next
        if cur:
            prev.next = cur.next
        return cur


def main():
    nodes = [ListNode(int(x)) for x in input().split()]
    for i, n in enumerate(nodes[:-1]):
        n.next = nodes[i+1]
    head = nodes[0]
    print(head)
    print(Solution().insertionSortList(head))


if __name__ == '__main__':
    main()
