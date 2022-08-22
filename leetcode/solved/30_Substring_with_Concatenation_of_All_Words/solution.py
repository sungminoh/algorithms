#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

	For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.

Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
The output order does not matter. Returning [9,0] is fine too.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: Since words.length == 4 and words[i].length == 4, the concatenated substring has to be of length 16.
There is no substring of length 16 is s that is equal to the concatenation of any permutation of words.
We return an empty array.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.

Constraints:

	1 <= s.length <= 104
	1 <= words.length <= 5000
	1 <= words[i].length <= 30
	s and words[i] consist of lowercase English letters.
"""
from heapq import heappush
from functools import lru_cache
from pathlib import Path
import json
import sys
from collections import Counter
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def findSubstring(self, s, words):
        """08/05/2018 04:55"""
        if not words:
            return []
        from collections import defaultdict
        counts = defaultdict(int)
        for w in words:
            counts[w] += 1

        ret = []
        word_length = len(words[0])
        for i in range(word_length):
            start = i
            cnt = 0
            visited = defaultdict(int)
            for j in range(i, len(s)-word_length+1, word_length):
                ss = s[j:j+word_length]
                if ss in counts:
                    cnt += 1
                    visited[ss] += 1
                    while visited[ss] > counts[ss]:
                        visited[s[start:start+word_length]] -= 1
                        cnt -= 1
                        start += word_length
                    if cnt == len(words):
                        ret.append(start)
                        visited[s[start:start+word_length]] -= 1
                        cnt -= 1
                        start += word_length
                else:
                    start = j + word_length
                    cnt = 0
                    visited.clear()
        return ret

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """08/21/2022 17:34
        Memory Limit Exceeded
        """
        def infdict():
            return defaultdict(infdict)

        # build words trie
        trie = infdict()
        for i, word in enumerate(words):
            t = trie
            for c in word:
                t = t[c]
            t[None][i] = None

        # get start indexes of occurrences of each word
        index_to_word = defaultdict(set)
        tries = [trie]
        for i, c in enumerate(s):
            new_tries = [trie]
            for t in tries:
                if c in t:
                    for wi in t[c][None].keys():
                        index_to_word[i-len(words[wi])+1].add(wi)
                    new_tries.append(t[c])
            tries = new_tries

        @lru_cache(None)
        def dfs(i, remains):
            if remains == 0:
                return True
            for wi in index_to_word.get(i, set()):
                if 1<<wi & remains:
                    if dfs(i+len(words[wi]), remains^(1<<wi)):
                        return True
            return False

        return [i for i in index_to_word.keys() if dfs(i, (1<<len(words))-1)]

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """maximum recursion depth exceeded"""
        def infdict():
            return defaultdict(infdict)

        length = sum(len(w) for w in words)
        word_cnt = Counter(words)
        words = list(word_cnt.keys())

        # build words trie
        trie = infdict()
        for i, word in enumerate(words):
            t = trie
            for c in word:
                t = t[c]
            t[None][i] = None

        # get start indexes of occurrences of each word
        index_to_word = defaultdict(set)
        tries = [trie]
        for i, c in enumerate(s):
            new_tries = [trie]
            for t in tries:
                if c in t:
                    for wi in t[c][None].keys():
                        index_to_word[i-len(words[wi])+1].add(wi)
                    new_tries.append(t[c])
            tries = new_tries

        def dfs(i):
            if not word_cnt:
                return True
            for wi in index_to_word.get(i, set()):
                word = words[wi]
                if word_cnt.get(word, 0) > 0:
                    word_cnt[word] -= 1
                    if word_cnt[word] == 0:
                        word_cnt.pop(word)
                    ret = dfs(i+len(words[wi]))
                    word_cnt[word] += 1
                    if ret:
                        return True
            return False

        return [i for i in index_to_word.keys() if len(s)-i >= length and dfs(i)]

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """08/21/2022 18:28
        Generic solution when lengths of words are not the same
        Time Complexity: O(s*logs*words + word*words)
        """
        def infdict():
            return defaultdict(infdict)

        length = sum(len(w) for w in words)
        word_cnt = Counter(words)
        words = list(word_cnt.keys())
        counts = [word_cnt[w] for w in words]

        # build words trie
        # Time Complexity: O(words*word)
        trie = infdict()
        for i, word in enumerate(words):
            t = trie
            for c in word:
                t = t[c]
            t[None][i] = None

        # get start indexes of occurrences of each word
        # Time Complexity: O(s*word)
        index_to_word = defaultdict(set)
        tries = [trie]
        for i, c in enumerate(s):
            new_tries = [trie]
            for t in tries:
                if c in t:
                    for wi in t[c][None].keys():
                        index_to_word[i-len(words[wi])+1].add(wi)
                    new_tries.append(t[c])
            tries = new_tries

        # iterate from the smallest possible index
        heap = []
        # Time Complexity: O(s*logs)
        for i, wis in index_to_word.items():
            if len(s)-i >= length:
                heappush(heap, (i, counts[:]))

        ret = []
        # Time Complexity: O(s*logs*words)
        while heap:
            i, cnt = heap.pop(0)
            if all(x==0 for x in cnt):
                ret.append(i - length)
            for wi in index_to_word.get(i, set()):
                if cnt[wi] > 0:
                    heappush(heap, (i + len(words[wi]), cnt[:wi] + [cnt[wi]-1] + cnt[wi+1:]))

        return ret


    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """08/21/2022 19:16
        Time Complexity: O((s-word*words)*word*words)
        """
        if not words or not words[0]:
            return list(range(len(s)))

        cnt = len(words)
        w = len(words[0])
        l = w*len(words)

        def find(i):
            ret = []
            j = i
            counter = Counter(words)
            while i+w <= len(s):
                cur = s[i:i+w]
                i += w
                while i-j > l:
                    counter[s[j:j+w]] += 1
                    j += w
                if cur in counter:
                    counter[cur] -= 1
                    if i-j == l and all(x == 0 for x in counter.values()):
                        ret.append(j)
                else:
                    counter = Counter(words)
                    j = i
                if len(s)-j < l:
                    break
            return ret

        ret = []
        for i in range(w):
            ret.extend(find(i))
        return ret


@pytest.mark.parametrize('s, words, expected', [
    ("barfoothefoobarman", ["foo","bar"], [0,9]),
    ("wordgoodgoodgoodbestword", ["word","good","best","word"], []),
    ("barfoofoobarthefoobarman", ["bar","foo","the"], [6,9,12]),
    (*json.load(open(Path(__file__).parent/'testcase.json')), [0]),
])
def test(s, words, expected):
    assert expected == Solution().findSubstring(s, words)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
