#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
"""


import pytest
from typing import List
from itertools import combinations
from functools import lru_cache

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        @lru_cache()
        def _rec(i):
            ret = [nums[i]]
            for j, n in enumerate(nums[:i]):
                if nums[i] % n == 0:
                    ret = max(ret, _rec(j) + [nums[i]], key=len)
            return ret

        nums = sorted(nums)
        return max([_rec(i) for i in range(len(nums))], key=len)


    def _largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        m = 0
        def _rec(nums, i, cur):
            nonlocal m
            if len(nums) - i + len(cur) <= m:
                return []
            if i == len(nums):
                m = max(m, len(cur))
                return cur[:]
            ret = []
            if not cur or nums[i] % cur[-1] == 0:
                cur.append(nums[i])
                ret = max(ret, _rec(nums, i + 1, cur), key=lambda x: len(x))
                cur.pop()
            return max(ret, _rec(nums, i + 1, cur), key=lambda x: len(x))
        return _rec(sorted(nums), 0, [])


@pytest.mark.parametrize('nums', [
    [1,2,3],
    [1,2,4,8],
    # [425,197,7,865,438,500,838,521,642,941,621,879,17,44,640,589,538,123,631,139,643,33,806,262,647,189,193,597,368,120,982,145,668,988,9,105,488,198,625,129,491,359,507,351,448,529,473,430,667,467,462,472,80,460,660,272,56,380,391,37,524,58,376,884,515,863,433,344,923,440,702,782,79,52,581,960,876,10,626,342,471,98,773,282,109,689,840,786,77,715,196,452,598,710,315,383,552,305,991,63,86,422,18,381,27,6,36,849,455,808,130,916,204,818,755,989,894,470,536,346,419,245,12,801,149,373,458,435,895,560,901,913,292,595,939,298,630,788,104,789,269,19,992,87,126,333,332,947,868,677,365,465,40,518,613,412,975,103,847,221,15,99,133,306,693,424,955,674,563,411,463,831,429,906,138,601,852,358,629,569,822,669,432,240,632,254,729,117,912,540,218,447,102,628,909,284,409,714,553,314,153,561,781,734,171,871,585,934,110,214,565,716,294,979,67,572,513,25,176,309,584,861,249,393,766,203,38,725,260,882,658,722,575,741,607,767,159,179,23,555,841,147,776,984,75,377,439,142,681,936,697,71,421,682,403,264,5,543,356,611,661,514,141,888,696,167,34,910,943,370,337,319,746,775,812,778,62,508,200,646,929,815,636,363,434,325,839,300,466,165,539,573,774,274,942,592,39,237,168,263,296,236,615,414,326,253,977,756,769,268,100,42,151,316,770,387,938,684,227,905,793,127,140,685,554,31,158,986,787,278,406,378,670,950,688,192,76,759,937,904,228,428,588,320,842,582,497,723,692,993,832,108,137,867,590,880,169,307,709,542,833,238,952,22,745,750,662,820,694,802,570,20,512,53,680,711,520,505,61,535,94,441,486,115,286,211,88,35,347,749,206,795,639,248,596,69,967,72,107,751,184,270,885,163,256,475,257,893,933,980,928,649,874,772,896,821,317,972,551,209,713,634,235,526,55,956,188,810,311,994,417,604,564,82,890,170,948,523,757,341,401,666,974,478,3,132,633,485,49,663,187,606,510,384,246,136,469,517,587,608,1000,571,92,355,675,213,14,78,81,379,957,889,483,480,848,482,51,291,836,374,965,768,362,122,407,385,605,721,357,66,250,258,900,730,457,733,747,124,591,304,814,550,546,366,144,946,963,303,911,45,764,791,853,444,83,809,798,799,652,954,251,858,46,490,90,233,70,225,85,106,95,493,453,578,777,450,386,659,431,873,330,819,155,959,897,494,349,878,160,327,186,338,446,474,624,739,166,837,945,11,645,125,289,442,299,343,593,217,953,202,394,340,230,285,423,281,74,843,864,887,617,708,921,261,719,220,113,243,924,89,162,908,835,586,367,426,413,686,827,280,48,971,877,785,926,657,288,60,616,845,267,566,295,917,208,252,21,830,807,720,339,931,886,999,402,182],
    [],
    [3,4,16,8],
    [2,3,4,9,8],
])
def test(nums):
    def is_divisible(subset):
        if not subset:
            return True
        subset = sorted(subset)
        for i in range(len(subset) - 1):
            if subset[i + 1] % subset[i] != 0:
                return False
        return True

    subset = Solution().largestDivisibleSubset(nums)
    print(subset)
    assert is_divisible(subset)
    for l in range(len(subset) + 1, len(nums) + 1):
        for larger_subset in combinations(nums, l):
            if is_divisible(larger_subset):
                assert len(larger_subset) < len(subset)
                return
