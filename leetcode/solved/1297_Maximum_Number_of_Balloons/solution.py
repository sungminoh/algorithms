#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0

Constraints:

	1 <= text.length <= 104
	text consists of lower case English letters only.
"""
import sys
from collections import Counter
import pytest


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter('balloon')
        cnt = Counter(text)

        def deduct(a, b):
            for k, v in a.items():
                if k not in b or b[k] < v:
                    return False
                b[k] -= v
            return True

        ret = 0
        while deduct(balloon, cnt):
            ret += 1
        return ret


@pytest.mark.parametrize('text, expected', [
    ("nlaebolko", 1),
    ("loonbalxballpoon", 2),
    ("leetcode", 0),
])
def test(text, expected):
    assert expected == Solution().maxNumberOfBalloons(text)


if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
