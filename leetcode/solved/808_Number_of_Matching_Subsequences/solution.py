#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input:
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".

Note:

	All words in words and S will only consists of lowercase letters.
	The length of S will be in the range of [1, 50000].
	The length of words will be in the range of [1, 5000].
	The length of words[i] will be in the range of [1, 50].
"""
from pprint import pprint
import sys
from collections import Counter
from collections import deque
import queue
from typing import List
import pytest


def kmp(s, patterns):
    def build_lsp(p):
        ret = [0]
        i = 0
        for c in p[1:]:
            if c == p[i]:
                i += 1
                ret.append(i)
            else:
                while i > 0 and p[i] != c:
                    i = ret[i-1]
                if p[i] == c:
                    i += 1
                ret.append(i)
        return ret

    lsps = [build_lsp(p) for p in patterns]
    idxs = [0]*len(patterns)
    for c in s:
        for i in range(len(patterns)):
            if idxs[i] == len(patterns[i]):
                continue
            if patterns[i][idxs[i]] == c:
                idxs[i] += 1
            else:
                while idxs[i] > 0 and patterns[i][idxs[i]] != c:
                    idxs[i] = lsps[i][idxs[i]-1]
                if patterns[i][idxs[i]] == c:
                    idxs[i] += 1
    return [len(patterns[i]) == idxs[i] for i in range(len(patterns))]


def merge(d1, d2):
    for k, v in d2.items():
        if k not in d1:
            d1[k] = v
        else:
            if k == '__END__':
                d1[k] += v
            else:
                merge(d1[k], v)


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
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


    def __numMatchingSubseq(self, S: str, words: List[str]) -> int:
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

    def _numMatchingSubseq(self, S: str, words: List[str]) -> int:
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




@pytest.mark.parametrize('S, words, expected', [
    ("abcde", ["a", "bb", "acd", "ace"], 3)
])
def test(S, words, expected):
    assert expected == Solution().numMatchingSubseq(S, words)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
