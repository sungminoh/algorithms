#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Implement the Solution class:

	Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
	int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.

Example 1:

Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.

Constraints:

	The number of nodes in the linked list will be in the range [1, 104].
	-104 <= Node.val <= 104
	At most 104 calls will be made to getRandom.

Follow up:

	What if the linked list is extremely large and its length is unknown to you?
	Could you solve this efficiently without using extra space?
"""
from collections import defaultdict
import random
from typing import Optional
import pytest
import sys
sys.path.append('../')
from exercise.list import build_list, ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """04/17/2020 21:37	"""
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


class Solution:
    """Jan 29, 2022 00:19"""
    def __init__(self, head: Optional[ListNode]):
        self.h = head
        self.c = self.h
        self.n = 0
        while head:
            self.n += 1
            head = head.next

    def getRandom(self) -> int:
        n = self.n
        while random.randrange(0, n) != 0:
            n -= 1
            self.c = self.c.next if self.c.next else self.h
        return self.c


class Solution:
    """Apr 11, 2023 23:19"""
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.cur = self.head
        self.cnt = 0
        while head:
            self.cnt += 1
            head = head.next

    def getRandom(self) -> int:
        n = self.cnt
        while random.randrange(0, self.cnt) > 0:
            n -= 1
            self.cur = self.cur.next if self.cur.next else self.head
        return self.cur.val


@pytest.mark.parametrize('args', [
     ([1, 2, 3])
])
def test(args):
    o = Solution(build_list(args))
    cnt = defaultdict(int)
    for i in range(10000):
        cnt[o.getRandom()] += 1
    print(cnt)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
