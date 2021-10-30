#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Implement the RandomizedSet class:

	RandomizedSet() Initializes the RandomizedSet object.
	bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
	bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
	int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

Constraints:

	-231 <= val <= 231 - 1
	At most 2 * 105 calls will be made to insert, remove, and getRandom.
	There will be at least one element in the data structure when getRandom is called.
"""
import sys
import random
import pytest


class RandomizedSet:
    """04/15/2020 21:48"""
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dic:
            self.dic[val] = len(self.lst)
            self.lst.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dic:
            i = self.dic[val]
            if i != len(self.lst) - 1:
                self.lst[i], self.lst[-1] = self.lst[-1], self.lst[i]
                self.dic[self.lst[i]] = i
            self.lst.pop()
            self.dic.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.lst)


class RandomizedSet:
    def __init__(self):
        self.lst = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.dic[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        i = self.dic.pop(val)
        if i != len(self.lst)-1:
            self.lst[i] = self.lst[-1]
            self.dic[self.lst[-1]] = i
        self.lst.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],
     [[], [1], [2], [2], [], [1], [2], []],
     [None, True, False, True, 2, True, False, 2]),
    (["RandomizedSet","remove","remove","insert","getRandom","remove","insert"],
     [[],[0],[0],[0],[],[0],[0]],
     [None,False,False,True,0,True,True]
     )
])
def test(commands, arguments, expecteds):
    o = globals()[commands.pop(0)](*arguments.pop(0))
    expecteds.pop(0)
    for cmd, args, expected in zip(commands, arguments, expecteds):
        if cmd == 'getRandom':
            continue
        print(cmd, args, expected)
        assert expected == getattr(o, cmd)(*args)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
