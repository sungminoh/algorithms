
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a list of positive integers, the adjacent integers will perform the float division. For example, [2,3,4] -> 2 / 3 / 4.

However, you can add any number of parenthesis at any position to change the priority of operations. You should find out how to add parenthesis to get the maximum result, and return the corresponding expression in string format. Your expression should NOT contain redundant parenthesis.

Example:

Input: [1000,100,10,2]
Output: "1000/(100/10/2)"
Explanation:
1000/(100/10/2) = 1000/((100/10)/2) = 200
However, the bold parenthesis in "1000/((100/10)/2)" are redundant, since they don't influence the operation priority. So you should return "1000/(100/10/2)".

Other cases:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2

Note:

The length of the input array is [1, 10].
Elements in the given array will be in range [2, 1000].
There is only one optimal division for each test case.
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        @lru_cache(None)
        def sub(i, j):
            if i == j:
                return nums[i], nums[i], str(nums[i]), str(nums[i])
            mn, mx = float('inf'), -float('inf')
            mn_exp, mx_exp = '', ''
            for k in range(i, j):
                nmin, nmax, nmin_exp, nmax_exp = sub(i, k)
                dmin, dmax, dmin_exp, dmax_exp = sub(k+1, j)
                new_min = nmin/dmax
                new_max = nmax/dmin
                if new_min < mn:
                    mn = new_min
                    if '/' in dmax_exp:
                        dmax_exp = f'({dmax_exp})'
                    mn_exp = f'{nmin_exp}/{dmax_exp}'
                if new_max > mx:
                    mx = new_max
                    if '/' in dmin_exp:
                        dmin_exp = f'({dmin_exp})'
                    mx_exp = f'{nmax_exp}/{dmin_exp}'
            return mn, mx, mn_exp, mx_exp
        _, _, _, ret = sub(0, len(nums)-1)
        return ret


@pytest.mark.parametrize('nums, expected', [
    ([1000,100,10,2], "1000/(100/10/2)"),
])
def test(nums, expected):
    print()
    ans = Solution().optimalDivision(nums)
    print(expected, ans)
    assert eval(expected) == eval(ans)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
