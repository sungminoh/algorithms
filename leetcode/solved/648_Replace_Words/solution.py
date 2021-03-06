#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:

Input: dict = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Constraints:

	The input will only have lower-case letters.
	1 <= dict.length <= 1000
	1 <= dict[i].length <= 100
	1 <= sentence words number <= 1000
	1 <= sentence words length <= 1000
"""
import sys
from typing import List
import pytest


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        dict.sort(key=len)
        ret = []
        for w in sentence.split():
            for d in dict:
                if w.startswith(d):
                    ret.append(d)
                    break
            else:
                ret.append(w)
        return ' '.join(ret)


@pytest.mark.parametrize('dict, sentence, expected', [
    (["cat","bat","rat"], "the cattle was rattled by the battery", "the cat was rat by the bat"),
])
def test(dict, sentence, expected):
    assert expected == Solution().replaceWords(dict, sentence)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
