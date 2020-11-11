
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""
import random
from collections import Counter
from collections import defaultdict
from typing import List
import pytest


class Solution:

    def __init__(self, nums: List[int]):
        self.positions = defaultdict(list)
        for i, n in enumerate(nums):
            self.positions[n].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.positions[target])



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


@pytest.mark.parametrize('nums', [
    [1,2,3,3,3],
])
def test(nums):
    s = Solution(nums)
    cnt = Counter(nums)
    n = cnt.most_common(1)[0][0]
    picked = defaultdict(int)
    for _ in range(10000):
        picked[s.pick(n)] += 1
    print(picked)
