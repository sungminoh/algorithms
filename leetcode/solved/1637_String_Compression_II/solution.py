import math
from functools import lru_cache
from typing import Tuple
from typing import Optional

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


    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """Jan 27, 2024 17:50"""
        def encode(s):
            ret = []
            i = 0
            while i < len(s):
                cnt = 0
                j = i
                while j < len(s) and s[j] == s[i]:
                    cnt += 1
                    j += 1
                ret.append((s[i], cnt))
                i = j
            return ret

        def len_compressed(n):
            if n == 1:
                return 1
            return 1 + len(str(n))

        char_cnt = encode(s)
        length = 0
        for _, cnt in char_cnt:
            length += len_compressed(cnt)

        @lru_cache(None)
        def max_shorten(i, k, last_char=None, last_cnt=0):
            if i == len(char_cnt):
                return 0
            ret = 0
            cur_char, cur_cnt = char_cnt[i]
            # compress when the current char is the same as the last
            if last_char == cur_char:
                total_cnt = cur_cnt + last_cnt
                new_length = len_compressed(total_cnt)
                cur_length = len_compressed(cur_cnt)
                last_length = len_compressed(last_cnt)
                ret += (cur_length + last_length) - new_length
                cur_cnt = total_cnt
            # no deletion
            ret += max_shorten(i+1, k, cur_char, cur_cnt)
            # delete all the current chars
            if last_char != cur_char:
                if k >= cur_cnt:
                    ret = max(ret, len_compressed(cur_cnt) + max_shorten(i+1, k-cur_cnt, last_char, last_cnt))
                # delete except 1
                if cur_cnt > 1 and k >= cur_cnt-1:
                    ret = max(ret, len_compressed(cur_cnt)-1 + max_shorten(i+1, k-(cur_cnt-1), cur_char, 1))
            # delete to reduce the number of digits
            if cur_cnt >= 10:
                num_digits = len(str(cur_cnt))
                for m in range(num_digits-1, 0, -1):
                    to_delete = cur_cnt - (10**m - 1)
                    if k >= to_delete:
                        ret = max(ret, num_digits-m + max_shorten(i+1, k-to_delete, cur_char, cur_cnt-to_delete))

            return ret

        return length - max_shorten(0, k)


@pytest.mark.parametrize('args', [
    (("aaabcccd", 2, 4)),
    (("aabbaa", 2, 2)),
    (("aaaaaaaaaaa", 0, 3)),
    (("aabaabbcbbbaccc", 6, 4)),
    (("abbbbbbbbbba", 2, 3)),
    (("bbabbbabbbbcbb", 4, 3)),
    (("caacdcadc", 7, 2)),
    (("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 10, 3)),
    (("bbabbbabbbbcbb", 4, 3)),
    (("bbabbabbbcbbb", 4, 2)),
    (("bbabbbbbbbb", 2, 2)),
    (("abcdefghijklmnopqrstuvwxyz", 16, 10)),
    (("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 99, 1)),
])
def test(args):
    assert args[-1] == Solution().getLengthOfOptimalCompression(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
