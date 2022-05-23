#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

	Only numbers 1 through 9 are used.
	Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

Constraints:

	2 <= k <= 9
	1 <= n <= 60
"""
import sys
from typing import List
import pytest


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """05/02/2019 02:09"""
        memo = {}

        def combination(k: int, n: int, m: int) -> List[List[int]]:
            if k == 1:
                if m <= n <= 9:
                    return [[n]]
                else:
                    return []
            if (k, n, m) in memo:
                # hit += 1
                return memo[(k, n, m)]
            ret = []
            for i in range(m, 10):
                ret.extend([[i, *s] for s in combination(k - 1, n - i, i + 1)])
            memo[(k, n, m)] = ret
            return ret

        ret = combination(k, n, 1)
        return ret

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """05/02/2019 02:24"""
        def dfs(k, n, m):
            if k == 1:
                return [[n]] if m <= n <= 9 else []
            ret = []
            for i in range(m, 10):
                ret.extend([[i, *s] for s in dfs(k - 1, n - i, i + 1)])
            return ret
        return dfs(k, n, 1)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """05/22/2022 15:11"""
        def dfs(i, cur, acc):
            if len(cur) == k and acc == n:
                return [cur]
            if len(cur) >= k or i >= 10 or i > n-acc:
                return []
            return dfs(i+1, cur + [i], acc+i) + dfs(i+1, cur, acc)

        return dfs(1, [], 0)


@pytest.mark.parametrize('k, n, expected', [
    (3, 7, [[1,2,4]]),
    (3, 9, [[1,2,6],[1,3,5],[2,3,4]]),
    (4, 1, []),
    (4, 24, [[1,6,8,9],[2,5,8,9],[2,6,7,9],[3,4,8,9],[3,5,7,9],[3,6,7,8],[4,5,6,9],[4,5,7,8]]),
])
def test(k, n, expected):
    assert expected == Solution().combinationSum3(k, n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
