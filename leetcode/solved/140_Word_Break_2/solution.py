#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

"""
from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def word_break(self, i):
        if i == len(self.s):
            return [[]]
        ret = []
        for j in range(i+1, len(self.s)+1):
            if self.s[i:j] in self.words:
                ret.extend([[self.s[i:j]] + l for l in self.word_break(j)])
        return ret

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.words = set(wordDict)
        self.s = s
        return [' '.join(x) for x in self.word_break(0)]


def main():
    # s = input()
    # wordDict = input().split()
    data = [
        ("catsanddog", ["cat", "cats", "and", "sand", "dog"]),
        ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"])
    ]
    for d in data:
        print(Solution().wordBreak(*d))


if __name__ == '__main__':
    main()
