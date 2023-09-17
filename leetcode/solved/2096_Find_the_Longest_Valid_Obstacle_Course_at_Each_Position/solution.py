#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You want to build some obstacle courses. You are given a 0-indexed integer array obstacles of length n, where obstacles[i] describes the height of the ith obstacle.

For every index i between 0 and n - 1 (inclusive), find the length of the longest obstacle course in obstacles such that:

	You choose any number of obstacles between 0 and i inclusive.
	You must include the ith obstacle in the course.
	You must put the chosen obstacles in the same order as they appear in obstacles.
	Every obstacle (except the first) is taller than or the same height as the obstacle immediately before it.

Return an array ans of length n, where ans[i] is the length of the longest obstacle course for index i as described above.

Example 1:

Input: obstacles = [1,2,3,2]
Output: [1,2,3,3]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [1], [1] has length 1.
- i = 1: [1,2], [1,2] has length 2.
- i = 2: [1,2,3], [1,2,3] has length 3.
- i = 3: [1,2,3,2], [1,2,2] has length 3.

Example 2:

Input: obstacles = [2,2,1]
Output: [1,2,1]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [2], [2] has length 1.
- i = 1: [2,2], [2,2] has length 2.
- i = 2: [2,2,1], [1] has length 1.

Example 3:

Input: obstacles = [3,1,5,6,4,2]
Output: [1,1,2,3,2,2]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [3], [3] has length 1.
- i = 1: [3,1], [1] has length 1.
- i = 2: [3,1,5], [3,5] has length 2. [1,5] is also valid.
- i = 3: [3,1,5,6], [3,5,6] has length 3. [1,5,6] is also valid.
- i = 4: [3,1,5,6,4], [3,4] has length 2. [1,4] is also valid.
- i = 5: [3,1,5,6,4,2], [1,2] has length 2.

Constraints:

	n == obstacles.length
	1 <= n <= 105
	1 <= obstacles[i] <= 107
"""
import pytest
import sys
import bisect
from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        """Sep 10, 2023 14:01"""
        class SegmentTree:
            def __init__(self, arr):
                def build(i, j):
                    if i == j:
                        return [0, None, None]
                    m = i + (j-i)//2
                    l = build(i, m)
                    r = build(m+1, j)
                    return [max(l[0], r[0]), l, r]

                self.arr = arr
                self.tree = build(0, len(arr)-1)

            def query(self, n):
                i = bisect.bisect_left(self.arr, n+1)-1
                def q(i, j, l, r, tree):
                    if i <= l and r <= j:
                        return tree[0]
                    m = l + (r-l)//2
                    if j <= m:
                        return q(i, j, l, m, tree[1])
                    if m < i:
                        return q(i, j, m+1, r, tree[2])
                    return max(
                        q(i, j, l, m, tree[1]),
                        q(i, j, m+1, r, tree[2]))

                return q(0, i, 0, len(self.arr)-1, self.tree)

            def update(self, n, v):
                i = bisect.bisect_left(self.arr, n)

                def u(l, r, tree):
                    if l == r == i:
                        tree[0] = v
                        return tree[0]
                    m = l + (r-l)//2
                    if i <= m:
                        tree[0] = max(tree[2][0] if tree[2] else 0, u(l, m, tree[1]))
                    else:
                        tree[0] = max(tree[1][0] if tree[1] else 0, u(m+1, r, tree[2]))
                    return tree[0]

                return u(0, len(self.arr)-1, self.tree)


        st = SegmentTree(list(sorted(set(obstacles))))

        ret = []
        seen = []
        for o in obstacles:
            n = st.query(o)
            ret.append(n+1)
            st.update(o, n+1)
        return ret

    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        """Sep 10, 2023 14:04"""
        ret = []
        seen = []
        for o in obstacles:
            i = bisect.bisect_right(seen, o)
            if i == len(seen):
                seen.append(o)
                ret.append(len(seen))
            else:
                seen[i] = o
                ret.append(i+1)
        return ret


@pytest.mark.parametrize('args', [
    (([1,2,3,2], [1,2,3,3])),
    (([2,2,1], [1,2,1])),
    (([3,1,5,6,4,2], [1,1,2,3,2,2])),
    (([5,1,5,5,1,3,4,5,1,4], [1,1,2,3,2,3,4,5,3,5])),
])
def test(args):
    assert args[-1] == Solution().longestObstacleCourseAtEachPosition(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
