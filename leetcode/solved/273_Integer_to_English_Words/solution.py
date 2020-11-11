
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"

Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""
import sys
import pytest


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


@pytest.mark.parametrize('num, expected', [
    (123,"One Hundred Twenty Three"),
    (12345,"Twelve Thousand Three Hundred Forty Five"),
    (1234567,"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"),
    (1234567891,"One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"),
    (0, "Zero"),
    (18, "Eighteen"),
    (1000000, "One Million"),
    (1000010, "One Million Ten")
])
def test(num, expected):
    assert expected == Solution().numberToWords(num)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
