#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

Example 1:

Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]

Example 2:

Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].

Constraints:

	1 <= arr.length <= 1000
	2 <= arr[i] <= 109
	All the values of arr are unique.
"""
from collections import defaultdict
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        """05/25/2020 16:26 TLE"""
        MOD = 1e9 + 7
        nums = set(A)

        @lru_cache(None)
        def count(root):
            ret = 1
            for i in range(2, root // 2 + 1):
                if i not in nums:
                    continue
                j, r = divmod(root, i)
                if r != 0 or j not in nums:
                    continue
                comb = (count(i) * count(j)) % MOD
                ret += comb
                ret %= MOD
            return ret

        return int(sum(count(n) for n in nums) % MOD)

    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        """05/25/2020 16:43"""
        MOD = 1e9 + 7
        A = sorted(A)
        indexes = {n: i for i, n in enumerate(A)}
        counts = [0] * len(A)
        for i, n in enumerate(A):
            counts[i] += 1
            for j in range(i + 1, len(A)):
                m, r = divmod(A[j], n)
                if r != 0 or m not in indexes or m > n:
                    continue
                comb = counts[i] * counts[indexes[m]]
                if n != m:
                    comb *= 2
                counts[j] += comb
        return int(sum(counts) % MOD)

    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """08/21/2022 15:33"""
        MOD = int(1e9+7)
        nums = set(arr)
        @lru_cache(None)
        def num_trees_with_root_val(val):
            if val not in nums:
                return 0
            ret = 1
            for n in nums:
                if val%n == 0 and val//n in nums:
                    ret += (num_trees_with_root_val(n)*num_trees_with_root_val(val//n)) % MOD
                    ret %= MOD
            return ret

        return sum(num_trees_with_root_val(n) for n in arr) % MOD

    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """08/21/2022 15:35"""
        MOD = int(1e9+7)
        nums = set(arr)
        factors = defaultdict(list)
        for a in nums:
            for b in nums:
                if a*b in nums:
                    factors[a*b].append((a, b))

        @lru_cache(None)
        def num_trees_with_root_val(val):
            if val not in nums:
                return 0
            ret = 1
            for a, b in factors[val]:
                ret += (num_trees_with_root_val(a)*num_trees_with_root_val(b)) % MOD
                ret %= MOD
            return ret

        return sum(num_trees_with_root_val(n) for n in arr) % MOD


@pytest.mark.parametrize('arr, expected', [
    ([2,4], 3),
    ([2,4,5,10], 7),
    ([971588554,520749447,513757887,356788063,379421244,334699070,801826060,638738612,653781951,460666710,807141900,929231987,297512619,6379760,489106943,628271028,340935071,967513857,180148101,761244375,597342008,615772190,724451136,156377973,688556948,831332491,733176736,208041691,389648590,161022238,515610564,150675857,509429598,823949222,588859735,453671129,30238374,824683171,131803832,892866393,107942717,560039467,143093909,997422290,194174308,862589146,818071068,693274617,185009960,693700721,58513372,438718445,287965773,689582058,614172953,700651151,261372170,75354128,147909532,17228919,715958073,136158414,331954012,185618368,862734075,707150336,728938522,162008403,172786110,280903590,343005938,244111565,855806684,589965235,126901051,306282962,770459398,921746511,703761214,421881560,234488692,727254497,2759161,670049873,922168104,260297905,531652898,982438210,225731770,816657952,980558196,394321587,461519578,184495724,664385099,869060936,271278958,456998531,871564841,194362094], 100),
    ([18,3,6,2], 12),
])
def test(arr, expected):
    assert expected == Solution().numFactoredBinaryTrees(arr)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
