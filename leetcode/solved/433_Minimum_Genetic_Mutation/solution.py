
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

	Starting point is assumed to be valid, so it might not be included in the bank.
	If multiple mutations are needed, all mutations during in the sequence must be valid.
	You may assume start and end string is not the same.

Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1

Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2

Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3
"""
import sys
from collections import deque
from collections import defaultdict
from typing import Dict
from typing import List
import pytest





def gene2num(s: str) -> int:
    ret = 0
    for i, c in enumerate(s):
        ret += {'A': 0, 'C': 1, 'G': 2, 'T': 3}[c] * pow(4, i)
    # 00 00 00 00 / 00 00 00 00
    return ret


def msb(n: int, bit=16) -> int:
    b = 1
    while b < bit:
        n |= n >> b
    n += 1
    return n >> 1


def lsb(n: int) -> int:
    return n & -n


def is_mutation(a: int, b: int) -> bool:
    xor = a ^ b
    diff = False
    while xor:
        if xor % 4 > 0:
            if diff:
                return False
            else:
                diff = True
        xor >>= 2
    return diff


def build_graph(lst: List[int]) -> Dict:
    ret = defaultdict(list)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_mutation(lst[i], lst[j]):
                ret[lst[i]].append(lst[j])
                ret[lst[j]].append(lst[i])
    return ret


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        s = gene2num(start)
        e = gene2num(end)
        pool = [gene2num(g) for g in set(bank + [start])]
        graph = build_graph(pool)

        queue = deque([(0, s)])
        while queue:
            d, n = queue.popleft()
            for m in graph[n]:
                if m == e:
                    return d + 1
                else:
                    queue.append((d + 1, m))
            graph.pop(n)

        return -1


@pytest.mark.parametrize('start, end, bank, expected', [
    ('AACCGGTT', 'AACCGGTA', ['AACCGGTA'], 1),
    ('AACCGGTT', 'AAACGGTA', ['AACCGGTA', 'AACCGCTA', 'AAACGGTA'], 2),
    ('AAAAACCC', 'AACCCCCC', ['AAAACCCC', 'AAACCCCC', 'AACCCCCC'], 3),
])
def test(start, end, bank, expected):
    assert expected == Solution().minMutation(start, end, bank)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
