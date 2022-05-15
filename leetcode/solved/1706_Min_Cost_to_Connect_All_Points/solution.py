#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Example 1:

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

Constraints:

	1 <= points.length <= 1000
	-106 <= xi, yi <= 106
	All pairs (xi, yi) are distinct.
"""
import sys
from heapq import heappop
from heapq import heappush
from typing import List
import pytest


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Time complexity: O(n^2*log(n^2))
        Space complexity: O(n^2)
        """
        def dist(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        heap = []
        graph = {}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                d = dist(points[i], points[j])
                graph.setdefault(i, {})[j] = graph.setdefault(j, {})[i] = d
                heappush(heap, (d, i, j))

        class UnionFind:
            def __init__(self):
                self.rep = {}

            def find(self, a):
                if a not in self.rep:
                    self.rep[a] = a
                if self.rep[a] != a:
                    self.rep[a] = self.find(self.rep[a])
                return self.rep[a]

            def union(self, a, b):
                pa = self.find(a)
                pb = self.find(b)
                self.rep[pa] = self.rep[pb] = min(pa, pb)

        uf = UnionFind()
        ret = 0
        while heap:
            d, i, j = heappop(heap)
            if uf.find(i) != uf.find(j):
                uf.union(i, j)
                ret += d
        return ret

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        def dist(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        graph = {}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                graph[i, j] = dist(points[i], points[j])

        class UnionFind:
            def __init__(self):
                self.rep = {}

            def find(self, a):
                if a not in self.rep:
                    self.rep[a] = a
                if self.rep[a] != a:
                    self.rep[a] = self.find(self.rep[a])
                return self.rep[a]

            def union(self, a, b):
                pa = self.find(a)
                pb = self.find(b)
                self.rep[pa] = self.rep[pb] = min(pa, pb)

        uf = UnionFind()
        ret = 0
        cnt = 0
        while graph:
            i, j = min(graph, key=graph.get)
            d = graph.pop((i, j))
            if uf.find(i) != uf.find(j):
                uf.union(i, j)
                ret += d
        return ret

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Dijkstra
        """
        def dist(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        distances = {(x, y): float('inf') for x, y in points}
        distances[tuple(points[0])] = 0
        ret = 0
        while distances:
            closest_point = min(distances, key=distances.get)
            ret += distances.pop(closest_point)
            for point in distances:
                distances[point] = min(distances[point], dist(closest_point, point))
        return ret


@pytest.mark.parametrize('points, expected', [
    ([[0,0],[2,2],[3,10],[5,2],[7,0]], 20),
    ([[3,12],[-2,5],[-4,1]], 18),
    ([[75,790],[767,519],[405,210],[-526,-175],[-126,-824],[382,862],[-832,630],[-23,-463],[62,-480],[371,724],[280,-645],[144,-115],[-212,-990],[-856,-393],[43,-429],[959,880],[267,-876],[-212,500],[-699,-240],[349,-745],[-558,92],[-52,-619],[269,282],[-403,-921],[-848,-406],[-737,-453],[335,-521],[-914,953],[-612,-268],[-133,238],[304,-477],[-312,-565],[-643,-114],[908,923],[946,-296],[-1000,-464],[770,405],[-491,543],[439,199],[31,182],[-362,790],[956,935],[-913,-368],[-766,449],[-103,96],[551,-792],[-136,456],[29,592],[462,-813],[859,-832],[-22,-987],[-762,686],[-483,281],[-115,1000],[40,-978],[993,-85],[-516,662],[797,-968],[106,-578],[-517,1000],[535,-696],[-140,-821],[-843,831],[-918,704],[-679,375],[475,105],[-293,1000],[-80,809],[-600,783],[-210,-810],[260,-234],[-374,-488],[-640,820],[-717,23],[-729,-282],[534,-752],[-775,-493],[796,-39],[-403,531],[665,543],[-51,71],[-321,576],[-513,-665],[-510,-38],[733,576],[567,461],[46,-985],[199,-462],[-145,833],[888,908],[-148,445],[-542,-432],[-277,-735],[-564,-428],[-88,790],[495,-227],[-794,83],[-691,-677],[-3,901],[999,-22],[2,408],[-300,482],[-650,-54],[-425,-875],[-163,959],[-609,123],[491,765],[-126,253],[-147,971],[-991,952],[-917,-928],[891,-717],[-232,-173],[231,-335],[869,-890],[369,-108],[708,874],[-452,785],[921,-333],[625,-257],[-490,666],[-271,974],[599,-691],[634,-731],[630,901],[426,-293],[229,-753],[-668,-371],[311,-928],[569,-154],[-766,-232],[847,-457],[48,56],[583,201],[-799,-744],[-119,-967],[-261,-970],[-100,-379],[91,-909],[7,631],[-163,-962],[-979,144],[-590,779],[30,-453],[-300,-488],[-360,-960],[-498,-465],[-753,436],[-193,-494],[-480,-730],[130,-77],[966,694],[121,-420],[359,736],[-717,683],[-786,-619],[357,-58],[163,172],[960,-153],[-89,-536],[-374,-4],[342,-493],[-631,350],[859,682],[777,954],[-124,948],[636,-79],[-587,609],[427,-816],[-856,-672],[828,152],[828,192],[-791,737],[155,-723],[-940,632],[-460,22],[519,-687],[-848,48],[535,-168],[442,304],[-267,436],[-309,-280],[160,-63],[440,229],[732,42],[592,531],[347,-494],[919,-663],[474,941],[88,-405],[-403,-529],[988,342]], 22679),
])
def test(points, expected):
    assert expected == Solution().minCostConnectPoints(points)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
