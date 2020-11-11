#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True
        if not wordDict:
            return False
        self.s = s
        self.wordDict = set(wordDict)
        self.lengths = {len(word) for word in wordDict}
        self.memo = [None] * len(s)
        return self.solve(0)

    def solve(self, i):
        s = self.s[i:]
        if not s:
            return True
        if self.memo[i] is not None:
            return self.memo[i]
        for j in self.lengths:
            if s[:j] in self.wordDict:
                sub_result = self.solve(i+j)
                if sub_result:
                    self.memo[i] = True
                    return True
        self.memo[i] = False
        return False


def main():
    s = input()
    wordDict = input().split()
    print(Solution().wordBreak(s, wordDict))


if __name__ == '__main__':
    main()
