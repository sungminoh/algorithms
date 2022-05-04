#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

	MyHashMap() initializes the object with an empty map.
	void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
	int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
	void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

Constraints:

	0 <= key, value <= 106
	At most 104 calls will be made to put, get, and remove.
"""
import json
from pathlib import Path
import sys
import pytest


class MyHashMap:
    def __init__(self, n=100):
        self.n = n
        self.store = self.get_basestore()

    def get_basestore(self):
        return [None] * (self.n + 1)

    def put(self, key: int, value: int) -> None:
        store = self.store
        while key:
            key, i = divmod(key, self.n)
            if store[i] is None:
                store[i] = self.get_basestore()
            store = store[i]
        store[-1] = value

    def get(self, key: int) -> int:
        store = self.store
        while key:
            key, i = divmod(key, self.n)
            if store[i] is None:
                return -1
            store = store[i]
        return -1 if store[-1] is None else store[-1]

    def remove(self, key: int) -> None:
        stack = []
        store = self.store
        while key:
            key, i = divmod(key, self.n)
            if store[i] is None:
                return
            store = store[i]
            stack.append((store, i))
        store[-1] = None

        while stack:
            store, i = stack.pop()
            if stack and all(x is None for x in store):
                stack[-1][0][i] = None
            else:
                return


class _MyHashMap:
    def __init__(self):
        self.d = {}

    def put(self, key, value):
        self.d[key] = value

    def get(self, key):
        return self.d.get(key, -1)

    def remove(self, key):
        if key in self.d:
            self.d.pop(key)


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"],
     [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2],],
     [None, None, None, 1, -1, None, 1, None, -1]),
    json.load(open(Path(__file__).parent/'testcase.json')),
    json.load(open(Path(__file__).parent/'testcase2.json')),
    json.load(open(Path(__file__).parent/'testcase3.json')),
])
def test(commands, arguments, expecteds):
    obj = globals()[commands.pop(0)](*arguments.pop(0))
    expecteds.pop(0)
    actual = []
    for cmd, arg in zip(commands, arguments):
        actual.append(getattr(obj, cmd)(*arg))
    assert expecteds == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
