#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        """
          _ h o r s e
        _ 0 1 2 3 4 5
        o 1 1 1 2 3 4
        r 2 2 2 1 2 3
        s 3 3 2 2 1 2

        """
        if not word1 or not word2:
            return max(len(word1), len(word2))
        memo = [j+1 for j in range(len(word2))]
        for i in range(len(word1)):
            new_memo = []
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    new_memo.append(memo[j-1] if j != 0 else i)
                else:
                    new_memo.append(1 + min(new_memo[-1] if j != 0 else i+1,
                                            memo[j-1] if j != 0 else i,
                                            memo[j]))
            memo = new_memo
        return memo[-1]


def main():
    word1 = input()
    word2 = input()
    print(Solution().minDistance(word1, word2))


if __name__ == '__main__':
    main()
