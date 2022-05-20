#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"

Constraints:

	1 <= s.length <= 105
	2 <= k <= 104
	s only contains lower case English letters.
"""
from typing import List
import sys
import pytest


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """05/05/2021 09:41
        Time complexity: O(n)
        Space complexity: O(n)
        """
        stack: List[List[str, int]] = []  # the number of consecutive same char
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            while stack and stack[-1][1] == k:
                stack.pop()
        return ''.join([c*n for c, n in stack])

    def removeDuplicates(self, s: str, k: int) -> str:
        """05/20/2022 14:27"""
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack and stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c*n for c, n in stack)


@pytest.mark.parametrize('s, k, expected', [
    ("abcd", 2, "abcd"),
    ("deeedbbcccbdaa", 3, "aa"),
    ("pbbcggttciiippooaais", 2, "ps"),
])
def test(s, k, expected):
    assert expected == Solution().removeDuplicates(s, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
