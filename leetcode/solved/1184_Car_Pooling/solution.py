#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true

Constraints:

	1 <= trips.length <= 1000
	trips[i].length == 3
	1 <= numPassengersi <= 100
	0 <= fromi < toi <= 1000
	1 <= capacity <= 105
"""
from collections import defaultdict
import sys
from heapq import heappush
from heapq import heappop
from typing import List
import pytest


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Heap
        Time complexity: O(nlogn)
        Space complexity: O(n)
        """
        trips.sort(key=lambda x: (x[1], x[2]))
        occ = 0
        h = []
        for p, s, e in trips:
            while h and h[0][0] <= s:
                occ -= heappop(h)[1]
            occ += p
            heappush(h, (e, p))
            if occ > capacity:
                return False
        return True

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Counter
        Time complexity: O(n)
        Space complexity: O(n)
        """
        changes = defaultdict(int)
        for p, s, e in trips:
            changes[s] += p
            changes[e] -= p

        occ = 0
        for i in sorted(changes.keys()):
            occ += changes[i]
            if occ > capacity:
                return False

        return True


@pytest.mark.parametrize('trips, capacity, expected', [
    ([[2,1,5],[3,3,7]], 4, False),
    ([[2,1,5],[3,3,7]], 5, True),
])
def test(trips, capacity, expected):
    assert expected == Solution().carPooling(trips, capacity)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
