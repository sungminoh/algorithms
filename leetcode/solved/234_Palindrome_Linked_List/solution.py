#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false

Constraints:

	The number of nodes in the list is in the range [1, 105].
	0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""
import sys
from typing import List
import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> {self.next}'


def build_list(nodes: List):
    if not nodes:
        return None
    head = ListNode(nodes[0])
    node = head
    for v in nodes[1:]:
        node.next = ListNode(v)
        node = node.next
    return head


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        def get_size(node: ListNode):
            size = 0
            while node:
                node = node.next
                size += 1
            return size

        size = get_size(head)
        stack = []
        node = head
        for i in range(size//2):
            stack.append(node.val)
            node = node.next
        if size%2 == 1:
            node = node.next
        while node:
            if stack[-1] != node.val:
                return False
            stack.pop()
            node = node.next
        return True


    def isPalindrome(self, head: ListNode) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        def same(h1, h2):
            while h1 and h2:
                if h1.val != h2.val:
                    return False
                h1 = h1.next
                h2 = h2.next
            return h1 is None and h2 is None

        def reverse(h):
            t = h
            p = None
            while h:
                n = h.next
                h.next = p
                p, h = h, n
            return p, t

        # Empty or single node list
        if not head or not head.next:
            return True
        # Find the middle while reverse from the middle to the head
        rev, slow, fast = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            tmp = rev
            rev, slow = slow, slow.next
            rev.next = tmp
        mid = slow
        # When the fast is not None, the number of nodes is odd
        if fast:
            slow = slow.next
        # Compare the remaining list from the middle to the end with the reversed list
        ret = same(rev, slow)
        # Revert the reversed list
        h, t = reverse(rev)
        t.next = mid
        # Return the result
        return ret


@pytest.mark.parametrize('nodes, expected', [
    ([1,2,3,4,5], False),
    ([1,2,3,2,1], True),
    ([1,2,2,1], True),
    ([1,2], False),
    ([1], True)
])
def test(nodes, expected):
    ll = build_list(nodes)
    assert expected == Solution().isPalindrome(ll)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
