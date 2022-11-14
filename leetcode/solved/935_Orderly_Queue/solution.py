#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a string s and an integer k. You can choose one of the first k letters of s and append it at the end of the string..

Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.

Example 1:

Input: s = "cba", k = 1
Output: "acb"
Explanation:
In the first move, we move the 1st character 'c' to the end, obtaining the string "bac".
In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".

Example 2:

Input: s = "baaca", k = 3
Output: "aaabc"
Explanation:
In the first move, we move the 1st character 'b' to the end, obtaining the string "aacab".
In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc".

Constraints:

	1 <= k <= s.length <= 1000
	s consist of lowercase English letters.
"""
import pytest
import sys


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        """09/22/2021 21:15"""
        if k == 0:
            return s
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        else:
            return ''.join(sorted(list(s)))

    def orderlyQueue(self, s: str, k: int) -> str:
        """11/13/2022 18:09"""
        if k > 2:
            return ''.join(sorted(s))
        ret = s
        for i in range(1,len(s)):
            ret = min(ret, s[i:] + s[:i])
        return ret


@pytest.mark.parametrize('s, k, expected', [
    ("cba", 1, "acb"),
    ("baaca", 3, "aaabc"),
    ("xmvzi", 2, "imvxz"),
])
def test(s, k, expected):
    assert expected == Solution().orderlyQueue(s, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
