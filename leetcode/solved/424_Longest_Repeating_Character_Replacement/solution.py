
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.

 

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""
import sys
import pytest
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        window = max_count = 0
        for j in range(len(s)):
            # replace all numbers that are not the number with max count.
            counter[s[j]] += 1
            max_count = max(max_count, counter[s[j]])
            if window - max_count < k:  # never shrink the window
                window += 1
            else:
                counter[s[j - window]] -= 1
        return window

    def _characterReplacement(self, s: str, k: int) -> int:
        positions = defaultdict(list)
        i = 0
        while i < len(s):
            c = s[i]
            start = i
            while i < len(s) and s[i] == c:
                i += 1
            end = i - 1
            positions[c].append([start, end])

        def get_max(pairs, k):
            buf = min(k, pairs[0][0] + (len(s) - 1 - pairs[0][1]))
            total_width = pairs[0][1] - pairs[0][0] + 1
            max_width = total_width + buf
            orig_k = k
            i, j = 0, 1
            while j < len(pairs):
                gap = pairs[j][0] - pairs[j - 1][1] - 1
                while gap > k:
                    prev_gap = pairs[i + 1][0] - pairs[i][1] - 1
                    total_width -= pairs[i][1] - pairs[i][0] + 1
                    k += prev_gap
                    i += 1
                total_width += pairs[j][1] - pairs[j][0] + 1
                k -= gap
                total_gap = orig_k - k
                buf = min(k, pairs[i][0] + (len(s) - 1 - pairs[j][1]))
                max_width = max(max_width, total_width + total_gap + buf)
                j += 1
            return max_width

        # print(positions)
        ret = 0
        for pairs in positions.values():
            ret = max(ret, get_max(pairs, k))
        return ret


@pytest.mark.parametrize('s, k, expected', [
    ('ABAB', 2, 4),
    ('AABABBA', 1, 4),
    ('AAAA', 2, 4),
    ("AABA", 0, 2),
    ("ABCDE", 1, 2),
    ("", 0, 0)
])
def test(s, k, expected):
    assert expected == Solution().characterReplacement(s, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
