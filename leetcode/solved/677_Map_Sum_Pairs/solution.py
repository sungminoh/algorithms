#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:

Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
"""
import sys
from collections import defaultdict
import pytest


def infdict():
    return defaultdict(infdict)


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = infdict()

    def insert(self, key: str, val: int) -> None:
        def insert_at(d, k, v):
            d.setdefault('_', 0)
            if not k:
                diff = v - d.get('_end_', 0)
                d['_end_'] = v
                d['_'] += diff
                return diff
            diff = insert_at(d[k[0]], k[1:], v)
            d['_'] += diff
            return diff

        insert_at(self.d, key, val)

    def sum(self, prefix: str) -> int:
        d = self.d
        for c in prefix:
            d = d[c]
        return d.get('_', 0)


@pytest.mark.parametrize('commands, args, expecteds', [
    (['insert', 'sum', 'insert', 'sum'],
     [['apple', 3], ['ap'], ['app', 2], ['ap']],
     [None, 3, None, 5]),
])
def test(commands, args, expecteds):
    o = MapSum()
    for c, a, e in zip(commands, args, expecteds):
        assert e == getattr(o, c)(*a)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
