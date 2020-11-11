
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
"""
from collections import defaultdict
import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.cnt = self.getSize(head)
        self.head = head

    def getSize(self, node):
        cnt = 0
        while node:
            cnt += 1
            node = node.next
        return cnt

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        node = self.head
        n = random.randint(0, self.cnt - 1)
        while n:
            n -= 1
            node = node.next
        return node.val


# Your Solution object will be instantiated and called as such:
def test():
    head = ListNode(1);
    head.next = ListNode(2);
    head.next.next = ListNode(3);
    solution = Solution(head);
    cnt = defaultdict(int)
    for i in range(10000):
        cnt[solution.getRandom()] += 1
    print(cnt)
