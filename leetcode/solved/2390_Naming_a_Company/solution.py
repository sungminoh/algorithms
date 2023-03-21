#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:

	Choose 2 distinct names from ideas, call them ideaA and ideaB.
	Swap the first letters of ideaA and ideaB with each other.
	If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
	Otherwise, it is not a valid name.

Return the number of distinct valid names for the company.

Example 1:

Input: ideas = ["coffee","donuts","time","toffee"]
Output: 6
Explanation: The following selections are valid:
- ("coffee", "donuts"): The company name created is "doffee conuts".
- ("donuts", "coffee"): The company name created is "conuts doffee".
- ("donuts", "time"): The company name created is "tonuts dime".
- ("donuts", "toffee"): The company name created is "tonuts doffee".
- ("time", "donuts"): The company name created is "dime tonuts".
- ("toffee", "donuts"): The company name created is "doffee tonuts".
Therefore, there are a total of 6 distinct company names.

The following are some examples of invalid selections:
- ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
- ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
- ("coffee", "toffee"): Both names formed after swapping already exist in the original array.

Example 2:

Input: ideas = ["lack","back"]
Output: 0
Explanation: There are no valid selections. Therefore, 0 is returned.

Constraints:

	2 <= ideas.length <= 5 * 104
	1 <= ideas[i].length <= 10
	ideas[i] consists of lowercase English letters.
	All the strings in ideas are unique.
"""
from collections import defaultdict
from pathlib import Path
import json
from typing import List
import pytest
import sys


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        """Mar 19, 2023 12:57
        TLE
        """
        suffixes = []
        heads = []
        head_group = defaultdict(set)
        suffix_group = defaultdict(set)
        for i, idea in enumerate(ideas):
            h, suffix = idea[0], idea[1:]
            heads.append(h)
            suffixes.append(suffix)
            suffix_group[suffix].add(i)
            head_group[h].add(i)

        ret = 0
        for idea in ideas:
            h, suffix = idea[0], idea[1:]
            invalid = set()
            for i in suffix_group[suffix]:
                invalid |= head_group[heads[i]]
            for i in head_group[h]:
                invalid |= suffix_group[suffixes[i]]
            ret += len(ideas)-len(invalid)

        return ret

    def distinctNames(self, ideas: List[str]) -> int:
        """Mar 19, 2023 13:19"""
        head_suffixes = defaultdict(set)
        for idea in ideas:
            h, suffix = idea[0], idea[1:]
            head_suffixes[h].add(suffix)

        ret = 0
        heads = list(head_suffixes.keys())
        for i in range(len(heads)):
            for j in range(i+1, len(heads)):
                a, b = heads[i], heads[j]
                if a != b:
                    invalid = len(head_suffixes[a] & head_suffixes[b])
                    ret += 2*(len(head_suffixes[a])-invalid) * (len(head_suffixes[b])-invalid)
        return ret


@pytest.mark.parametrize('args', [
    ((["coffee","donuts","time","toffee"], 6)),
    ((["coffee","donuts","conuts", "time","toffee"], 6)),
    ((["lack","back"], 0)),
    ((json.load(open(Path(__file__).parent/'testcase.json')), 233645268)),
])
def test(args):
    assert args[-1] == Solution().distinctNames(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
