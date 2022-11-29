#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We are given n different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given string target by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.

Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and target was chosen as a concatenation of two random words.

Example 1:

Input: stickers = ["with","example","science"], target = "thehat"
Output: 3
Explanation:
We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.

Example 2:

Input: stickers = ["notice","possible"], target = "basicbasic"
Output: -1
Explanation:
We cannot form the target "basicbasic" from cutting letters from the given stickers.

Constraints:

	n == stickers.length
	1 <= n <= 50
	1 <= stickers[i].length <= 10
	1 <= target.length <= 15
	stickers[i] and target consist of lowercase English letters.
"""
from functools import lru_cache
from typing import List
import pytest
import sys


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        """11/28/2022 15:49 TLE"""
        def encode(word):
            cnt = [0]*26
            for c in word:
                cnt[ord(c)-ord('a')] += 1
            return tuple(cnt)

        def decode(cnt):
            ret = ''
            for i, c in enumerate(cnt):
                ret += chr(ord('a')+i)*c
            return ret

        chars = set(target)
        encoded = [encode(word) for word in stickers if set(word)&chars]
        N = len(encoded)
        tg = encode(target)
        for i, c in enumerate(tg):
            if c>0 and all(cnt[i]==0 for cnt in encoded):
                return -1

        @lru_cache(None)
        def dp(i, tg):
            if all(x == 0 for x in tg):
                return 0
            if i == N:
                return float('inf')
            cur = encoded[i]
            ret = dp(i+1, tg)
            for k in range(1, max((b+(a-1))//a for a, b in zip(cur, tg) if a > 0)+1):
                ret = min(ret, k + dp(i+1, tuple(max(0, b-(a*k)) for a, b in zip(cur, tg))))
            return ret

        ret = dp(0, tg)
        return ret if ret != float('inf') else -1

    def minStickers(self, stickers: List[str], target: str) -> int:
        """11/28/2022 16:12"""
        def encode(word):
            cnt = [0]*26
            for c in word:
                cnt[ord(c)-ord('a')] += 1
            return tuple(cnt)

        def decode(cnt):
            ret = ''
            for i, c in enumerate(cnt):
                ret += chr(ord('a')+i)*c
            return ret

        chars = set(target)
        encoded = [encode(word) for word in stickers if set(word)&chars]
        N = len(encoded)
        for i, c in enumerate(encode(target)):
            if c>0 and all(cnt[i]==0 for cnt in encoded):
                return -1

        @lru_cache(None)
        def dp(target):
            if not target:
                return 0
            ret = float('inf')
            for cnt in encoded:
                if cnt[ord(target[0])-ord('a')] == 0:
                    continue
                remain = tuple(max(0, b-a) for a, b in zip(cnt, encode(target)))
                ret = min(ret, 1+dp(decode(remain)))
            return ret

        ret = dp(target)
        return ret if ret != float('inf') else -1


@pytest.mark.parametrize('stickers, target, expected', [
    (["with","example","science"], "thehat", 3),
    (["notice","possible"], "basicbasic", -1),
    (["these","guess","about","garden","him"], "atomher", 3),
    (["tone","crowd","danger","money","some","product","high","cost","open","boat","scale","fair","twenty","top","night","cent","silver","paint","wood","black","which","of","type","life","finish","run","garden","shall","men","most","fall","put","quick","class","must","count","instant","third","plural","decimal","tree","gun","act","weather","pay","fun","tall","toward","round","south"], "steelhelp", 3),
    (["divide","danger","student","share","feet","say","expect","chair","special","blue","differ","thank","doctor","top","there","had","ice","mark","note","equate","basic","so","hope","happy","draw","evening","star","shall","thousand","mother","quite","letter","atom","baby","such","trouble","stand","day","room","third","level","salt","thing","shore","truck","block","time","fresh","dream","talk"], "distantcollect", 4),
])
def test(stickers, target, expected):
    assert expected == Solution().minStickers(stickers, target)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
