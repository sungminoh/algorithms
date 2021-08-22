#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design a map that allows you to do the following:

	Maps a string key to a given value.
	Returns the sum of the values that have a key with a prefix equal to a given string.

Implement the MapSum class:

	MapSum() Initializes the MapSum object.
	void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
	int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.

Example 1:

Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)

Constraints:

	1 <= key.length, prefix.length <= 50
	key and prefix consist of only lowercase English letters.
	1 <= val <= 1000
	At most 50 calls will be made to insert and sum.
"""
import sys
from collections import defaultdict
import pytest


def infdict():
    return defaultdict(infdict)


class MapSum:
    """08/17/2020 09:44
    Using trie
    """
    def __init__(self):
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


class MapSum:
    """
    Precalculate for possible prefixes
    """
    def __init__(self):
        self.prefix = defaultdict(set)
        self.values = []
        self.keyindex = dict()

    def insert(self, key: str, val: int) -> None:
        # update key value
        if key in self.keyindex:
            self.values[self.keyindex[key]] = val
        else:
            self.keyindex[key] = len(self.values)
            self.values.append(val)
            # update prefix map
            for i in range(len(key)+1):
                self.prefix[key[:i]].add(self.keyindex[key])

    def sum(self, prefix: str) -> int:
        return sum(self.values[i] for i in self.prefix.get(prefix, []))


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["MapSum", "insert", "sum", "insert", "sum"],
     [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]],
     [None, None, 3, None, 5]),
    (["MapSum","insert","sum","insert","sum"],
     [[],["apple",3],["apple"],["app",2],["ap"]],
     [None,None,3,None,5])
])
def test(commands, arguments, expecteds):
    obj = globals()[commands[0]](*arguments[0])
    for cmd, args, exp in zip(commands[1:], arguments[1:], expecteds[1:]):
        assert exp == getattr(obj, cmd)(*args)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))

