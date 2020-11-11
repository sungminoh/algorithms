#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.



Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199.
             1 + 99 = 100, 99 + 100 = 199


Constraints:

num consists only of digits '0'-'9'.
1 <= num.length <= 35
Follow up:
How would you handle overflow for very large input integers?
"""


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        for i in range(1, (len(num)-1) // 2 + 1):
            a, remain = num[:i], num[i:]
            if a.startswith('0') and len(a) > 1:
                break
            for j in range(1, len(num)-len(a)):
                b, remain2 = remain[:j], remain[j:]
                if b.startswith('0') and len(b) > 1:
                    break
                if self.is_additive(a, b, remain2):
                    return True
        return False

    def is_additive(self, a, b, num):
        # print(a, b, num)
        if not num:
            return True
        if num.startswith('0') and len(num) > 1:
            return False
        c = str(int(a) + int(b))
        if num.startswith(c) and self.is_additive(b, c, num[len(c):]):
            return True
        return False


if __name__ == '__main__':
    cases = [
        ('112358', True),
        ('199100199', True),
        ('123', True),
        ('5510', True),
        ('101', True),
        ('000', True),
        ('0235813', False),
    ]
    for case, expected in cases:
        actual = Solution().isAdditiveNumber(case)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
