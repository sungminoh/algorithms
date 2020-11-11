
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""
import random
import pytest


class RandomizedSet:

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


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


@pytest.mark.parametrize('commands, args, expected', [
    (["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"],
     [[],[1],[2],[2],[],[1],[2],[]],
     [None,True,False,True,2,True,False,2]),
    (["RandomizedSet","insert","insert","remove","insert","remove","getRandom"],
     [[],[0],[1],[0],[2],[1],[]],
     [None,True,True,True,True,True,2])
])
def test(commands, args, expected):
    s = RandomizedSet()
    assert expected == [None] + [getattr(s, cmd)(*arg) if arg else getattr(s, cmd)() for cmd, arg in zip(commands[1:], args[1:])]

