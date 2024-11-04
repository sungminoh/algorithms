#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Convert a non-negative integer num to its English words representation.

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Constraints:

	0 <= num <= 231 - 1
"""
from collections import deque
import pytest
import sys


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        one = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
               'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        unit = ['', 'Thousand', 'Million', 'Billion']
        i = 0
        s = []
        while num:
            num, n = divmod(num, 1000)
            h, n = divmod(n, 100)
            t, o = divmod(n, 10)
            strings = []
            if h >= 1:
                strings.append(f'{one[h]} Hundred')
            if t >= 2:
                strings.append(tens[t])
            else:
                o += 10 * t
            if o >= 1:
                strings.append(one[o])
            if strings:
                strings.append(unit[i])
                s.append(' '.join(strings).strip())
            i += 1
        return ' '.join(reversed(s)).strip()

    def numberToWords(self, num: int) -> str:
        """Nov 03, 2024 19:26"""
        if num == 0:
            return "Zero"

        def read(num):
            ONES = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
            TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            LESS_20 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
            if num >= 100:
                p, r = divmod(num, 100)
                return f"{ONES[p]} Hundred {read(r)}".strip()
            elif 10 <= num < 20:
                return LESS_20[num-10]
            else:
                p, r = divmod(num, 10)
                return f"{TENS[p]} {ONES[r]}".strip()


        ret = []
        scale = deque(["", "Thousand", "Million", "Billion"])
        while num:
            num, cur = divmod(num, 1000)
            text = read(cur)
            post = scale.popleft()
            if text:
                ret.append(post)
                ret.append(text)
        return " ".join(reversed(ret)).strip()


@pytest.mark.parametrize('args', [
    ((123, "One Hundred Twenty Three")),
    ((12345, "Twelve Thousand Three Hundred Forty Five")),
    ((1234567, "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")),
    ((1000000, "One Million")),
    ((1234567891,"One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One")),
    ((0, "Zero")),
    ((18, "Eighteen")),
    ((1000010, "One Million Ten")),
])
def test(args):
    assert args[-1] == Solution().numberToWords(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
