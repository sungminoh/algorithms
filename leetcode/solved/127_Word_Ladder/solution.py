#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""


class Solution(object):
    def are_transformable(self, a, b):
        return sum(x != y for x, y in zip(a, b)) == 1

    def build_list(self, s, e, words):
        words = [s, *words, e]
        mat = [[] for _ in words]
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if self.are_transformable(words[i], words[j]):
                    mat[i].append(j)
                    mat[j].append(i)
        return mat

    def bfs(self, mat):
        from collections import deque
        visited = [False] * len(mat)
        stack = deque([(0, 1)])
        visited[0] = True
        while stack:
            i, d = stack.popleft()
            for j in mat[i]:
                if not visited[j]:
                    if j == len(mat)-1:
                        return d+1
                    stack.append((j, d+1))
                    visited[j] = True
        return 0

    def bfs_raw(self, begin, end, words):
        from collections import deque
        possibles = [set(x) for x in zip(*words, begin, end)]
        words = set([*words, end])
        queue = deque([(1, begin)])
        def gen_words(w):
            for i in range(len(w)):
                for c in possibles[i]:
                    ret = w[:i] + c + w[i+1:]
                    if ret in words:
                        yield ret

        while queue:
            d, word = queue.popleft()
            for w in gen_words(word):
                if w == end:
                    return d+1
                queue.append((d+1, w))
                words.remove(w)
        return 0

    def bfs_set(self, begin, end, words):
        possibles = [set(x) for x in zip(*words, begin)]
        words = {*words}
        words.discard(begin)
        def gen_words(w):
            for i in range(len(w)):
                for c in possibles[i]:
                    ret = w[:i] + c + w[i+1:]
                    yield ret

        begin_set = {begin}
        end_set = {end}
        d = 1
        while begin_set:
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
            new_set = set()
            for b in begin_set:
                for w in gen_words(b):
                    if w in end_set:
                        return d+1
                    if w in words:
                        new_set.add(w)
                        words.remove(w)
            begin_set = new_set
            d += 1
        return 0

    def dijkstra(self, mat):
        from heapq import heappop, heappush, heapify
        dist = [float('inf')] * len(mat)
        h = [(1, 0)]
        heapify(h)
        while h:
            d, i = heappop(h)
            row = mat[i]
            for j in row:
                new_d = d + 1
                if new_d < dist[j]:
                    if j == len(mat)-1:
                        return new_d
                    dist[j] = new_d
                    heappush(h, (new_d, j))
        return 0

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        return self.bfs_set(beginWord, endWord, wordList)


def main():
    s = input()
    e = input()
    words = input().split()
    print(Solution().ladderLength(s, e, words))


if __name__ == '__main__':
    main()
