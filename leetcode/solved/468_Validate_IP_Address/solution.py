
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note:
You may assume there is no extra space or special characters in the input string.

Example 1:

Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:

Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:

Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.
"""
import sys
import pytest


numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
allowed_chars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                 'a', 'b', 'c', 'd', 'e', 'f',
                 'A', 'B', 'C', 'D', 'E', 'F',}


def is_ip4(s):
    chunks = s.split('.')
    if len(chunks) != 4:
        return False
    for chunk in chunks:
        if len(chunk) > 1 and chunk.startswith('0'):
            return False
        try:
            if chunk[0] not in numbers or not 0 <= int(chunk) <= 255:
                return False
        except:
            return False
    return True


def is_ip6(s):
    chunks = s.split(':')
    if len(chunks) != 8:
        return False
    for chunk in chunks:
        if len(chunk) > 4 or len(chunk) == 0:
            return False
        for c in chunk:
            if c not in allowed_chars:
                return False
    return True


class Solution:
    def validIPAddress(self, IP: str) -> str:
        if is_ip4(IP):
            return 'IPv4'
        elif is_ip6(IP):
            return 'IPv6'
        return 'Neither'


@pytest.mark.parametrize('IP, expected', [
    ("172.16.254.1", "IPv4"),
    ("2001:0db8:85a3:0:0:8A2E:0370:7334", "IPv6"),
    ("256.256.256.256", "Neither"),
    ("2001:db8:85a3:0:0:8A2E:0370:7334", "IPv6"),
    ("02001:0db8:85a3:0000:0000:8a2e:0370:7334", "Neither"),
    ("1e1.4.5.6", "Neither"),
    ("0.0.0.-0", "Neither")
])
def test(IP, expected):
    assert expected == Solution().validIPAddress(IP)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
