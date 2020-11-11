#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '%r -> %r' % (self.val, self.next)


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        from heapq import heappush, heappop
        heap = []
        tmp = 0
        for n in lists:
            if n:
                heappush(heap, (n.val, (tmp, n)))
                tmp += 1
        if not heap:
            return None
        head = cur = ListNode(None)
        while heap:
            v, (_, n) = heappop(heap)
            cur.next = n
            cur = cur.next
            nn = n.next
            if nn:
                heappush(heap, (nn.val, (tmp, nn)))
                tmp += 1
        return head.next


def get_list():
    nodes = [ListNode(int(x)) for x in input().split()]
    if not nodes:
        return None
    for i, n in enumerate(nodes[:-1]):
        n.next = nodes[i+1]
    return nodes[0]


def main():
    lists = []
    nodes = get_list()
    while nodes:
        lists.append(nodes)
        nodes = get_list()
    print(Solution().mergeKLists(lists))


if __name__ == '__main__':
    main()
