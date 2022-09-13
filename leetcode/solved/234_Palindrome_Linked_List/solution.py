#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

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
from typing import Optional
import pytest
import sys
sys.path.append('../')
from exercise.list import ListNode, build_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """04/20/2021 23:49
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
        """04/21/2021 00:11
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


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # [] -> a -> b -> c -> d -> e(or None)
        # []    a <- b    c -> d -> e(or None)
        #            | p  | s       | fast
        dummy = ListNode()
        dummy.next = head
        parent = dummy
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            next_slow = slow.next
            slow.next = parent
            parent, slow = slow, next_slow
        head.next = None  # detach dummy

        # compare and restore
        right = slow if not fast else slow.next
        left = parent
        parent = slow
        ret = True
        while left:
            if left.val != right.val:
                ret = False
            right = right.next
            next_left = left.next
            left.next = parent
            left, parent = next_left, left
        return ret


@pytest.mark.parametrize('values, expected', [
    ([1,2,3,4,5], False),
    ([1,2,3,2,1], True),
    ([1,2,2,1], True),
    ([1,2], False),
    ([1], True)
])
def test(values, expected):
    head = build_list(values)
    assert expected == Solution().isPalindrome(head)
    # To make sure there was no inplace change
    assert build_list(values) == head


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
