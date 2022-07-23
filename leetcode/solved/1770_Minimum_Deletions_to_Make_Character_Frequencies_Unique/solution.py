#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.

Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

Constraints:

	1 <= s.length <= 105
	s contains only lowercase English letters.
"""
import sys
from collections import Counter
import pytest


class Solution:
    def minDeletions(self, s: str) -> int:
        cnts = sorted(Counter(s).values(), reverse=True)
        ret = 0
        for i in range(1, len(cnts)):
            if cnts[i-1] <= cnts[i]:
                to = max(0, cnts[i-1]-1)
                ret += cnts[i] - to
                cnts[i] = to
        return ret


@pytest.mark.parametrize('s, expected', [
    ("aab", 0),
    ("aaabbbcc", 2),
    ("ceabaacb", 2),
    ("bbcebab", 2),
])
def test(s, expected):
    assert expected == Solution().minDeletions(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
