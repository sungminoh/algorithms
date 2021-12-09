#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string of a given array of strings words.

For example, if words = ["abc", "xyz"] and the stream added the four characters (one by one) 'a', 'x', 'y', and 'z', your algorithm should detect that the suffix "xyz" of the characters "axyz" matches "xyz" from words.

Implement the StreamChecker class:

	StreamChecker(String[] words) Initializes the object with the strings array words.
	boolean query(char letter) Accepts a new character from the stream and returns true if any non-empty suffix from the stream forms a word that is in words.

Example 1:

Input
["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"]
[[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]
Output
[null, false, false, false, true, false, true, false, false, false, false, false, true]

Explanation
StreamChecker streamChecker = new StreamChecker(["cd", "f", "kl"]);
streamChecker.query("a"); // return False
streamChecker.query("b"); // return False
streamChecker.query("c"); // return False
streamChecker.query("d"); // return True, because 'cd' is in the wordlist
streamChecker.query("e"); // return False
streamChecker.query("f"); // return True, because 'f' is in the wordlist
streamChecker.query("g"); // return False
streamChecker.query("h"); // return False
streamChecker.query("i"); // return False
streamChecker.query("j"); // return False
streamChecker.query("k"); // return False
streamChecker.query("l"); // return True, because 'kl' is in the wordlist

Constraints:

	1 <= words.length <= 2000
	1 <= words[i].length <= 2000
	words[i] consists of lowercase English letters.
	letter is a lowercase English letter.
	At most 4 * 104 calls will be made to query.
"""
import sys
from typing import List
from collections import defaultdict
import pytest


class StreamChecker:
    def __init__(self, words: List[str]):
        def infdict():
            return defaultdict(infdict)

        self.trie = infdict()

        for word in words:
            t = self.trie
            for w in word:
                t = t[w]
            t[None] = None

        self.candidates = []

    def query(self, letter: str) -> bool:
        ret = False
        new_candidate = []
        for t in self.candidates + [self.trie]:
            if letter in t:
                t = t[letter]
                if None in t:
                    ret = True
                new_candidate.append(t)
        self.candidates = new_candidate
        return ret


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"],
     [[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]],
     [None, False, False, False, True, False, True, False, False, False, False, False, True])
])
def test(commands, arguments, expecteds):
    obj = globals()[commands.pop(0)](*arguments.pop(0))
    expecteds.pop(0)
    for cmd, args, exp in zip(commands, arguments, expecteds):
        assert exp == getattr(obj, cmd)(*args)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
