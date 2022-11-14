#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

	For example, "AACCGGTT" --> "AACCGGTA" is one mutation.

There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

Constraints:

	0 <= bank.length <= 10
	startGene.length == endGene.length == bank[i].length == 8
	startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
"""
from collections import deque
from collections import defaultdict
from typing import Dict
from typing import List
import pytest
import sys


def msb(n: int, bit=16) -> int:
    b = 1
    while b < bit:
        n |= n >> b
    n += 1
    return n >> 1


def lsb(n: int) -> int:
    return n & -n


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def gene2num(s: str) -> int:
            ret = 0
            for i, c in enumerate(s):
                ret += {'A': 0, 'C': 1, 'G': 2, 'T': 3}[c] * pow(4, i)
            # 00 00 00 00 / 00 00 00 00
            return ret

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

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        m = {c: 1<<i for i, c in enumerate('ACGT')}
        def encode(gene):
            ret = 0
            for c in gene:
                ret <<= 4
                ret |= m[c]
            return ret

        def is_mutation(a, b):
            x = a^b
            first = x&(~x+1)
            x ^= first
            second = x&(~x+1)
            x ^= second
            return x == 0

        s = encode(startGene)
        e = encode(endGene)
        bk = [encode(x) for x in bank]
        bk.append(s)
        g = defaultdict(set)
        for i in range(len(bk)):
            a = bk[i]
            for j in range(i+1, len(bk)):
                b = bk[j]
                if is_mutation(a, b):
                    g[a].add(b)
                    g[b].add(a)

        # bfs
        visited = set([s])
        queue = deque([(s, 0)])
        while queue:
            x, d = queue.popleft()
            if x == e:
                return d
            for y in g[x]:
                if y not in visited:
                    visited.add(y)
                    queue.append((y, d+1))
        return -1


@pytest.mark.parametrize('startGene, endGene, bank, expected', [
    ("AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
    ("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"], 2),
    ('AAAAACCC', 'AACCCCCC', ['AAAACCCC', 'AAACCCCC', 'AACCCCCC'], 3),
])
def test(startGene, endGene, bank, expected):
    assert expected == Solution().minMutation(startGene, endGene, bank)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
