#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array data representing the data, return whether it is a valid UTF-8 encoding (i.e. it translates to a sequence of valid UTF-8 encoded characters).

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

	For a 1-byte character, the first bit is a 0, followed by its Unicode code.
	For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0, followed by n - 1 bytes with the most significant 2 bits being 10.

This is how the UTF-8 encoding would work:

     Number of Bytes   |        UTF-8 Octet Sequence
                       |              (binary)
   --------------------+-----------------------------------------
            1          |   0xxxxxxx
            2          |   110xxxxx 10xxxxxx
            3          |   1110xxxx 10xxxxxx 10xxxxxx
            4          |   11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

x denotes a bit in the binary form of a byte that may be either 0 or 1.

Note: The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

Input: data = [197,130,1]
Output: true
Explanation: data represents the octet sequence: 11000101 10000010 00000001.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

Example 2:

Input: data = [235,140,4]
Output: false
Explanation: data represented the octet sequence: 11101011 10001100 00000100.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.

Constraints:

	1 <= data.length <= 2 * 104
	0 <= data[i] <= 255
"""
import pytest
import sys
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        """04/20/2020 06:37"""
        def _byte_size(i):
            for j in range(8):
                if 1 & (data[i] >> (7 - j)) != 1:
                    return j
            return 8

        def _rec(i):
            if i == len(data):
                return True
            byte_size = _byte_size(i)
            if byte_size == 0:
                return _rec(i + 1)
            if byte_size == 1 or byte_size > 4 or i + byte_size > len(data):
                return False
            for j in range(1, byte_size):
                if _byte_size(i + j) != 1:
                    return False
            return _rec(i + byte_size)

        return _rec(0)

    def validUtf8(self, data: List[int]) -> bool:
        """10/03/2022 21:32"""
        remain = 0
        print()
        for d in data:
            print(bin(d)[2:])
            if d == 255:
                return False
            if remain == 0:
                if d & (1<<7) == 0:
                    continue
                cnt = 0
                while (1<<(6-cnt)) & d != 0:
                    cnt += 1
                if cnt == 0 or cnt > 3:
                    return False
                remain = cnt
            else:
                cond1 = (d & (1<<7)) != 0
                cond2 = (d ^ (1<<6)) != 0
                if not (cond1 and cond2):
                    return False
                remain -= 1
        return remain == 0


@pytest.mark.parametrize('data, expected', [
    ([197,130,1], True),
    ([235,140,4], False),
    ([255], False),
    ([237], False),
    ([250,145,145,145,145], False),
])
def test(data, expected):
    assert expected == Solution().validUtf8(data)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
