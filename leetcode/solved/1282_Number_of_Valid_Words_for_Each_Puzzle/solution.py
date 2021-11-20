#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:

	word contains the first letter of puzzle.
	For each letter in word, that letter is in puzzle.

		For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage", while
		invalid words are "beefed" (does not include 'a') and "based" (includes 's' which is not in the puzzle).

Return an array answer, where answer[i] is the number of words in the given word list words that is valid with respect to the puzzle puzzles[i].

Example 1:

Input: words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
Output: [1,1,3,2,4,0]
Explanation:
1 valid word for "aboveyz" : "aaaa"
1 valid word for "abrodyz" : "aaaa"
3 valid words for "abslute" : "aaaa", "asas", "able"
2 valid words for "absoryz" : "aaaa", "asas"
4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
There are no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.

Example 2:

Input: words = ["apple","pleas","please"], puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]
Output: [0,1,3,2,0]

Constraints:

	1 <= words.length <= 105
	4 <= words[i].length <= 50
	1 <= puzzles.length <= 104
	puzzles[i].length == 7
	words[i] and puzzles[i] consist of lowercase English letters.
	Each puzzles[i] does not contain repeated characters.
"""
from collections import Counter
from collections import defaultdict
import json
from pathlib import Path
import sys
from typing import List
import pytest


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """TLE"""
        def encode(w: str) -> int:
            ret = 0
            for c in set(w):
                ret |= 1 << (ord(c)-97)
            return ret

        encoded_words = [encode(w) for w in words]
        encoded_puzzles = [encode(p) for p in puzzles]

        ret = [0] * len(puzzles)
        for i, (p, ep) in enumerate(zip(puzzles, encoded_puzzles)):
            cnt = 0
            for ew in encoded_words:
                if ew & encode(p[0]) != 0 and ew - (ew & ep) == 0:
                    cnt += 1
            ret[i] = cnt

        return ret

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """TLE"""
        def encode(w: str) -> int:
            ret = 0
            for c in set(w):
                ret |= 1 << (ord(c)-97)
            return ret

        words_with_letter = defaultdict(set)
        encoded_words = [0]*len(words)
        for i, w in enumerate(words):
            ew = 0
            for c in w:
                d = ord(c)-97
                ew |= 1 << d
                words_with_letter[c].add(i)
            encoded_words[i] = ew

        for c in words_with_letter:
            print(c, len(words_with_letter[c]))

        ret = [0] * len(puzzles)
        for i, p in enumerate(puzzles):
            if p[0] in words_with_letter:
                ep = encode(p)
                cnt = 0
                for j in words_with_letter[p[0]]:
                    ew = encoded_words[j]
                    if ew - (ew&ep) == 0:
                        cnt += 1
                ret[i] = cnt

        return ret

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """
        Time complexity: O(W*w + P*2^6) where W = len(words), w = len(word), P = len(puzzles)
        Space complexity: O(W + P)
        """
        def encode(w: str) -> int:
            ret = 0
            for c in set(w):
                ret |= 1 << (ord(c)-97)
            return ret

        cnt = Counter()
        for w in words:
            cnt[encode(w)] += 1

        ret = [0] * len(puzzles)
        for i, p in enumerate(puzzles):
            req = 1<<(ord(p[0])-97)
            mask = encode(p[1:])
            sub = mask
            while sub:
                ret[i] += cnt[sub|req]
                sub = (sub-1) & mask
            ret[i] += cnt[req]

        return ret


@pytest.mark.parametrize('words, puzzles, expected', [
    (["aaaa","asas","able","ability","actt","actor","access"], ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"], [1,1,3,2,4,0]),
    (["apple","pleas","please"], ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"], [0,1,3,2,0]),
    (*json.load(open(Path(__file__).parent/'testcase.json')), [])
])
def test(words, puzzles, expected):
    assert expected == Solution().findNumOfValidWords(words, puzzles)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
