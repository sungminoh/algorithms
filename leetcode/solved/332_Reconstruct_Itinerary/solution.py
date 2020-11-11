#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""

import pytest
from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        cnt = len(tickets)
        tmap = defaultdict(list)
        for f, t in sorted(tickets):
            tmap[f].append(t)

        def rec(it):
            if len(it) == cnt + 1:
                return it
            ts = tmap[it[-1]]
            for i in range(len(ts)):
                it.append(ts.pop(i))
                res = rec(it)
                if res:
                    return res
                ts.insert(i, it.pop())
            return None

        return rec(['JFK'])


@pytest.mark.parametrize('tickets', [
    [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
    [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
])
def test(tickets):
    tmap = defaultdict(list)
    for f, t in tickets:
        tmap[f].append(t)

    itenerary = Solution().findItinerary(tickets)
    for i in range(len(itenerary) - 1):
        assert itenerary[i] in tmap
        assert itenerary[i + 1] in tmap[itenerary[i]]
