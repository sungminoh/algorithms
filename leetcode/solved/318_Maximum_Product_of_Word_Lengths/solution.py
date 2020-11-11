#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
"""
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        binary_map = {c: pow(2, i) for i, c in enumerate('abcdefghijklmnopqrstuvwxyz')}
        rep_length = {}
        for w in words:
            rep = sum(binary_map[c] for c in set(w))
            rep_length[rep] = max(rep_length.get(rep, 0), len(w))
        m = 0
        keys = list(rep_length.keys())
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                if keys[i] & keys[j] == 0:
                    length_mul = rep_length[keys[i]] * rep_length[keys[j]]
                    if length_mul > m:
                        m = length_mul
        return m


if __name__ == '__main__':
    cases = [
        (["abcw","baz","foo","bar","xtfn","abcdef"], 16),
        (["a","ab","abc","d","cd","bcd","abcd"], 4),
        (["a","aa","aaa","aaaa"], 0)
    ]
    for case, expected in cases:
        actual = Solution().maxProduct(case)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
