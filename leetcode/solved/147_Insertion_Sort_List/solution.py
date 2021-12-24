#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

	Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
	At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
	It repeats until no input elements remain.

The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Constraints:

	The number of nodes in the list is in the range [1, 5000].
	-5000 <= Node.val <= 5000
"""
from typing import Optional
import pytest
import sys
sys.path.append('../')
from exercise.list import ListNode, build_list


# Definition for singly-linked list.
class Solution:
    def insertionSortList(self, head):
        """07/27/2018 18:14"""
        def find(node, head):
            if head.val <= node.val and (head.next == node.next or node.val <= head.next.val):
                return head
            else:
                return find(node, head.next)

        def pop(prev, cur=None):
            cur = cur or prev.next
            if cur:
                prev.next = cur.next
            return cur

        if not head or not head.next:
            return head
        prev = head
        cur = head.next
        while cur:
            if prev.val <= cur.val:
                prev = cur
                cur = cur.next
                continue
            n = pop(prev)
            if n.val < head.val:
                n.next = head
                head = n
                cur = prev.next
            else:
                position = find(n, head)
                n.next = position.next
                position.next = n
                cur = prev.next
        return head

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def remove(p, n):
            nn = n.next
            p.next = nn
            n.next = None
            return p, nn

        def insert(h, n, e):
            p = h
            c = h.next
            while c and c != e:
                if c.val >= n.val:
                    p.next = n
                    n.next = c
                    return n, c
                p = c
                c = c.next
            p.next = n
            n.next = e
            return n, e

        h = ListNode(-float('inf'), next=head)
        p = h
        n = h.next
        while n:
            if p.val < n.val:  # accelerate
                p = n
                n = n.next
                continue
            np, nn = remove(p, n)
            n, nc = insert(h, n, nn)
            if nn == nc:
                np = n
            p = np
            n = nn

        return h.next


@pytest.mark.parametrize('values, expected', [
    ([4,2,1,3], [1,2,3,4]),
    ([-1,5,3,4,0], [-1,0,3,4,5]),
])
def test(values, expected):
    exp = build_list(expected)
    print()
    print(exp)
    assert exp == Solution().insertionSortList(build_list(values))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
