#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Note: This is a companion problem to the System Design problem: Design TinyURL.

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the Solution class:

	Solution() Initializes the object of the system.
	String encode(String longUrl) Returns a tiny URL for the given longUrl.
	String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.

Example 1:

Input: url = "https://leetcode.com/problems/design-tinyurl"
Output: "https://leetcode.com/problems/design-tinyurl"

Explanation:
Solution obj = new Solution();
string tiny = obj.encode(url); // returns the encoded tiny url.
string ans = obj.decode(tiny); // returns the original url after deconding it.

Constraints:

	1 <= url.length <= 104
	url is guranteed to be a valid URL.
"""
import sys
import pytest


class Codec:
    """06/02/2020 23:01"""
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


class Codec:
    urls = []
    idx = {}  # to check if the url was previously encoded

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.idx:
            self.idx[longUrl] = len(self.urls)
            self.urls.append(longUrl)
        return str(self.idx[longUrl])

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls[int(shortUrl)]


@pytest.mark.parametrize('url', [
    ("https://leetcode.com/problems/design-tinyurl"),
    ('http://www.google.com'),
    ('http://www.amazon.com'),
    ('http://www.leetcode.com'),
    ("ftp://174.123.452.34/directory/file"),
])
def test(url):
    obj = Codec()
    encoded = obj.encode(url)
    print(url, encoded)
    assert url == obj.decode(encoded)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
