#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design the CombinationIterator class:

	CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
	next() Returns the next combination of length combinationLength in lexicographical order.
	hasNext() Returns true if and only if there exists a next combination.

Example 1:

Input
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
Output
[null, "ab", true, "ac", true, "bc", false]

Explanation
CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next();    // return "ab"
itr.hasNext(); // return True
itr.next();    // return "ac"
itr.hasNext(); // return True
itr.next();    // return "bc"
itr.hasNext(); // return False

Constraints:

	1 <= combinationLength <= characters.length <= 15
	All the characters of characters are unique.
	At most 104 calls will be made to next and hasNext.
	It is guaranteed that all calls of the function next are valid.
"""
import sys
from collections import deque
import pytest


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        def gen_comb(s, l, i=0):
            if l == 0:
                yield ''
            else:
                for j in range(i, len(s)+1-l):
                    c = s[j]
                    for sub in gen_comb(s, l-1, j+1):
                        yield c+sub

        self.g = gen_comb(characters, combinationLength, 0)
        self.q = deque()

    def next(self) -> str:
        if self.q:
            return self.q.popleft()
        return next(self.g)

    def hasNext(self) -> bool:
        if self.q:
            return True
        n = next(self.g, None)
        if n is not None:
            self.q.append(n)
            return True
        return False


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"],
     [["abc", 2], [], [], [], [], [], []],
     [None, "ab", True, "ac", True, "bc", False])
])
def test(commands, arguments, expecteds):
    obj = globals()[commands.pop(0)](*arguments.pop(0))
    expecteds.pop(0)
    for cmd, arg, exp in zip(commands, arguments, expecteds):
        actual = getattr(obj, cmd)(*arg)
        print(cmd, arg, exp, actual)
        assert exp == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
