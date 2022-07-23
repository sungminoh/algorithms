#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

Constraints:

	1 <= products.length <= 1000
	1 <= products[i].length <= 3000
	1 <= sum(products[i].length) <= 2 * 104
	All the strings of products are unique.
	products[i] consists of lowercase English letters.
	1 <= searchWord.length <= 1000
	searchWord consists of lowercase English letters.
"""
import sys
from heapq import heappop
from heapq import heappush
import operator
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        Time complexity: O(n*l)
        Space complexity: O(n*l)
        """
        def infdict():
            return defaultdict(infdict)

        class ContraStr:
            def __init__(self, s):
                self.s = s

            def __lt__(self, other):
                return self.s.__gt__(other.s)

            def __le__(self, other):
                return self.s.__ge__(other.s)

            def __eq__(self, other):
                return self.s.__eq__(other.s)

            def __ne__(self, other):
                return self.s.__ne__(other.s)

            def __gt__(self, other):
                return self.s.__lt__(other.s)

            def __ge__(self, other):
                return self.s.__le__(other.s)

        class Heap:
            def __init__(self, capacity=float('inf'), key=None):
                self.capacity = capacity
                self.key = key or (lambda x: x)
                self.h = []

            def add(self, v):
                heappush(self.h, (self.key(v), v))
                while len(self.h) > self.capacity:
                    heappop(self.h)

            def peak(self):
                return self.h[0]

        trie = infdict()
        for i, product in enumerate(products):
            m = trie
            for c in product:
                m = m[c]
                m.setdefault(None, Heap(capacity=3, key=lambda i: ContraStr(products[i])))
                m[None].add(i)

        ret = []
        m = trie
        for c in searchWord:
            m = m[c]
            if None in m:
                ret.append(sorted([x[0].s for x in m[None].h]))
            else:
                ret.append([])
        return ret


@pytest.mark.parametrize('products, searchWord, expected', [
    (["mobile","mouse","moneypot","monitor","mousepad"], "mouse", [
        ["mobile","moneypot","monitor"],
        ["mobile","moneypot","monitor"],
        ["mouse","mousepad"],
        ["mouse","mousepad"],
        ["mouse","mousepad"]
    ]),
    (["havana"], "havana", [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]),
    (["bags","baggage","banner","box","cloths"], "bags", [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]),
    (["havana"], "tatiana", [[],[],[],[],[],[],[]]),
])
def test(products, searchWord, expected):
    actual = Solution().suggestedProducts(products, searchWord)
    assert expected == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
