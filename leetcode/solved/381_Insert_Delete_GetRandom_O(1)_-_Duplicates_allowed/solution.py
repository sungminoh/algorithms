#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design a data structure that supports all following operations in average O(1) time.
Note: Duplicate elements are allowed.

insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.

Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
"""
import sys
import random
from collections import defaultdict
import pytest


class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []
        self.d = defaultdict(set)


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.d[val].add(len(self.l))
        self.l.append(val)
        return len(self.d[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if len(self.d[val]) == 0:
            return False
        i = self.d[val].pop()
        if i != len(self.l)-1:
            self.l[i], self.l[-1] = self.l[-1], self.l[i]
            self.d[self.l[i]].remove(len(self.l)-1)
            self.d[self.l[i]].add(i)
        self.l.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.l)


class _RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pool = set()
        self.d = defaultdict(list)


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        i = self.d[val][-1]+1 if len(self.d[val]) > 0 else 0
        self.d[val].append(i)
        self.pool.add((val, i))
        return len(self.d[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if len(self.d[val]) == 0:
            return False
        self.pool.remove((val, self.d[val].pop()))
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.sample(self.pool, 1)[0][0]


@pytest.mark.parametrize('commands, args', [
    (['RandomizedCollection', 'insert', 'insert', 'insert', 'getRandom', 'remove', 'getRandom'],
     [[],[1],[1],[2],[],[1],[]]),
    (["RandomizedCollection","insert","insert","remove","insert","remove","getRandom"],
     [[],[0],[1],[0],[2],[1],[]]),
    (["RandomizedCollection","insert","insert","insert","insert","insert","remove","remove","remove","remove"],
     [[],[4],[3],[4],[2],[4],[4],[3],[4],[4]]),
])
def test(commands, args):
    inserted = defaultdict(int)
    count = 0
    o = RandomizedCollection()
    for c, a in zip(commands[1:], args[1:]):
        if c == 'insert':
            if inserted[a[0]] == 0:
                assert o.insert(*a)
            else:
                assert False == o.insert(*a)
            inserted[a[0]] += 1
            count += 1
        elif c == 'remove':
            if inserted[a[0]] == 0:
                assert False == o.remove(*a)
            else:
                assert o.remove(*a)
            inserted[a[0]] -= 1
            count -= 1
        elif c == 'getRandom':
            actual = defaultdict(int)
            for _ in range(100 * count):
                actual[o.getRandom()] += 1
            for val, cnt in actual.items():
                assert 95 * inserted[val] <= cnt <= 105 * inserted[val]


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))

