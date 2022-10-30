#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting at most k characters.

Example 1:

Input: s = "aaabcccd", k = 2
Output: 4
Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.

Example 2:

Input: s = "aabbaa", k = 2
Output: 2
Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.

Example 3:

Input: s = "aaaaaaaaaaa", k = 0
Output: 3
Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.

Constraints:

	1 <= s.length <= 100
	0 <= k <= s.length
	s contains only lowercase English letters.
"""
from functools import lru_cache
import math
import itertools
import pytest
import sys


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """10/29/2022 17:52"""
        def compress(s):
            ret = []
            for c in s:
                if ret and ret[-1][0] == c:
                    ret[-1][1] += 1
                else:
                    ret.append([c, 1])
            return ret

        code = compress(s)
        acc = list(itertools.accumulate(
            code, func=lambda x, y: x+y[1], initial=0))

        def codelen(cnt):
            if cnt <= 1:
                return cnt
            return int(math.log10(cnt))+2

        @lru_cache(None)
        def dfs(i, last_char, last_char_cnt, n_delete):
            if i == len(code) or n_delete >= acc[-1] - acc[i]:
                return 0

            char, cnt  = code[i]
            ret = 0
            if char == last_char:
                ret -= codelen(last_char_cnt)
                cnt += last_char_cnt
            # no delete
            ret += codelen(cnt) + dfs(i+1, char, cnt, n_delete)

            to_deletes = []
            p = pow(10, int(math.log10(cnt)))
            while p > 0 and cnt-p+1<= n_delete:
                to_delete = cnt-p+1
                if char == last_char and  to_delete == cnt:
                    # When the current char is the same as the last one
                    # We don't need to consider remove all the same
                    # consecutive chars since it is considered from i-1
                    p //= 10
                    continue
                p //= 10
                to_deletes.append(to_delete)
            if cnt-1 <= n_delete:
                to_deletes.append(cnt-1)
            for to_delete in to_deletes:
                sub = 0
                if char == last_char:
                    sub -= codelen(last_char_cnt)
                sub += codelen(cnt - to_delete) + dfs(
                    i+1,
                    char if to_delete < cnt else last_char,
                    cnt - to_delete if to_delete < cnt else last_char_cnt,
                    n_delete - to_delete,
                )
                ret = min(ret, sub)
                p //= 10
            return ret

        return dfs(0, None, 0, k)


@pytest.mark.parametrize('s, k, expected', [
    ("aaabcccd", 2, 4),
    ("aabbaa", 2, 2),
    ("aaaaaaaaaaa", 0, 3),
    ("bbabbbabbbbcbb", 4, 3),
    ("bbabbabbbcbbb", 4, 2),
    ("bbabbbbbbbb", 2, 2),
    ("abcdefghijklmnopqrstuvwxyz", 16, 10),
    ("caacdcadc", 7, 2),
    ("abbbbbbbbbba", 2, 3),
    ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 99, 1),
])
def test(s, k, expected):
    assert expected == Solution().getLengthOfOptimalCompression(s, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
