#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

from typing import Any
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not other:
            return False
        return self.val == other.val and self.next == other.next

    def __repr__(self):
        ret = f'({self.val})'
        if self.next:
            ret += f'-{self.next}'
        return ret

    def __iter__(self):
        yield self.val
        if self.next:
            yield from self.next


def build_list(values: List[Any]):
    if not values:
        return None
    head = ListNode(values[0])
    node = head
    for i in range(1, len(values)):
        node.next = ListNode(values[i])
        node = node.next
    return head

