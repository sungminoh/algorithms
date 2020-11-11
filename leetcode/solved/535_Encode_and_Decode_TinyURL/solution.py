
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Note: This is a companion problem to the System Design problem: Design TinyURL.

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
"""
import sys
from functools import lru_cache
import pytest


class Codec:
    prefix = 'http://tinyurl.com/'
    allowed_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_.~/:'
    storage = []

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.storage.append(longUrl)
        n = len(self.storage)
        n <<= 1
        s = ''
        while n:
            n, i = divmod(n, len(self.allowed_chars))
            s += self.allowed_chars[i]
        return self.prefix + s

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        shortUrl = shortUrl[len(self.prefix):]
        n = 0
        base = 1
        for c in shortUrl:
            i = self.allowed_chars.index(c)
            n += base * i
            base *= len(self.allowed_chars)
        bit = n % 2
        n //= 2
        return self.storage[n-1]


def test():
    print()
    urls = ['http://www.google.com',
            'http://www.amazon.com',
            'http://www.leetcode.com'
            "ftp://174.123.452.34/directory/file"]
    codec = Codec()
    for url in urls:
        shortUrl = codec.encode(url)
        print(url, shortUrl)
        assert url == codec.decode(shortUrl)



if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))


