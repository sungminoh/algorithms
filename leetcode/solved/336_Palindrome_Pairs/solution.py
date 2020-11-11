#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]

Constraints:

	1 <= words.length <= 5000
	0 <= words[i] <= 300
	words[i] consists of lower-case English letters.
"""
from functools import lru_cache
import sys
from collections import defaultdict
from typing import List
import pytest


def infdict():
    return defaultdict(infdict)


def to_dict(d):
    return {k: to_dict(v) for k, v in d.items()} if isinstance(d, dict) else d


class Solution:
    def _palindromePairs(self, words: List[str]) -> List[List[int]]:
        @lru_cache(None)
        def is_palindrome(s):
            return s == s[::-1]

        def find_all(d, stack):
            for k, v in d.items():
                if k is not None:
                    yield from find_all(v, stack + [k])
                else:
                    if is_palindrome(''.join(stack)):
                        yield from v

        ret = []
        trie = infdict()
        for i, word in enumerate(words):
            d = trie
            for c in reversed(word):
                d = d[c]
            else:
                d.setdefault(None, [])
                d[None].append(i)
        # print(to_dict(trie))
        for i, word in enumerate(words):
            d = trie
            for _i, c in enumerate(word):
                if None in d:
                    if is_palindrome(word[_i:]):
                        for j in d[None]:
                            ret.append([i, j])
                if c not in d:
                    break
                d = d[c]
            else:
                for j in find_all(d, []):
                    if i != j:
                        ret.append([i, j])

        return ret


@pytest.mark.parametrize('words, expected', [
    (["abcd","dcba","lls","s","sssll"], [[0,1],[1,0],[3,2],[2,4]]),
    (["bat","tab","cat"], [[0,1],[1,0]]),
    (["bat","tab","cat", "aaa", ""], [[0,1],[1,0],[3,4],[4,3]]),
    (["a",""], [[0,1],[1,0]]),
    (["a","b","c","ab","ac","aa"], [[3,0],[1,3],[4,0],[2,4],[5,0],[0,5]])
])
def test(words, expected):
    print()
    actual = Solution().palindromePairs(words)
    print(sorted(expected))
    print(sorted(actual))
    assert sorted(expected) == sorted(actual)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
