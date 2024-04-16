#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of integers nums represents the numbers written on a chalkboard.

Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first. If erasing a number causes the bitwise XOR of all the elements of the chalkboard to become 0, then that player loses. The bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is 0.

Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to 0, then that player wins.

Return true if and only if Alice wins the game, assuming both players play optimally.

Example 1:

Input: nums = [1,1,2]
Output: false
Explanation:
Alice has two choices: erase 1 or erase 2.
If she erases 1, the nums array becomes [1, 2]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 2 = 3. Now Bob can remove any element he wants, because Alice will be the one to erase the last element and she will lose.
If Alice erases 2 first, now nums become [1, 1]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 1 = 0. Alice will lose.

Example 2:

Input: nums = [0,1]
Output: true

Example 3:

Input: nums = [1,2,3]
Output: true

Constraints:

	1 <= nums.length <= 1000
	0 <= nums[i] < 216
"""
import functools
from typing import List
from collections import Counter
import pytest
import sys


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        """Apr 15, 2024 22:46"""
        xor = functools.reduce(lambda x, y: x ^ y, nums, 0)
        counter = Counter(nums)

        def play(counter):
            keys = list(counter.keys())
            for n in keys:
                if counter[n] > 0 and xor^n != 0:
                    counter[n] -= 1
                    if counter[n] == 0:
                        counter.pop(n)
                    return xor ^ n
            return 0

        while xor != 0:
            xor = play(counter)
            if xor == 0:
                return False
            xor = play(counter)
        return True


@pytest.mark.parametrize('args', [
    (([1,1,2], False)),
    (([0,1], True)),
    (([1,2,3], True)),
])
def test(args):
    assert args[-1] == Solution().xorGame(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
