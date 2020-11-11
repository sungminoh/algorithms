#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        memo = dict()
        lst = []
        n = head
        while n:
            node = RandomListNode(n.label)
            node.random = id(n.random) if n.random else None
            memo[id(n)] = node
            lst.append(node)
            n = n.next
        for i in range(0, len(lst)-1):
            n = lst[i]
            if n.random:
                n.random = memo[n.random]
            n.next = lst[i+1]
        if lst:
            n = lst[-1]
            if n.random:
                n.random = memo[n.random]
        if lst:
            return lst[0]
        else:
            return None


def main():
    pass


if __name__ == '__main__':
    main()
