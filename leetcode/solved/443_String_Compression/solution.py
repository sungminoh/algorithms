#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

	If the group's length is 1, append the character to s.
	Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

Constraints:

	1 <= chars.length <= 2000
	chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""
from typing import List
import pytest
import sys


class Solution:
    def compress(self, chars: List[str]) -> int:
        """Nov 19, 2020 23:53"""
        def count(i, backward=False):
            c = chars[i]
            cnt = 0
            while 0 <= i < len(chars) and chars[i] == c:
                cnt += 1
                i += 1 if not backward else -1
            return i, cnt

        def fill(i, j):
            nj, cnt = count(j)
            l = (int(math.log(cnt, 10)) + 1) if cnt > 1 else 0
            ni = i + 1 + l
            if ni <= nj:
                chars[i] = chars[j]
                if cnt != 1:
                    while cnt:
                        chars[i+l] = str(cnt % 10)
                        cnt //= 10
                        l -= 1
            else:
                while nj < ni < len(chars):
                    nj, cnt = count(nj)
                    l = (int(math.log(cnt, 10)) + 1) if cnt > 1 else 0
                    ni = ni + 1 + l
                a = ni-1
                b = nj-1
                while b >= j:
                    c = chars[b]
                    b, cnt = count(b, backward=True)
                    if cnt != 1:
                        while cnt:
                            chars[a] = str(cnt % 10)
                            cnt //= 10
                            a -= 1
                    chars[a] = c
                    a -= 1
            if nj >= len(chars):
                return ni
            return fill(ni, nj)

        return fill(0, 0)


    def compress(self, chars: List[str]) -> int:
        """Apr 02, 2023 19:58"""
        ret = ''
        p = 0
        cur = chars[0]
        cnt = 1
        for i in range(1, len(chars)):
            c = chars[i]
            if c != cur:
                chars[p] = cur
                p += 1
                if cnt > 1:
                    for k in str(cnt):
                        chars[p] = k
                        p += 1
                cur = c
                cnt = 0
            cnt += 1
        chars[p] = cur
        p += 1
        if cnt > 1:
            for k in str(cnt):
                chars[p] = k
                p += 1
        return p


@pytest.mark.parametrize('args', [
    ((["a","a","b","b","c","c","c"], 6)),
    ((["a"], 1)),
    ((["a","b","b","b","b","b","b","b","b","b","b","b","b"], 4)),
    (["a","a","a","b","b","a","a"], 6),
])
def test(args):
    assert args[-1] == Solution().compress(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
