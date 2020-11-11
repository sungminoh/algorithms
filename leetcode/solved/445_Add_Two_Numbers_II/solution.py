
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""
import sys
import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def len_list(l):
    i = 0
    while l:
        l = l.next
        i += 1
    return i


def reverse_list(l):
    # a -> b -> c -> d -> e
    p = None
    while l:
        n = l.next
        l.next = p
        p = l
        l = n
    return p


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = len_list(l1)
        s2 = len_list(l2)
        if s1 < s2:
            l1, l2 = l2, l1
            s1, s2 = s2, s1
        tail = None
        while s1 > 0:
            if s1 > s2:
                n = ListNode(l1.val)
            else:
                n = ListNode(l1.val + l2.val)
                l2 = l2.next
                s2 -= 1
            l1 = l1.next
            s1 -= 1
            n.next = tail
            tail = n

        # carry up
        n = tail
        head = None
        crr = 0
        while n:
            n.val += crr
            if n.val > 9:
                crr, n.val = divmod(n.val, 10)
            else:
                crr = 0
            if not n.next:
                head = n
            n = n.next

        if crr:
            head.next = ListNode(crr)
            head = head.next

        return reverse_list(tail)


def arr_to_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    n = head
    for i in arr[1:]:
        n.next = ListNode(i)
        n = n.next
    return head


def list_to_arr(lst):
    arr = []
    while lst:
        arr.append(lst.val)
        lst = lst.next
    return arr


@pytest.mark.parametrize('l1, l2, expected', [
    ([7,2,4,3], [5,6,4], [7,8,0,7]),
    ([5], [5], [1, 0]),
    ([0], [7,3], [7,3])
])
def test(l1, l2, expected):
    lst1 = arr_to_list(l1)
    lst2 = arr_to_list(l2)
    assert expected == list_to_arr(Solution().addTwoNumbers(lst1, lst2))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
