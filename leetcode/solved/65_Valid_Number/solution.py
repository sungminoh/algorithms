#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.

"""
import re


class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if 'e' in s:
            s = s.split('e')
            return len(s) == 2 and self.isFloat(s[0]) and self.isInt(s[1])
        else:
            return self.isFloat(s)

    def isFloat(self, s):
        return re.search(r'[\d]+', s) is not None \
            and re.match(r'^[-+]?[\d]*\.?[\d]*$', s) is not None

    def isInt(self, s):
        return re.match(r'^[-+]?[\d]+$', s) is not None


def main():
    s = input()
    print(Solution().isNumber(s))


if __name__ == '__main__':
    main()
