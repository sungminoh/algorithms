#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

Constraints:

	1 <= words.length <= 500
	1 <= words[i].length <= 10
	words[i] consists of lowercase English letters.
	k is in the range [1, The number of unique words[i]]

Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
"""
from collections import defaultdict
from collections import Counter
from heapq import heappop, heappush
from typing import List
import pytest
import sys


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

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        def rev(word):
            return (*(-ord(c) for c in word), float('inf'))

        cnt = Counter(words)
        heap = []
        for w, c in cnt.items():
            heappush(heap, (c, rev(w), w))
            if len(heap) > k:
                # Pop min cnt, lexicographically later one
                heappop(heap)

        ret = []
        while heap:
            ret.append(heappop(heap)[2])

        return ret[::-1]


@pytest.mark.parametrize('words, k, expected', [
    (["i","love","leetcode","i","love","coding"], 2, ["i","love"]),
    (["the","day","is","sunny","the","the","the","sunny","is","is"], 4, ["the","is","sunny","day"]),
    (["a","aa","aaa"], 1, ['a']),
    (["plpaboutit","jnoqzdute","sfvkdqf","mjc","nkpllqzjzp","foqqenbey","ssnanizsav","nkpllqzjzp","sfvkdqf","isnjmy","pnqsz","hhqpvvt","fvvdtpnzx","jkqonvenhx","cyxwlef","hhqpvvt","fvvdtpnzx","plpaboutit","sfvkdqf","mjc","fvvdtpnzx","bwumsj","foqqenbey","isnjmy","nkpllqzjzp","hhqpvvt","foqqenbey","fvvdtpnzx","bwumsj","hhqpvvt","fvvdtpnzx","jkqonvenhx","jnoqzdute","foqqenbey","jnoqzdute","foqqenbey","hhqpvvt","ssnanizsav","mjc","foqqenbey","bwumsj","ssnanizsav","fvvdtpnzx","nkpllqzjzp","jkqonvenhx","hhqpvvt","mjc","isnjmy","bwumsj","pnqsz","hhqpvvt","nkpllqzjzp","jnoqzdute","pnqsz","nkpllqzjzp","jnoqzdute","foqqenbey","nkpllqzjzp","hhqpvvt","fvvdtpnzx","plpaboutit","jnoqzdute","sfvkdqf","fvvdtpnzx","jkqonvenhx","jnoqzdute","nkpllqzjzp","jnoqzdute","fvvdtpnzx","jkqonvenhx","hhqpvvt","isnjmy","jkqonvenhx","ssnanizsav","jnoqzdute","jkqonvenhx","fvvdtpnzx","hhqpvvt","bwumsj","nkpllqzjzp","bwumsj","jkqonvenhx","jnoqzdute","pnqsz","foqqenbey","sfvkdqf","sfvkdqf"], 1, ["fvvdtpnzx"]),
])
def test(words, k, expected):
    assert expected == Solution().topKFrequent(words, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
