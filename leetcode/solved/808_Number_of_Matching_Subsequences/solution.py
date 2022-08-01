#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

	For example, "ace" is a subsequence of "abcde".

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2

Constraints:

	1 <= s.length <= 5 * 104
	1 <= words.length <= 5000
	1 <= words[i].length <= 50
	s and words[i] consist of only lowercase English letters.
"""
from pathlib import Path
import json
from functools import lru_cache
from pygments.lexer import words
import sys
import bisect
from collections import Counter
from collections import deque
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        """09/14/2020 01:50	"""
        qs = [[] for _ in range(26)]
        for word in words:
            qs[ord(word[0])-97].append(word)
        cnt = 0
        for c in S:
            q = qs[ord(c)-97]
            qs[ord(c)-97] = []
            for w in q:
                if len(w) == 1:
                    cnt += 1
                else:
                    qs[ord(w[1])-97].append(w[1:])
        return cnt

    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        """09/14/2020 01:38"""
        def merge(d1, d2):
            for k, v in d2.items():
                if k not in d1:
                    d1[k] = v
                else:
                    if k == '__END__':
                        d1[k] += v
                    else:
                        merge(d1[k], v)

        # build trie
        trie = dict()
        for word in words:
            d = trie
            for c in word:
                d.setdefault(c, dict())
                d = d[c]
            d.setdefault('__END__', 0)
            d['__END__'] += 1
        cnt = 0
        cur = trie
        for c in S:
            nxt = dict()
            for k in cur:
                if c  == k:
                    merge(nxt, cur[c])
                else:
                    merge(nxt, {k: cur[k]})
            cur = nxt
        cnt += cur.get('__END__', 0)
        return cnt

    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        """09/12/2020 17:05"""
        counter = Counter(words)
        keys = list(counter.keys())
        idx = set(range(len(counter)))
        qs = [deque(word) for word in keys]
        cnt = 0
        for c in S:
            for i in list(idx):
                q = qs[i]
                if q[0] == c:
                    q.popleft()
                    if len(q) == 0:
                        idx.remove(i)
                        cnt += counter[keys[i]]

        return cnt

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        """TLE"""
        @lru_cache(None)
        def is_sub(a, b):
            if not b or a == b: return True
            if len(a) < len(b): return False
            i = a.find(b[0])
            if i < 0:
                return False
            return is_sub(a[i+1:], b[1:])

        return sum(1 for w in words if is_sub(s, w))

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        """
        Greedily find all mathcing word
        Time complexity: O(len(s) * len(words))
        Space complexity: O(len(words))
        """
        d = defaultdict(list)
        for w in words:
            d[w[0]].append((0, w))
        cnt = 0
        for c in s:
            if c in d:
                for i, w in d.pop(c):
                    if i == len(w)-1:
                        cnt += 1
                    else:
                        d[w[i+1]].append((i+1, w))
        return cnt

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        """
        07/31/2022 23:26
        07/31/2022 23:35
        Time complexity: O(len(words) * len(word) * log(len(s))) + O(len(s))
        Space complexity: O(len(s))
        """
        indexes = defaultdict(list)
        for i, c in enumerate(s):
            indexes[c].append(i)

        def bisearch(arr, x):
            i, j = 0, len(arr)-1
            while i <= j:
                m = i + ((j-i)//2)
                if arr[m] < x:
                    i = m+1
                else:
                    j = m-1
            return i

        def is_subsequence(word):
            i = -1
            for c in word:
                idxs = indexes.get(c, [])
                j = bisearch(idxs, i+1)
                #j = bisect.bisect_left(idxs, i+1)
                if j == len(idxs):
                    return False
                i = idxs[j]
            return True

        ret = 0
        for word in words:
            if is_subsequence(word):
                ret += 1
        return ret


@pytest.mark.parametrize('s, words, expected', [
    ("abcde", ["a","bb","acd","ace"], 3),
    ("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"], 2),
    ("qlhxagxdqh", ["qlhxagxdq","qlhxagxdq","lhyiftwtut","yfzwraahab"], 2),
    (*json.load(open(Path(__file__).parent/'testcase.json')), 1000)
])
def test(s, words, expected):
    assert expected == Solution().numMatchingSubseq(s, words)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
