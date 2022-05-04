#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

	void add(key) Inserts the value key into the HashSet.
	bool contains(key) Returns whether the value key exists in the HashSet or not.
	void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)

Constraints:

	0 <= key <= 106
	At most 104 calls will be made to add, remove, and contains.
"""
import sys
import pytest


class MyHashSet:
    def __init__(self, n=100):
        self.n = n
        self.store = self.get_basestore()

    def get_basestore(self):
        return [None] * (self.n + 1)

    def add(self, key: int) -> None:
        store = self.store
        while key:
            key, i = divmod(key, self.n)
            if store[i] is None:
                store[i] = self.get_basestore()
            store = store[i]
        store[-1] = True

    def remove(self, key: int) -> None:
        stack = []
        store = self.store
        while key:
            key, i = divmod(key, self.n)
            store = store[i]
            if store is None:
                return
            stack.append((store, i))
        store[-1] = None
        while stack:
            store, i = stack.pop()
            if stack and all(x is None for x in store):
                stack[-1][0][i] = None
            else:
                return

    def contains(self, key: int) -> bool:
        store = self.store
        while key:
            key, i = divmod(key, self.n)
            if store[i] is None:
                return False
            store = store[i]
        return store[-1] is True


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"],
     [[], [1], [2], [1], [3], [2], [2], [2], [2]],
     [None, None, None, True, False, None, True, None, False]),
])
def test(commands, arguments, expecteds):
    obj = globals()[commands.pop(0)](*arguments.pop(0))
    actual = [None]
    for cmd, arg in zip(commands, arguments):
        actual.append(getattr(obj, cmd)(*arg))
    assert expecteds == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
