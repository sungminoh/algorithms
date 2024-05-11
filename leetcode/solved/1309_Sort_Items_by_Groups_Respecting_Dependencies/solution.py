#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

	The items that belong to the same group are next to each other in the sorted list.
	There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).

Return any solution if there is more than one solution and return an empty list if there is no solution.

Example 1:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]

Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.

Constraints:

	1 <= m <= n <= 3 * 104
	group.length == beforeItems.length == n
	-1 <= group[i] <= m - 1
	0 <= beforeItems[i].length <= n - 1
	0 <= beforeItems[i][j] <= n - 1
	i != beforeItems[i][j]
	beforeItems[i] does not contain duplicates elements.
"""
from collections import defaultdict
from collections import deque
from typing import List
import pytest
import sys


class Solution:
    """May 04, 2024 21:02"""
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        no_group = -1
        group_indices = {}
        for i in range(len(group)):
            if group[i] < 0:
                group[i] = no_group
                no_group -= 1
            group_indices.setdefault(group[i], set()).add(i)


        def sort_indices(indices):
            indegree = defaultdict(int)
            out = defaultdict(list)
            for i in indices:
                for j in beforeItems[i]:
                    if j in indices:
                        indegree[i] += 1
                        out[j].append(i)
            queue = deque([i for i in indices if indegree[i] == 0])
            ret = []
            while queue:
                i = queue.popleft()
                ret.append(i)
                for j in out[i]:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        queue.append(j)
            return ret

        group_indices = {g: sort_indices(indices) for g, indices in group_indices.items()}

        group_dependencies = defaultdict(set)
        for i, bf in enumerate(beforeItems):
            for j in bf:
                gp = group[j]
                gn = group[i]
                if gp != gn:
                    group_dependencies[gp].add(gn)

        group_indegree = defaultdict(int)
        for pre, posts in group_dependencies.items():
            for x in posts:
                group_indegree[x] += 1

        ret = []
        queue = deque([g for g in group_indices if group_indegree[g] == 0])
        while queue:
            g = queue.popleft()
            ret.extend(group_indices[g])
            for ng in group_dependencies[g]:
                group_indegree[ng] -= 1
                if group_indegree[ng] == 0:
                    queue.append(ng)
        return ret if len(ret) == len(group) else []


def check(arr, group, beforeItems):
    for i, bf in enumerate(beforeItems):
        if bf:
            ii = arr.index(i)
            for j in bf:
                assert arr.index(j) < ii, f'{j} must appear first than {i}'
    groups = [group[n] for n in arr]
    seen = set()
    cur = groups[0]
    for g in groups:
        if g != cur:
            assert cur not in seen
            seen.add(cur)
            cur = g
    assert cur not in seen


@pytest.mark.parametrize('args', [
    ((8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3,6],[],[],[]], [6,3,4,1,5,2,0,7])),
    ((8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3],[],[4],[]], [])),
])
def test(args):
    actual = Solution().sortItems(*args[:-1])
    if not actual:
        assert args[-1] == actual
    else:
        check(actual, args[2], args[3])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
