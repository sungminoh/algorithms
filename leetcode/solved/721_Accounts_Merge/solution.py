#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts.  Two accounts definitely belong to the same person if there is some email that is common to both accounts.  Note that even if two accounts have the same name, they may belong to different people as people could have the same name.  A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order.  The accounts themselves can be returned in any order.

Example 1:

Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Note:
The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""
from pprint import pprint
import sys
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        names = dict()
        parents = dict()
        for name, *emails in accounts:
            for email in emails:
                while email in parents and email != parents[email]:
                    p = parents[email]
                    parents[email] = emails[0]
                    email = p
                parents[email] = emails[0]
            names[emails[0]] = name
        emails = defaultdict(set)
        for c, p in parents.items():
            stack = []
            while c != parents[c]:
                stack.append(c)
                c = parents[c]
                p = parents[p]
            emails[p].add(c)
            while stack:
                c = stack.pop()
                parents[c] = p
                emails[p].add(c)
        return [[names[e], *list(sorted(es))] for e, es in emails.items()]


@pytest.mark.parametrize('accounts, expected', [
    ([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]],
     [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]),
    ([["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]],
     [['Alex', 'Alex0@m.co', 'Alex4@m.co', 'Alex5@m.co'], ['Ethan', 'Ethan0@m.co', 'Ethan3@m.co'], ['Kevin', 'Kevin2@m.co', 'Kevin4@m.co'], ['Gabe', 'Gabe0@m.co', 'Gabe2@m.co', 'Gabe3@m.co', 'Gabe4@m.co']]),
    ([["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]],
     [["David","David0@m.co","David1@m.co","David3@m.co","David4@m.co","David5@m.co"]])
])
def test(accounts, expected):
    actual = Solution().accountsMerge(accounts)
    pprint(actual)
    assert sorted(expected) == sorted(actual)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
