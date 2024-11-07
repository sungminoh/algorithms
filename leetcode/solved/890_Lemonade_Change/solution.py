#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

Example 1:

Input: bills = [5,5,5,10,20]
Output: true
Explanation:
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

Example 2:

Input: bills = [5,5,10,10,20]
Output: false
Explanation:
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.

Constraints:

	1 <= bills.length <= 105
	bills[i] is either 5, 10, or 20.
"""
from collections import Counter
from typing import List
import pytest
import sys


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """Nov 06, 2024 15:42"""
        count = {20:0, 10:0, 5:0}
        for bill in bills:
            change = bill-5
            for b in [20, 10, 5]:
                while count[b] > 0 and b <= change:
                    change -= b
                    count[b] -= 1
            if change > 0:
                return False
            count[bill] += 1
        return True


@pytest.mark.parametrize('args', [
    (([5,5,5,10,20], True)),
    (([5,5,10,10,20], False)),
    (([5,5,5,10,5,5,10,20,20,20], False)),
])
def test(args):
    assert args[-1] == Solution().lemonadeChange(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
