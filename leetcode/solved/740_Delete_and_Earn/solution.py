#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

	Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.

Return the maximum number of points you can earn by applying the above operation some number of times.

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.

Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.

Constraints:

	1 <= nums.length <= 2 * 104
	1 <= nums[i] <= 104
"""
from functools import lru_cache
import math
import sys
from collections import Counter
from typing import List
import pytest


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """Wrong"""
        cnt = Counter(nums)
        keys = sorted(cnt.keys(), key=lambda x: x*cnt[x], reverse=True)
        for k in keys:
            print(k, cnt[k])
        ret = 0
        visited = set()
        for k in keys:
            if k in visited:
                continue
            ret += k*cnt[k]
            visited.add(k-1)
            visited.add(k+1)
        return ret

    def deleteAndEarn(self, nums: List[int]) -> int:
        """09/05/2020 13:01"""
        cnt = Counter(nums)
        keys = sorted(cnt.keys())

        @lru_cache(None)
        def rec(i, used=False):
            if i < 0:
                return 0
            k = keys[i]
            if k-1 not in cnt:
                ret = k*cnt[k] + rec(i-1, False)
            else:
                # not use the current key
                ret = rec(i-1, False)
                save = cnt[k-1]
                cnt[k-1] = 0
                ret = max(ret, k*cnt[k] + rec(i-1, True))
                cnt[k-1] = save
            return ret

        return rec(len(keys)-1)

    def deleteAndEarn(self, nums: List[int]) -> int:
        """TLE"""
        def dfs(cnt):
            max_k = None
            ret = 0
            for k in cnt:
                if cnt[k] == 0:
                    continue

                # save
                n = cnt[k]
                cnt[k] = 0
                a = 0
                if k-1 in cnt:
                    a = cnt[k-1]
                    cnt[k-1] = 0
                b = 0
                if k+1 in cnt:
                    b = cnt[k+1]
                    cnt[k+1] = 0

                # recursion
                points = n*k + dfs(cnt)
                if points > ret:
                    max_k = k
                    ret = max(ret, points)

                # restore
                cnt[k] = n
                if a > 0:
                    cnt[k-1] = a
                if b > 0:
                    cnt[k+1] = b

            return ret

        return dfs(Counter(nums))

    def deleteAndEarn(self, nums: List[int]) -> int:
        """TLE"""
        cnt = Counter(nums)
        keys = list(cnt.keys())
        key_index = {k: i for i, k in enumerate(keys)}
        allbit = (1<<len(keys))-1

        @lru_cache(None)
        def dfs(visited):
            if visited == allbit:
                return 0
            # find a key which is not yet visited
            bit = (visited+1) & (~visited)  # least significant zero bit
            i = int(math.log2(bit))
            k = keys[i]
            # 1. when the key is not picked
            visited |= bit
            ret = dfs(visited)
            # 2. when the key is picked
            if k-1 in key_index:
                visited |= (1 << key_index[k-1])
            if k+1 in key_index:
                visited |= (1 << key_index[k+1])
            ret = max(ret, k*cnt[k] + dfs(visited))
            return ret

        return dfs(0)

    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        DP recursion
        Time complexity: O(n)
        Space complexity: O(n)
        """
        cnt = Counter(nums)
        keys = list(sorted(cnt.keys()))

        @lru_cache(None)
        def dp(i, use):
            if i == len(keys):
                return 0
            if use:
                ret = cnt[keys[i]] * keys[i]
                if i+1 < len(keys) and keys[i+1] == keys[i]+1:
                    ret += dp(i+1, use=False)
                else:
                    ret += max(dp(i+1, use=False), dp(i+1, use=True))
                return ret
            else:
                return max(dp(i+1, use=False), dp(i+1, use=True))

        return max(dp(0, False), dp(0, True))

    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        DP bottom up
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not nums:
            return 0
        cnt = Counter(nums)
        keys = list(sorted(cnt.keys()))
        used, notused = cnt[keys[0]]*keys[0], 0
        for i in range(1, len(keys)):
            if keys[i] == keys[i-1]+1:
                _notused = max(used, notused)
                _used = notused + cnt[keys[i]]*keys[i]
            else:
                _used = max(used, notused) + cnt[keys[i]]*keys[i]
                _notused = max(used, notused)
            used = _used
            notused = _notused

        return max(used, notused)


@pytest.mark.parametrize('nums, expected', [
    ([3,4,2], 6),
    ([2,2,3,3,3,4], 9),
    ([37,6,8,34,67,54,13,26,41,54,58,34,96,40,52,59,95,61,39,30,76,99,93,34,63,77,37,47,74,65,85,93,20,43,29,60,63,46,17,28,73,49,1,71,99,93,46,29,1,44,93,64,84,73,2,10,22,87,14,70,32,58,20,87,57,17,55,55,15,16,38,67,98,78,61,13,92,32,75,64,78,25,85,34,51,28,100,30,10,45,65,52,13,80,35,8,84,1,60,11,54,92,22,26,54,30,97,54,62,59,92,64,21,69,88,27,73,20,42,5,52,93,46,71,75,63,77,18,27,14,45,72,80,36,30,89,49,79,18,24,39,9,30,27,69,7,100,56,30,77,89,97,20,65,38,17,19,92,84,99,21,49,62,52,19,78,47,62,79,29,64,36,7,9,69,80,20,24,78,93,54,79,54,96,72,76,5,63,33,20,32,36,69,69,11,35,71,79,66,46], 6238),
])
def test(nums, expected):
    print()
    assert expected == Solution().deleteAndEarn(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
