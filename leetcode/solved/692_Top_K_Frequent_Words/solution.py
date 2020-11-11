#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non-empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:

Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.

Follow up:

Try to solve it in O(n log k) time and O(n) extra space.
"""
import sys
from heapq import heappop
from heapq import heappush
from collections import defaultdict
from typing import List
import pytest


class Solution:
    class Word:
        def __init__(self, s):
            self.s = s

        def __gt__(self, o):
            return self.s < o.s

        def __lt__(self, o):
            return self.s > o.s


    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = defaultdict(int)
        for w in words:
            d[w] += 1
        h = []
        for w, c in d.items():
            heappush(h, (c, Solution.Word(w)))
            while len(h) > k:
                heappop(h)
        ret = []
        while h:
            _, w = heappop(h)
            ret.append(w.s)

        return ret[::-1]


@pytest.mark.parametrize('words, k, expected', [
    (["i", "love", "leetcode", "i", "love", "coding"], 2, ["i", "love"]),
    (["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4, ["the", "is", "sunny", "day"]),
])
def test(words, k, expected):
    assert expected == Solution().topKFrequent(words, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
