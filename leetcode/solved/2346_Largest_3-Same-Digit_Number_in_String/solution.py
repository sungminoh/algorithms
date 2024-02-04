from collections import Counter

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

	It is a substring of num with length 3.
	It consists of only one unique digit.

Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

	A substring is a contiguous sequence of characters within a string.
	There may be leading zeroes in num or a good integer.

Example 1:

Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".

Example 2:

Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.

Example 3:

Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.

Constraints:

	3 <= num.length <= 1000
	num only consists of digits.
"""
import pytest
import sys


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        """Feb 04, 2024 10:06"""
        ret = ""
        cnt = Counter()
        for i in range(len(num)):
            cnt[num[i]] += 1
            if i >= 3:
                cnt[num[i-3]] -= 1
                if cnt[num[i-3]] == 0:
                    cnt.pop(num[i-3])
            if i >= 2 and len(cnt) == 1:
                ret = max(ret, next(iter(cnt.keys()))*3)
        return ret


@pytest.mark.parametrize('args', [
    (("6777133339", "777")),
    (("2300019", "000")),
    (("42352338", "")),
])
def test(args):
    assert args[-1] == Solution().largestGoodInteger(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
