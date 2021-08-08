#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A car travels from a starting position to a destination which is target miles east of the starting position.

There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

Example 1:

Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.

Example 2:

Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can not reach the target (or even the first gas station).

Example 3:

Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.

Constraints:

	1 <= target, startFuel <= 109
	0 <= stations.length <= 500
	0 <= positioni <= positioni+1 < target
	1 <= fueli < 109
"""
from heapq import heappush
from heapq import heappop
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        DP: min refuel starting from i-th station with fuel
        """
        @lru_cache(None)
        def start(i, fuel):
            if i == len(stations)-1:
                return 0
            cp, cf = stations[i]
            fuel += cf
            ret = float('inf')
            for j in range(i+1, len(stations)):
                np, _ = stations[j]
                if np-cp > fuel:
                    break
                ret = min(ret, 1 + start(j, fuel - (np-cp)))
            return ret

        stations.insert(0, [0, startFuel])
        stations.append([target, 0])
        ret = start(0, 0)-1
        return ret if ret != float('inf') else -1

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        DP: max_fuel at i-th station when refuel n times
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        dp = [startFuel]  # (pos, num_refuel) -> max_fuel
        stations.insert(0, [0, startFuel])
        stations.append([target, 0])
        for i in range(1, len(stations)):
            dist = stations[i][0] - stations[i-1][0]
            row = [dp[n] - dist for n in range(0, i)]
            for n in range(1, i):
                if dp[n-1] >= dist:
                    row[n] = max(row[n], dp[n-1] - dist + stations[i][1])
            if dp[i-1] >= dist:
                row.append(dp[i-1] - dist + stations[i][1])
            else:
                row.append(-1)
            dp = row
        for i, v in enumerate(dp):
            if v >= 0:
                return i
        else:
            return -1

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        An array keeps all possible cases
        Time complexity: O(2^n)
        Space complexity: O(2^n)
        """
        h = [(0, startFuel)]
        stations.insert(0, [0, startFuel])
        stations.append([target, 0])
        for i, (pos, fuel) in enumerate(stations[1:], 1):
            dist = stations[i][0] - stations[i-1][0]
            h_ = [(x[0], x[1]-dist) for x in h if x[1] >= dist]
            h = h_ + [(x[0]+1, x[1]+fuel) for x in h_]
        return min(x[0] for x in h) if h else -1

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        Min-heap keeps the min refuel
        Time complexity: O(2^n)
        Space complexity: O(2^n)
        """
        h = [(0, 0, startFuel)]  # refuel, idx, fuel
        stations.insert(0, [0, startFuel])
        stations.append([target, 0])

        while h and h[0][1] != len(stations)-1:
            n, i, f = heappop(h)
            dist = stations[i+1][0] - stations[i][0]
            if f >= dist:
                heappush(h, (n, i+1, f-dist))
                heappush(h, (n+1, i+1, f-dist+stations[i+1][1]))
        return -1 if not h else h[0][0]

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        Furthest position with cnt refuel. Assume that we refueled at the
        station that had the largest fuel when refuel is needed.
        Time complexity: O(n*logn)
        Space complexity: O(n)
        """
        p = 0
        cnt = 0
        i = 0
        h = [-startFuel]
        while h:
            f = -heappop(h)
            p += f
            if p >= target:
                return cnt
            while i < len(stations) and stations[i][0] <= p:
                heappush(h, -stations[i][1])
                i += 1
            cnt += 1
        return -1


@pytest.mark.parametrize('target, startFuel, stations, expected', [
    (1, 1, [], 0),
    (100, 1, [[10,100]], -1),
    (100, 10, [[10,60],[20,30],[30,30],[60,40]], 2),
    (1000000, 8663, [[31,195796],[42904,164171],[122849,139112],[172890,121724],[182747,90912],[194124,112994],[210182,101272],[257242,73097],[284733,108631],[369026,25791],[464270,14596],[470557,59420],[491647,192483],[516972,123213],[577532,184184],[596589,143624],[661564,154130],[705234,100816],[721453,122405],[727874,6021],[728786,19444],[742866,2995],[807420,87414],[922999,7675],[996060,32691]], 6),
    (1000, 10, [[1,209],[2,30],[24,106],[25,3],[30,164],[33,4],[38,40],[56,202],[58,219],[69,90],[77,45],[78,90],[89,171],[94,26],[96,165],[109,122],[110,14],[121,142],[141,154],[150,196],[155,67],[159,246],[175,58],[203,71],[211,173],[226,64],[249,89],[272,74],[275,99],[276,205],[278,160],[279,203],[281,15],[282,72],[283,124],[295,90],[296,8],[307,120],[313,73],[327,15],[330,135],[331,87],[353,217],[364,120],[367,99],[371,152],[385,175],[392,241],[393,112],[399,125],[400,88],[409,187],[444,129],[448,158],[466,247],[468,153],[470,227],[474,129],[476,80],[477,198],[505,20],[529,125],[552,91],[553,59],[578,180],[587,142],[599,134],[617,224],[629,55],[649,79],[664,63],[669,236],[679,101],[694,108],[707,161],[717,32],[719,228],[721,95],[738,120],[747,59],[761,164],[769,153],[795,154],[802,236],[836,229],[849,247],[866,34],[874,45],[876,4],[880,31],[895,125],[908,188],[909,182],[911,62],[915,222],[928,34],[931,115],[934,165],[971,92],[993,221]], 5),
])
def test(target, startFuel, stations, expected):
    assert expected == Solution().minRefuelStops(target, startFuel, stations)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
